#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Common Slovak words with 'u' that might be on signs
words_with_u = [
    # Common fence/sign words
    "sukromne", "sukromny", "sukromneho", "sukromnepozemok",
    "cudzi", "cudzim", "cudzich", "cudzieho",
    "vstup", "vstupu", "vstupom", "vstupovat",
    "zakazu", "zakazuje", "zakazany", "zakazaneho",
    "pozoru", "porucha", "poruchy",
    
    # Building names
    "kulturny", "kulturneho", "kulturnehodomu",
    "ustredna", "ustredny", "ustredneho",
    "muzeum", "muzea", "muzeom",
    
    # Common surnames with u
    "kubik", "kubica", "kuban", "kubas", "kubat",
    "dusan", "dusana", "dusanom",
    "rudolf", "rudolfa", "rudolfom",
    "julius", "juliusa", "juliusom",
    "lukac", "lukaca", "lukacom",
    "juraj", "juraja", "jurajom",
    "burian", "buriana", "burianom",
    "burgr", "burgra", "burgrom",
    "turcan", "turcana", "turcanom",
    "rusnak", "rusnaka", "rusnakom",
    
    # Place-related with u
    "ulica", "ulice", "ulicou",
    "studna", "studne", "studnou",
    "pumpa", "pumpe", "pumpou",
    "huta", "hute", "hutou",
    "luka", "luke", "lukou",
    "buda", "bude", "budou",
    "mur", "mure", "murom",
    
    # Food/drink related (pub signs)
    "bufet", "bufetu", "bufetom",
    "vycap", "vycapu", "vycapom",
    "pivo", "pivu", "pivom",  # no u actually
    "vinum", "vina",
    
    # Old Slovak/historical
    "uprava", "upravy", "upravou",
    "utulek", "utulku", "utulkom",
    "uzemie", "uzemim", "uzemiu",
    
    # Government/admin
    "urad", "uradu", "uradom",
    "ustav", "ustavu", "ustavom",
    
    # Animal related (farm signs)
    "suhaj", "suhaja", "suhajom",
    "kurnik", "kurnika", "kurnikom",
    "volk", "volku", "volkom",  # no u
    
    # Simple words
    "dub", "dubu", "dubom",
    "kut", "kutu", "kutom",
    "sud", "sudu", "sudom",
    "muk", "muku", "mukom",
    "tuk", "tuku", "tukom",
    "lup", "lupu", "lupom",
    "sup", "supu", "supom",
    "cup", "cupu", "cupom",
    "dup", "dupu", "dupom",
    "hup", "hupu", "hupom",
    "puk", "puku", "pukom",
    "suk", "suku", "sukom",
    "zub", "zubu", "zubom",
    "rub", "rubu", "rubom",
    "hub", "hubu", "hubom",
    "klub", "klubu", "klubom",
]

# Generate test cases - remove 'u' and use same for both user/pass
test_cases = []
for word in words_with_u:
    cleaned = word.replace('u', '')
    if cleaned and len(cleaned) >= 2:
        test_cases.append((word, cleaned, cleaned))

# Also test lowercase and uppercase variations
for word in words_with_u[:20]:  # First 20 only
    cleaned = word.replace('u', '')
    if cleaned:
        test_cases.append((word.upper(), cleaned.upper(), cleaned.upper()))

print(f"Testing {len(test_cases)} word combinations...")

found = False
for i, (orig, user, pwd) in enumerate(test_cases):
    if i % 50 == 0:
        print(f"Progress: {i}/{len(test_cases)}")
    try:
        r = requests.get(url, auth=HTTPBasicAuth(user.lower(), pwd.lower()), timeout=10, verify=False)
        if r.status_code == 200:
            print(f"\n*** SUCCESS! ***")
            print(f"Original: {orig}")
            print(f"Username: {user.lower()}")
            print(f"Password: {pwd.lower()}")
            found = True
            break
    except Exception as e:
        pass

if not found:
    print("\nNo match found")
