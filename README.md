# UKTE: Update Keyed Text Encrypt
Encrypt text with a key

click "Code>Download ZIP"
when the download is finished,
extract the ZIP file
open a terminal on the extracted folder
test `python --version`
if there is an error, install python/pip
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
