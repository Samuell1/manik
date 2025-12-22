import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter
import struct

def decrypt_encipher_v2(ciphertext, password):
    """Exact method that worked for level 16"""
    try:
        # Parse ENCT v2 format
        # Format: EnCt2<40 hex HMAC><24 hex partial><base64 data>IwEmS
        if not ciphertext.startswith('EnCt2') or not ciphertext.endswith('IwEmS'):
            return None
            
        middle = ciphertext[5:-5]  # Remove EnCt2 and IwEmS
        
        # First 40 chars are HMAC in hex
        hmac_part = middle[:40]
        # Next 24 chars are part of HMAC repeated
        middle = middle[40:]
        partial = middle[:24]
        # Rest is base64 data
        b64_data = middle[24:]
        
        # Decode base64
        data = base64.b64decode(b64_data)
        
        # First 8 bytes are salt
        salt = data[:8]
        # Next 8 bytes are nonce for CTR mode
        nonce = data[8:16]
        # Rest is ciphertext
        ct = data[16:]
        
        # Derive key with PBKDF2-SHA1, 1000 iterations
        key = PBKDF2(password.encode('utf-8'), salt, dkLen=16, count=1000, hmac_hash_module=hashlib.sha1)
        
        # AES-CTR decryption
        ctr = Counter.new(64, prefix=nonce, initial_value=0)
        cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
        plaintext = cipher.decrypt(ct)
        
        # Try to decode as UTF-8
        try:
            text = plaintext.decode('utf-8')
            # Check if it looks valid
            if len([c for c in text if c.isprintable() or c in '\n\r\t']) > len(text) * 0.8:
                return text
        except:
            pass
        
        # Try other encodings
        for enc in ['latin-1', 'cp1250', 'windows-1250']:
            try:
                text = plaintext.decode(enc)
                if len([c for c in text if c.isprintable() or c in '\n\r\t']) > len(text) * 0.7:
                    return text
            except:
                pass
                
    except Exception as e:
        pass
    return None

with open('prezident.enc', 'r') as f:
    ciphertext = f.read().strip()

# Extended password list
passwords = [
    # Direct hints
    'prezident', 'PREZIDENT', 
    # Permutation results  
    'nzupasoto', 'NZUPASOTO', 'zetpderni', 'ZETPDERNI',
    'poznoastu', 'POZNOASTU', 'nsopuoatz', 'NSOPUOATZ',
    # Video/channel
    'mnk', 'MNK', 'Mnk', '1hHcWSUxQB8', 'meandrekamenistehopotoka',
    # Latin phrase parts
    'pisces', 'mortui', 'solum', 'flumine', 'natant', 'piscesmortui',
    # Location/nature
    'meandre', 'meander', 'kamenisty', 'potok', 'polana', 'chko', 'sopsr',
    # Previous level answers
    'karosa', 'krcma', 'skodov', 'iveco', 'crossway',
    # Numbers
    '439167285', '4 3 9 1 6 7 2 8 5', '439', '167', '285',
    # Slovak president related
    'schuster', 'kovac', 'gasparovic', 'caputova', 'kiska', 'pellegrini',
    'rudolf', 'michal', 'ivan', 'zuzana', 'andrej', 'peter',
    # Nature protection
    'ochrana', 'prirody', 'statna', 'ochranar', 'les', 'lesy',
    # Latin for president
    'praeses', 'praesidens',
    # Sign text words
    'prirodzene', 'meandrujuci', 'tok', 'ktorom', 'mozno', 'dokladovat',
    'tvorba', 'dynamika', 'meandrov', 'dlzka', 'chraneneho', 'vytvoru',
    'neznecistujte', 'neposkodzujte', 'chranene', 'uzemie',
]

for pwd in passwords:
    result = decrypt_encipher_v2(ciphertext, pwd)
    if result and 'HRA' in result or (result and len(result) > 10):
        print(f"SUCCESS with: {pwd}")
        print("=" * 50)
        print(result[:500])
        break
else:
    print("No matching password found")
    
    # Show raw decryption attempts for first few passwords
    print("\nTrying raw decryption with first few passwords:")
    for pwd in passwords[:5]:
        result = decrypt_encipher_v2(ciphertext, pwd)
        if result:
            print(f"\n{pwd}: {result[:100]}...")
