#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encipher.it decryption using PyCryptodome

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA1, HMAC
import base64
import binascii
import sys
from Crypto.Util import Counter

def analyze(ciphertext):
    """Parse encipher.it format"""
    # Remove newlines/spaces
    ciphertext = ciphertext.replace('\n', '').replace(' ', '')

    # Format: EnCt2 + HMAC(40) + HMAC[:24](24) + salt(8) + base64(nonce+ct) + IwEmS
    if not ciphertext.startswith("EnCt2"):
        print(f"Warning: Expected 'EnCt2', got '{ciphertext[:5]}'")
    if not ciphertext.endswith("IwEmS"):
        print(f"Warning: Expected 'IwEmS', got '{ciphertext[-5:]}'")

    ct = ciphertext[5:-5]  # trim head and foot

    # Extract parts
    c_hmac = ct[:40]  # 40 hex chars
    # ct[40:64] is first 24 chars of HMAC repeated (skip)
    mac_salt = ct[64:72]  # 8 chars, base64 encoded
    b64_data = ct[72:]
    c_data = base64.b64decode(b64_data)
    ctr_nonce = c_data[:8]
    c_text = c_data[8:]

    return (c_hmac, mac_salt.encode('utf-8'), ctr_nonce, c_text)

def decrypt(password, ciphertext, verbose=False):
    """Decrypt encipher.it message"""
    c_hmac, mac_salt, ctr_nonce, c_text = analyze(ciphertext)

    if verbose:
        print(f"HMAC: {c_hmac}")
        print(f"Salt (base64): {mac_salt.decode()}")
        print(f"Nonce (hex): {binascii.hexlify(ctr_nonce).decode()}")
        print(f"Ciphertext: {len(c_text)} bytes")

    # Derive MAC key using PBKDF2-SHA1, 1000 iterations
    mac_key = PBKDF2(password.encode('utf-8'), mac_salt, dkLen=32, count=1000, hmac_hash_module=SHA1)
    mac_key_hex = binascii.hexlify(mac_key)

    if verbose:
        print(f"MAC key (hex): {mac_key_hex[:32].decode()}...")

    # Generate AES key: AES-ECB encrypt first 16 bytes of hex key
    keycipher = AES.new(mac_key_hex[:32], AES.MODE_ECB)
    aes_key_part = keycipher.encrypt(mac_key_hex[:16])
    aes_key = aes_key_part + aes_key_part  # Double it

    if verbose:
        print(f"AES key (hex): {binascii.hexlify(aes_key).decode()}")

    # Decrypt using AES-CTR with nonce + 8 zero bytes
    # CTR mode with 16-byte IV: nonce(8) + zeros(8)
    ctr = Counter.new(64, prefix=ctr_nonce, initial_value=0)
    cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr)
    message = cipher.decrypt(c_text)

    if verbose:
        try:
            print(f"Raw decrypted (first 100): {message[:100]}")
            printable = sum(1 for b in message[:50] if 32 <= b <= 126 or b in [10, 13])
            print(f"Printable chars in first 50: {printable}/50")
        except:
            pass

    # Verify HMAC
    h = HMAC.new(mac_key_hex, digestmod=SHA1)
    h.update(message)
    computed_hmac = h.hexdigest()

    if computed_hmac == c_hmac:
        try:
            return message.decode('utf-8')
        except:
            return message.decode('latin-1')
    else:
        if verbose:
            print(f"HMAC mismatch: computed={computed_hmac[:20]}... expected={c_hmac[:20]}...")
        return None

# Read encrypted file
with open('/home/user/manik/levels/16/ZV414BC', 'r') as f:
    encrypted = f.read().strip()

print(f"File length: {len(encrypted)}")
print()

# Parse and display structure
try:
    c_hmac, mac_salt, ctr_nonce, c_text = analyze(encrypted)
    print("=== Parsed encipher.it structure ===")
    print(f"HMAC: {c_hmac}")
    print(f"Salt: {mac_salt.decode()}")
    print(f"Nonce: {binascii.hexlify(ctr_nonce).decode()}")
    print(f"Ciphertext: {len(c_text)} bytes")
    print()
except Exception as e:
    print(f"Parse error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Comprehensive password list
passwords = [
    # Bus manufacturers
    "iveco", "IVECO", "Iveco", "irisbus", "IRISBUS", "Irisbus",
    "crossway", "CROSSWAY", "Crossway", "karosa", "KAROSA", "Karosa",
    "ivecobus", "IvecoBus", "IVECOBUS",

    # Bus operators
    "sad", "SAD", "Sad", "sadzvolen", "SADZvolen", "zvolen", "ZVOLEN",
    "zssk", "ZSSK",

    # Brewery / Beer
    "urpiner", "URPINER", "Urpiner", "pivovar", "PIVOVAR", "Pivovar",
    "pivo", "PIVO", "Pivo", "urpin", "URPIN", "Urpin",
    "pivovarbrezno", "brezno", "BREZNO", "Brezno",

    # Pub names
    "pohostinstvo", "POHOSTINSTVO", "Pohostinstvo",
    "hostinec", "HOSTINEC", "Hostinec",
    "krcma", "KRCMA", "Krcma", "pivnica", "PIVNICA",

    # Location related
    "lom", "LOM", "Lom", "rimavica", "RIMAVICA", "Rimavica",
    "lomnadrimavicou", "rimavicou", "nadrimavicou",

    # Coop Jednota
    "jednota", "JEDNOTA", "Jednota", "coop", "COOP", "Coop",
    "coopjednota", "jednotacoop",

    # Common establishment names
    "bufet", "BUFET", "jedalen", "JEDALEN",
    "restauracia", "motorest", "MOTOREST",
    "zastavka", "stanica", "autobusova",

    # Historical brewery names (Urpiner history)
    "heritz", "HERITZ", "Heritz",  # Original owner family
    "benus", "BENUS", "Benus",  # Later owner

    # Simple/common
    "heslo", "password", "test", "admin", "abc123",
]

print(f"=== Testing {len(passwords)} passwords ===")
for pwd in passwords:
    result = decrypt(pwd, encrypted)
    if result:
        print(f"\n*** SUCCESS with password: {pwd} ***")
        print(f"Decrypted:\n{result}")
        sys.exit(0)

print(f"\nNo match found.")
print("\n=== Verbose test with 'urpiner' ===")
decrypt("urpiner", encrypted, verbose=True)
