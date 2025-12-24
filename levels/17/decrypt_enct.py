import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import sys

def decrypt_encipher(ciphertext, password):
    """Decrypt encipher.it format (ENCT v2)"""
    try:
        # Parse format: EnCt2 + 40 hex HMAC + 24 hex + Base64 + IwEmS
        if not ciphertext.startswith('EnCt2'):
            return None
        
        content = ciphertext[5:-5]  # Remove EnCt2 and IwEmS
        
        # Extract HMAC (40 hex = 20 bytes)
        hmac_hex = content[:40]
        rest = content[40:]
        
        # Skip next 24 hex chars (partial HMAC)
        if len(rest) > 24:
            rest = rest[24:]
        
        # Rest is Base64 encoded
        try:
            encrypted = base64.b64decode(rest)
        except:
            return None
        
        # Derive key using PBKDF2
        salt = encrypted[:8]
        cipherdata = encrypted[8:]
        
        key = PBKDF2(password.encode(), salt, dkLen=32, count=1000, hmac_hash_module=hashlib.sha1)
        
        # Try AES-CTR mode
        nonce = cipherdata[:8]
        ct = cipherdata[8:]
        
        # Create counter
        from Crypto.Util import Counter
        ctr = Counter.new(64, prefix=nonce, initial_value=0)
        cipher = AES.new(key[:16], AES.MODE_CTR, counter=ctr)
        
        plaintext = cipher.decrypt(ct)
        
        # Check if result looks like text
        try:
            text = plaintext.decode('utf-8', errors='ignore')
            if any(c.isalpha() for c in text[:50]):
                return text
        except:
            pass
            
    except Exception as e:
        pass
    return None

# Read encrypted content
with open('prezident.enc', 'r') as f:
    ciphertext = f.read().strip()

# Try passwords
passwords = [
    'prezident', 'PREZIDENT', 'Prezident',
    'kovac', 'schuster', 'gasparovic', 'kiska', 'caputova', 'pellegrini',
    'meandre', 'potoka', 'kamenista', 'dolina',
    'poznoastu', 'nzupasoto', 'zetpderni',
    'sopsr', 'ochrana', 'priroda', 'prirody',
    'youtube', 'video', 'pisces', 'mortui',
    'karosa', 'sihla', 'krcma', 'skodov',
    '1hHcWSUxQB8', 'vyhliadka', 'vyhliadke'
]

for pwd in passwords:
    result = decrypt_encipher(ciphertext, pwd)
    if result:
        print(f"Password: {pwd}")
        print(f"Decrypted: {result[:200]}...")
        break
else:
    print("No password worked")
