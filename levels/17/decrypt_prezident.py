#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import ECB, CTR
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
import base64
import binascii

ENCT2_HEAD = "EnCt2"
ENCT2_FOOT = "IwEmS"

def analyze(ciphertext):
    ciphertext = ciphertext.replace('\n', '').replace(' ', '')
    ct = ciphertext[5:-5]
    c_hmac = ct[:40]
    mac_salt = ct[64:72].encode('utf8')
    c_text = base64.b64decode(ct[72:])
    ctr_nonce, c_text = c_text[:8], c_text[8:]
    return (c_hmac, mac_salt, ctr_nonce, c_text)

def decrypt(password, ciphertext):
    try:
        c_hmac, mac_salt, ctr_nonce, c_text = analyze(ciphertext)
        mac_kdf = PBKDF2HMAC(algorithm=SHA1(), length=32, salt=mac_salt,
                             iterations=1000, backend=default_backend())
        mac_key = mac_kdf.derive(password.encode("utf-8"))
        mac_key = binascii.hexlify(mac_key)
        
        keycipher = Cipher(algorithm=AES(mac_key[:32]), mode=ECB(), backend=default_backend())
        keycipher = keycipher.encryptor()
        aes_key = keycipher.update(mac_key[:16]) + keycipher.finalize()
        aes_key += aes_key
        
        cipher = Cipher(algorithm=AES(aes_key), mode=CTR(ctr_nonce + bytes(8)), backend=default_backend())
        cipher = cipher.decryptor()
        message = cipher.update(c_text) + cipher.finalize()
        
        mac = HMAC(key=mac_key, algorithm=SHA1(), backend=default_backend())
        mac.update(message)
        mac.verify(binascii.unhexlify(c_hmac))
        return message.decode('utf-8')
    except:
        return None

with open('prezident.enc', 'r') as f:
    encrypted = f.read().strip()

passwords = [
    # Permutation results
    'nzupasoto', 'zetpderni', 'poznoastu', 'nsopuoatz',
    # President related
    'prezident', 'president', 'hlava', 'hlavaštatu',
    # Slovak presidents
    'schuster', 'gasparovic', 'kiska', 'caputova', 'pellegrini', 'kovac',
    'rudolf', 'ivan', 'andrej', 'zuzana', 'peter', 'michal',
    # Video/channel
    'mnk', '1hHcWSUxQB8', 'meandre', 'kamenistypotok',
    # Latin
    'pisces', 'mortui', 'flumine', 'natant', 'solum',
    # Location
    'polana', 'sihla', 'hroncek', 'brezno', 'detva',
    # Nature protection
    'sopsr', 'ochrana', 'priroda', 'chko', 'statna',
    # Previous levels
    'karosa', 'krcma', 'skodov', 'vrak', 'auto',
    # Sign text
    'meandry', 'potoka', 'chraneny', 'areal', 'uzemie',
    # First letters
    'ppmmtnkkm',
    # Numbers
    '439167285', 'styritridevat',
]

print("Testing passwords for prezident.enc...")
for pwd in passwords:
    result = decrypt(pwd, encrypted)
    if result:
        print(f"\n*** SUCCESS: {pwd} ***")
        print("=" * 60)
        print(result)
        break
else:
    print(f"No match found with {len(passwords)} passwords")
