from unicodedata import normalize

ckey = 1


def setkey(key):
    """Set the current key."""
    global ckey
    if not key:
        raise ValueError("Key cannot be empty.")

    key_bytes = key.encode("utf-8")
    key_hex = key_bytes.hex().upper()
    k1 = int.from_bytes(key_bytes, "big")

    con = {str(i): i for i in range(10)}
    con.update({chr(ord('a') + i): 10 + i for i in range(6)})

    key_nums = [con[ch.lower()] for ch in key_hex]
    k2 = sum(n * k1 for n in key_nums)

    k3 = k2 // k1
    k4 = abs((k1 // k3) - k2)

    ckey = abs(((k1 + k2) * (k3 + k4)) // k1)

    # Must be >= 3 for decrypt to be unique
    if ckey < 3:
        ckey = 3

    print(f"ckey = {ckey}")


def _width():
    """Hex field width: based on ((255 * ckey) + ckey) / 3."""
    max_num = (255 * ckey + ckey) // 3
    return len(format(max_num, 'X'))


def encrypt(text):
    """Encrypt the text -> hexadecimal."""
    text = normalize("NFC", text)
    w = _width()
    out = []
    for c in text:
        # (c * ckey + ckey) / 3 -> integer (same as int(.../3))
        n = (ord(c) * ckey + ckey) // 3
        out.append(format(n, f'0{w}X'))
    return "".join(out)


def decrypt(text):
    """Decrypt the hexadecimal -> text."""
    w = _width()
    if len(text) % w != 0:
        raise ValueError("Invalid encrypted text.")

    out = []
    for pos in range(0, len(text), w):
        n = int(text[pos:pos + w], 16)
        # Inverse of n = (c*ckey + ckey) // 3
        c = (3 * n + ckey - 1) // ckey - 1
        out.append(chr(c))
    return "".join(out)