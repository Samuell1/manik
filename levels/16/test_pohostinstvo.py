#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Under "POHOSTINSTVO" sign - possible texts that start with P
# and have 'u' (6-7 characters as user mentioned)
test_cases = [
    # PUTIKA (small pub) variations
    ("putika", "ptika", "ptika"),
    ("putiku", "ptik", "ptik"),
    ("putikar", "ptikar", "ptikar"),
    
    # PÚPAVA (dandelion)
    ("pupava", "ppava", "ppava"),
    ("pupavu", "ppav", "ppav"),
    
    # PUMPA (pump)
    ("pumpak", "pmpak", "pmpak"),
    ("pumpou", "pmpo", "pmpo"),
    
    # PUSTÝ/PUSTKA (empty/wasteland)
    ("pustka", "pstka", "pstka"),
    ("pustak", "pstak", "pstak"),
    
    # PUTOVNÝ (traveling)
    ("putovny", "ptovny", "ptovny"),
    
    # PUKÁŇ and similar surnames
    ("pukanov", "pkanov", "pkanov"),
    ("pukanovi", "pkanovi", "pkanovi"),
    ("pukanom", "pkanom", "pkanom"),
    
    # PRUŽINA (spring/coil)
    ("pruzina", "przina", "przina"),
    
    # Under POHOSTINSTVO might be owner's name
    # Format: "POHOSTINSTVO U [NAME]" or just "[NAME]"
    ("ujulia", "jlia", "jlia"),
    ("ujulika", "jlika", "jlika"),
    ("ukubana", "kbana", "kbana"),
    ("udusana", "dsana", "dsana"),
    ("ujuraja", "jraja", "jraja"),
    ("ujurka", "jrka", "jrka"),
    ("uburiana", "briana", "briana"),
    
    # Place name variants
    ("primula", "primla", "primla"),  # type of flower, common cafe/pub name
    ("primulu", "priml", "priml"),
    
    # POSUDEK/POSUNEK (judgment/gesture)
    ("posunek", "posnek", "posnek"),
    ("posudek", "posdek", "posdek"),
    
    # Common pub/establishment names starting with P
    ("pezinok", "pezinok", "pezinok"),  # no u
    ("poluvka", "polvka", "polvka"),  # soup
    ("palenka", "palenka", "palenka"),  # brandy - no u
    ("pivaren", "pivaren", "pivaren"),  # no u
    
    # PODUNAJSK- (Danubian)
    ("podunaj", "podnaj", "podnaj"),
    ("podunajsko", "podnajsko", "podnajsko"),
    
    # Try with second word
    ("putika julia", "ptika", "jlia"),
    ("putika julius", "ptika", "jlis"),
    ("putika kuban", "ptika", "kban"),
    ("pupava ruzena", "ppava", "rzena"),
]

print(f"Testing {len(test_cases)} POHOSTINSTVO-related combinations...")

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
