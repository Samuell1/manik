import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter

def decrypt_encipher(ciphertext, password):
    try:
        if not ciphertext.startswith('EnCt2'):
            return None
        
        content = ciphertext[5:-5]
        hmac_hex = content[:40]
        rest = content[40:]
        
        if len(rest) > 24 and all(c in '0123456789abcdefABCDEF' for c in rest[:24]):
            rest = rest[24:]
        
        encrypted = base64.b64decode(rest)
        salt = encrypted[:8]
        cipherdata = encrypted[8:]
        
        key = PBKDF2(password.encode(), salt, dkLen=32, count=1000, hmac_hash_module=hashlib.sha1)
        
        nonce = cipherdata[:8]
        ct = cipherdata[8:]
        
        ctr = Counter.new(64, prefix=nonce, initial_value=0)
        cipher = AES.new(key[:16], AES.MODE_CTR, counter=ctr)
        
        plaintext = cipher.decrypt(ct)
        text = plaintext.decode('utf-8', errors='ignore')
        
        # Check for readable content
        if 'HRA' in text or 'manik' in text or any(word in text.lower() for word in ['heslo', 'meno', 'level', 'dalsi']):
            return text
        if sum(1 for c in text[:100] if c.isalpha()) > 30:
            return text
            
    except Exception as e:
        pass
    return None

with open('prezident.enc', 'r') as f:
    ciphertext = f.read().strip()

passwords = [
    # Video and channel related
    '1hHcWSUxQB8', 'MnkFcbk', 'Mnk', 'mnk', 'pisces', 'mortui', 'flumine', 'natant',
    # Sign text
    'meandre', 'kamenisty', 'potok', 'potoka', 'kamenistypotok',
    # Protected area
    'sopsr', 'sop', 'chko', 'polana', 'chraneny', 'areal', 'cha',
    # Location
    'sihla', 'hronec', 'hroncek', 'dolina', 'kamenistadolina',
    # Previous answers
    'karosa', 'krcma', 'skodov', 'vrak', 'auto',
    # Numbers as text
    'styri', 'tri', 'devat', 'jeden', 'sest', 'sedem', 'dva', 'osem', 'pat',
    # Permutation results
    'poznoastu', 'nzupasoto', 'ppmmtnkkm',
    # Presidents
    'schuster', 'rudolf', 'gasparovic', 'ivan', 'kiska', 'andrej',
    # Latin
    'piscesmortui', 'solumc umflumine',
    # Others
    'vyhliadka', 'rozhladna', 'turistika', 'príroda', 'priroda', 'ochrana'
]

for pwd in passwords:
    result = decrypt_encipher(ciphertext, pwd)
    if result:
        print(f"SUCCESS! Password: {pwd}")
        print(f"Content:\n{result}")
        break
else:
    print("No password found. Trying more...")
    # Try lowercase/uppercase variants
    for pwd in ['MEANDRE', 'Meandre', 'POTOKA', 'Potoka', 'PREZIDENT', 'SOPSR', 'CHKO', 'POLANA']:
        result = decrypt_encipher(ciphertext, pwd)
        if result:
            print(f"SUCCESS! Password: {pwd}")
            print(f"Content:\n{result}")
            break
