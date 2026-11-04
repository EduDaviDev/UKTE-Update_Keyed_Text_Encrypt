from unicodedata import normalize


class UKTECipher:
    """Keyed text cipher using a reversible character-level transform."""

    MIN_CKEY = 3  # below this, the transform is not bijective

    def __init__(self, key: str | None = None) -> None:
        self._ckey = self.MIN_CKEY
        if key is not None:
            self.set_key(key)

    @property
    def ckey(self) -> int:
        """Current effective key."""
        return self._ckey

    def set_key(self, key: str) -> int:
        """Derive and store the numeric key from a text key."""
        if not key:
            raise ValueError("Key cannot be empty.")

        key_bytes = key.encode("utf-8")
        key_hex = key_bytes.hex().upper()
        k1 = int.from_bytes(key_bytes, "big")

        key_nums = [int(ch, 16) for ch in key_hex]
        k2 = sum(n * k1 for n in key_nums)

        k3 = k2 // k1
        k4 = abs((k1 // k3) - k2)

        ckey = abs(((k1 + k2) * (k3 + k4)) // k1)
        if ckey < self.MIN_CKEY:
            ckey = self.MIN_CKEY

        self._ckey = ckey
        return ckey

    def _width(self) -> int:
        """Hex field width based on ((255 * ckey) + ckey) / 3."""
        max_num = (255 * self._ckey + self._ckey) // 3
        return len(format(max_num, "X"))

    def encrypt(self, text: str) -> str:
        """Encrypt `text` into an uppercase hexadecimal string."""
        text = normalize("NFC", text)
        w = self._width()
        out = []
        for c in text:
            # Requested formula: ((c * ckey) + ckey) / 3
            n = (ord(c) * self._ckey + self._ckey) // 3
            out.append(format(n, f"0{w}X"))
        return "".join(out)

    def decrypt(self, text: str) -> str:
        """Decrypt a hexadecimal string produced by `encrypt`."""
        w = self._width()
        if len(text) % w != 0:
            raise ValueError("Invalid encrypted text.")

        out = []
        for pos in range(0, len(text), w):
            n = int(text[pos : pos + w], 16)
            # Inverse of n = (c * ckey + ckey) // 3
            c = (3 * n + self._ckey - 1) // self._ckey - 1
            out.append(chr(c))
        return "".join(out)
