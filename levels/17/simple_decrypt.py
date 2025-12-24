import base64
import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter
from Crypto.Hash import HMAC as CRYPTO_HMAC, SHA1

def analyze(ciphertext):
    ciphertext = ciphertext.replace('\n', '').replace(' ', '')
    ct = ciphertext[5:-5]  # Remove EnCt2 and IwEmS
    c_hmac = ct[:40]
    mac_salt = ct[64:72].encode('utf8')
    c_text = base64.b64decode(ct[72:])
    ctr_nonce, c_text = c_text[:8], c_text[8:]
    return (c_hmac, mac_salt, ctr_nonce, c_text)

def decrypt(password, ciphertext):
    try:
        c_hmac, mac_salt, ctr_nonce, c_text = analyze(ciphertext)
        
        # PBKDF2 key derivation
        mac_key = PBKDF2(password.encode('utf-8'), mac_salt, dkLen=32, count=1000, hmac_hash_module=hashlib.sha1)
        mac_key_hex = binascii.hexlify(mac_key)
        
        # AES-ECB for key generation
        cipher_ecb = AES.new(mac_key_hex[:32], AES.MODE_ECB)
        aes_key = cipher_ecb.encrypt(mac_key_hex[:16])
        aes_key = aes_key + aes_key  # Double it
        
        # AES-CTR for decryption
        ctr = Counter.new(64, prefix=ctr_nonce, initial_value=0)
        cipher_ctr = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
        message = cipher_ctr.decrypt(c_text)
        
        # Verify HMAC
        h = CRYPTO_HMAC.new(mac_key_hex, message, SHA1)
        computed_hmac = h.hexdigest()
        
        if computed_hmac == c_hmac:
            return message.decode('utf-8')
    except Exception as e:
        pass
    return None

with open('prezident.enc', 'r') as f:
    encrypted = f.read().strip()

passwords = [
    'nzupasoto', 'zetpderni', 'poznoastu', 'nsopuoatz', 'prezident',
    'schuster', 'gasparovic', 'kiska', 'caputova', 'pellegrini', 'kovac',
    'mnk', '1hHcWSUxQB8', 'meandre', 'pisces', 'mortui', 'flumine',
    'polana', 'sihla', 'sopsr', 'ochrana', 'karosa', 'krcma', 'skodov',
    'ppmmtnkkm', '439167285', 'potoka', 'chko', 'meandry'
]

print("Testing...")
for pwd in passwords:
    result = decrypt(pwd, encrypted)
    if result:
        print(f"\n*** FOUND: {pwd} ***\n{result}")
        break
else:
    print("No match")
