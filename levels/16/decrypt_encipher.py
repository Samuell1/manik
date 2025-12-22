#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Correct encipher.it decryption based on official algorithm

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
import sys

ENCT2_HEAD = "EnCt2"
ENCT2_FOOT = "IwEmS"

def analyze(ciphertext):
    """Parse encipher.it format"""
    # Remove newlines/spaces
    ciphertext = ciphertext.replace('\n', '').replace(' ', '')

    # Check header and footer
    if not ciphertext.startswith(ENCT2_HEAD):
        print(f"Warning: Expected header '{ENCT2_HEAD}', got '{ciphertext[:5]}'")
    if not ciphertext.endswith(ENCT2_FOOT):
        print(f"Warning: Expected footer '{ENCT2_FOOT}', got '{ciphertext[-5:]}'")

    ct = ciphertext[5:-5]  # trim head and foot

    # Extract parts based on algorithm
    c_hmac = ct[:40]  # 40 hex chars
    # ct[40:64] is first 24 chars of HMAC repeated (skip)
    mac_salt = ct[64:72].encode('utf8')  # 8 chars, base64 encoded
    c_text = base64.b64decode(ct[72:])
    ctr_nonce, c_text = c_text[:8], c_text[8:]

    return (c_hmac, mac_salt, ctr_nonce, c_text)

def decrypt(password, ciphertext, verbose=False):
    """Decrypt encipher.it message"""
    # Extract parts
    c_hmac, mac_salt, ctr_nonce, c_text = analyze(ciphertext)

    if verbose:
        print(f"HMAC: {c_hmac}")
        print(f"Salt (base64): {mac_salt}")
        print(f"Nonce (hex): {binascii.hexlify(ctr_nonce)}")
        print(f"Ciphertext length: {len(c_text)} bytes")

    # Derive key (using PBKDF2)
    mac_kdf = PBKDF2HMAC(algorithm=SHA1(),
                         length=32,
                         salt=mac_salt,
                         iterations=1000,
                         backend=default_backend())
    mac_key = mac_kdf.derive(password.encode("utf-8"))
    mac_key = binascii.hexlify(mac_key)

    if verbose:
        print(f"Derived key (hex): {mac_key[:32]}...")

    # Generate key for decryption (using AES)
    keycipher = Cipher(algorithm=AES(mac_key[:32]),
                       mode=ECB(),
                       backend=default_backend())
    keycipher = keycipher.encryptor()
    aes_key = keycipher.update(mac_key[:16]) + keycipher.finalize()
    aes_key += aes_key  # Double the key

    # Decrypt the ciphertext (using AES in CTR-mode)
    cipher = Cipher(algorithm=AES(aes_key),
                    mode=CTR(ctr_nonce + bytes(8)),
                    backend=default_backend())
    cipher = cipher.decryptor()

    message = cipher.update(c_text) + cipher.finalize()

    # Check the HMAC over the message (using SHA1)
    mac = HMAC(key=mac_key,
               algorithm=SHA1(),
               backend=default_backend())
    mac.update(message)

    try:
        mac.verify(binascii.unhexlify(c_hmac))
        return message.decode('utf-8')
    except InvalidSignature:
        return None
    except:
        return None

def try_password(password, ciphertext, verbose=False):
    """Try a single password and return result or None"""
    try:
        result = decrypt(password, ciphertext, verbose)
        if result:
            return result
    except Exception as e:
        if verbose:
            print(f"Error with '{password}': {e}")
    return None

# Read encrypted file
with open('/home/user/manik/levels/16/ZV414BC', 'r') as f:
    encrypted = f.read().strip()

print(f"Encrypted data length: {len(encrypted)}")
print(f"First 20 chars: {encrypted[:20]}")
print(f"Last 20 chars: {encrypted[-20:]}")
print()

# Analyze structure
try:
    c_hmac, mac_salt, ctr_nonce, c_text = analyze(encrypted)
    print("=== Parsed structure ===")
    print(f"HMAC (40 chars): {c_hmac}")
    print(f"Salt (8 chars base64): {mac_salt.decode()}")
    print(f"Nonce (8 bytes hex): {binascii.hexlify(ctr_nonce).decode()}")
    print(f"Ciphertext: {len(c_text)} bytes")
    print()
except Exception as e:
    print(f"Parse error: {e}")
    sys.exit(1)

# Password candidates based on hints:
# "kľúč je názov podniku, ktorý ho vyrobil" = key is name of company that made it
# "dolezita zastavka je v Lome nad Rimavicou" = important stop in Lom nad Rimavicou
# Images show: POHOSTINSTVO sign, Urpiner beer advertisement

passwords = [
    # Bus manufacturers
    "iveco", "IVECO", "Iveco", "irisbus", "IRISBUS", "Irisbus",
    "crossway", "CROSSWAY", "Crossway", "karosa", "KAROSA", "Karosa",

    # Bus operators
    "sad", "SAD", "Sad", "sadzvolen", "SADZvolen", "zvolen", "ZVOLEN",

    # Brewery / Beer
    "urpiner", "URPINER", "Urpiner", "pivovar", "PIVOVAR", "Pivovar",
    "pivo", "PIVO", "Pivo", "urpin", "URPIN", "Urpin",

    # Pub names
    "pohostinstvo", "POHOSTINSTVO", "Pohostinstvo",
    "hostinec", "HOSTINEC", "Hostinec",
    "krcma", "KRCMA", "Krcma",

    # Location related
    "lom", "LOM", "Lom", "rimavica", "RIMAVICA", "Rimavica",
    "lomnadrimavicou", "rimavicou",

    # Coop Jednota (store in village)
    "jednota", "JEDNOTA", "Jednota", "coop", "COOP", "Coop",
    "coopjednota", "jednotacoop",

    # Common pub/restaurant names in Slovakia
    "bufet", "BUFET", "Bufet",
    "restauracia", "RESTAURACIA",
    "jedalen", "JEDALEN",
    "motorest", "MOTOREST",

    # Place-related
    "zastavka", "ZASTAVKA", "zastávka",
    "stanica", "STANICA",

    # Simple passwords
    "heslo", "password", "test", "admin",
]

print("=== Testing passwords ===")
for pwd in passwords:
    result = try_password(pwd, encrypted)
    if result:
        print(f"\n*** SUCCESS with password: {pwd} ***")
        print(f"Decrypted: {result}")
        sys.exit(0)

print(f"\nNo match found with {len(passwords)} passwords.")
print("\nTrying verbose mode with 'urpiner'...")
result = try_password("urpiner", encrypted, verbose=True)
