#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Words starting with P that have 'u' - based on user's observation that
# the sign under POHOSTINSTVO starts with P
p_words = [
    "pukac", "pukas", "pukan", "pukalovic", "pukanic",
    "pupak", "pupala", "pupava", "pupek",
    "puska", "puskar", "puskas",
    "putovny", "putik", "putka",
    "pucik", "pudelko", "pudel",
    "pudik", "pudinka",
    "pumpa", "pumpaj",
    "punktik", "punkt",
    "puritan", "puritanka",
    "pustevnik", "pustina", "pusty",
    # Slovak surnames starting with Pu
    "pulkrabek", "pulkova", "puljic",
    "pundor", "pungor",
    "pupos", "pupov",
    "purgar", "purgat",
    "puskac", "puskaric", "puskajler",
    "putala", "putalik", "putek",
    "pudmar", "puha",
    # Common pub name patterns
    "primula", "primulu", "prvaka", "primera",
    "prajuci", "pratura", "priaznivcu",
    # Village-specific
    "polunku", "polniku", "polunocny",
]

test_cases = []
for word in p_words:
    cleaned = word.replace('u', '')
    if cleaned and len(cleaned) >= 2:
        test_cases.append((word, cleaned, cleaned))

# Also try first word as user, second as pass
# If sign says two words: "PUKÁŇ DUSAN" or similar
pairs = [
    ("pukandusan", "pkan", "dsan"),
    ("puskarjuraj", "pskar", "jraj"),
    ("pupavadubu", "ppava", "db"),
    ("pumpaludva", "pmpa", "ldva"),
    ("pukanniku", "pkann", "nik"),
]
test_cases.extend(pairs)

print(f"Testing {len(test_cases)} P-word combinations...")

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
