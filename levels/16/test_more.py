#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# More comprehensive list
# Format: (original, user, password)
test_cases = [
    # Common fence signs - "SÚKROMNÉ" (Private)
    ("sukromne", "skromne", "skromne"),
    ("sukromny", "skromny", "skromny"),
    ("sukromnepoze", "skromne", "pozemok"),  # Private land - split
    
    # "KULTÚRNY DOM" (Cultural house) - common in villages
    ("kulturny", "kltrny", "kltrny"),
    ("kulturnydom", "kltrny", "dom"),
    
    # "ZÁKAZ VSTUPU" (No entry)
    ("zakazvstupu", "zakaz", "vstp"),
    
    # Local cottage names found in search
    ("limboru", "limbor", "limbor"),  # Drevenica Limbora without u
    ("kovacicu", "kovacic", "kovacic"),  # Drevenica Kovačica without u
    
    # "U XXXX" style pub/house names
    ("ukubana", "kbana", "kbana"),
    ("udusana", "dsana", "dsana"),
    ("ulukaca", "lkaca", "lkaca"),
    ("uburku", "brk", "brk"),
    ("uburaka", "braka", "braka"),
    ("uburiana", "briana", "briana"),
    
    # Municipal office number is 13, so opposite might be related
    ("dom13", "dom13", "dom13"),
    ("cislo14", "cislo14", "cislo14"),
    
    # "DÚLAVA" / "ÚDOLINA" (valley related - kamenista dolina hint)
    ("udolina", "dolina", "dolina"),
    ("dulava", "dlava", "dlava"),
    
    # Heritage houses mentioned (No. 32, No. 74)
    ("dom32u", "dom32", "dom32"),
    ("dom74u", "dom74", "dom74"),
    
    # Forgách family (founders) - surname variations
    ("forgacu", "forgac", "forgac"),
    ("forgacov", "forgacov", "forgacov"),
    
    # Try without diacritics - common words
    ("chudoba", "chdoba", "chdoba"),  # poverty
    ("slobodu", "slobod", "slobod"),  # freedom
    ("republika", "repblika", "repblika"),  # republic
    ("komunizmus", "komniزms", "komnizms"),  # communism (old sign?)
    
    # Simple common names
    ("burian", "brian", "brian"),
    ("bugaj", "bgaj", "bgaj"),
    ("bukva", "bkva", "bkva"),
    ("bukla", "bkla", "bkla"),
    ("burda", "brda", "brda"),
    ("murko", "mrko", "mrko"),
    ("puska", "pska", "pska"),
    ("dusek", "dsek", "dsek"),
    ("musil", "msil", "msil"),
    ("kuciak", "kciak", "kciak"),
    ("kucera", "kcera", "kcera"),
    
    # Double u words
    ("bubuk", "bbk", "bbk"),
    ("duduk", "ddk", "ddk"),
    ("kukuc", "kkc", "kkc"),
    
    # Try single word as both
    ("budka", "bdka", "bdka"),
    ("buzka", "bzka", "bzka"),
    ("butka", "btka", "btka"),
    ("cukra", "ckra", "ckra"),
    ("dukla", "dkla", "dkla"),
    ("fucik", "fcik", "fcik"),
    ("hudak", "hdak", "hdak"),
    ("jurek", "jrek", "jrek"),
    ("kukan", "kkan", "kkan"),
    ("lucan", "lcan", "lcan"),
    ("mucha", "mcha", "mcha"),
    ("pulka", "plka", "plka"),
    ("ruban", "rban", "rban"),
    ("sukan", "skan", "skan"),
    ("tukan", "tkan", "tkan"),
    ("zufan", "zfan", "zfan"),
]

print(f"Testing {len(test_cases)} combinations...")

for orig, user, pwd in test_cases:
    try:
        r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=10, verify=False)
        if r.status_code == 200:
            print(f"\n*** SUCCESS! ***")
            print(f"Original: {orig}")
            print(f"Username: {user}")
            print(f"Password: {pwd}")
            break
    except Exception as e:
        pass

print("\nDone")
