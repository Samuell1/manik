#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

# URL to test
url = "https://manik.sk/hra/kamenista_dolina/"

# Common Slovak words/names with 'u' that could be on a fence
# After removing 'u' we get credentials

# Format: (original_with_u, username, password)
# Based on hint: removing lowercase 'u' gives username AND password

test_cases = [
    # Same word for both
    ("burian", "brian", "brian"),
    ("burka", "brka", "brka"),
    ("bukva", "bkva", "bkva"),
    ("kukla", "kkla", "kkla"),
    ("buka", "bka", "bka"),
    ("kura", "kra", "kra"),
    ("suka", "ska", "ska"),
    ("tuka", "tka", "tka"),
    ("luka", "lka", "lka"),
    ("muka", "mka", "mka"),
    ("ruka", "rka", "rka"),
    ("pukla", "pkla", "pkla"),
    ("dukla", "dkla", "dkla"),
    ("bukla", "bkla", "bkla"),
    ("mukla", "mkla", "mkla"),
    
    # Common surnames after removing u
    ("burian", "brian", "brian"),
    ("bugaj", "bgaj", "bgaj"),
    ("bugar", "bgar", "bgar"),
    ("burat", "brat", "brat"),
    ("buran", "bran", "bran"),
    ("kuban", "kban", "kban"),
    ("lukac", "lkac", "lkac"),
    ("ruzan", "rzan", "rzan"),
    ("dusan", "dsan", "dsan"),
    ("rudolf", "rdolf", "rdolf"),
    
    # Pub names "U XXX" - removing u from U + name
    ("u brata", "brata", "brata"),  # At brother's
    ("u burku", "brk", "brk"),
    ("u buraka", "braka", "braka"),
    ("u lukaca", "lkaca", "lkaca"),
    ("u kubana", "kbana", "kbana"),
    
    # Two-word signs (first word username, second password)
    ("sukromny", "skromny", "skromny"),  # Private
    ("kulturny", "kltrny", "kltrny"),  # Cultural
    
    # Simple with u removed
    ("ruda", "rda", "rda"),
    ("muda", "mda", "mda"),
    ("luda", "lda", "lda"),
    ("huta", "hta", "hta"),
    ("buda", "bda", "bda"),
    ("cuda", "cda", "cda"),
    ("suda", "sda", "sda"),
    
    # Penzion/accommodation names
    ("vrchar", "vrchar", "vrchar"),  # Penzion Vrchar (no u)
    ("turista", "trista", "trista"),
    ("turistu", "trist", "trist"),
    
    # Location based
    ("rimavicu", "rimavic", "rimavic"),
    ("rimavica", "rimavica", "rimavica"),  # no u
    ("lomnadrimavicou", "lomnadrimavico", "lomnadrimavico"),
    
    # Combinations
    ("farmu", "farm", "farm"),
    ("chalupu", "chalp", "chalp"),
    ("usadlost", "sadlost", "sadlost"),
    
    # Random attempts
    ("kubik", "kbik", "kbik"),
    ("fukar", "fkar", "fkar"),
    ("fuska", "fska", "fska"),
    ("tunak", "tnak", "tnak"),
    ("bukas", "bkas", "bkas"),
]

print("Testing credentials for /kamenista_dolina/...")
print("=" * 50)

for original, user, pwd in test_cases:
    try:
        r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=10, verify=False)
        if r.status_code == 200:
            print(f"\n*** SUCCESS! ***")
            print(f"Original: {original}")
            print(f"Username: {user}")
            print(f"Password: {pwd}")
            print(f"Response preview: {r.text[:200]}")
            break
        elif r.status_code == 401:
            pass  # Expected for wrong credentials
        else:
            print(f"{user}:{pwd} -> Status {r.status_code}")
    except Exception as e:
        print(f"Error with {user}:{pwd}: {e}")

print("\nDone testing basic combinations")
