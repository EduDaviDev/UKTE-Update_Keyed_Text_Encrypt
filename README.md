# UKTE: Update Keyed Text Encrypt
Encrypt text with a key

click "Code>Download ZIP"<br>
when the download is finished,<br>
extract the ZIP file<br>
open a terminal on the extracted folder<br>
test `python --version`<br>
if there is an error, install python/pip<br>
rum `pip install -e .`

### Usage:

```python
import ukte

# Create the instance using the key
cipher = ukte.UKTECipher("HI")

# Test
original_text = "Hello world!"
print(f"Original:  {original_text}")

encrypted = cipher.encrypt(original_text)
print(f"Encrypted: {encrypted}")

decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```
