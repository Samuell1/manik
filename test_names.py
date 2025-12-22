#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Slovak names with 'u' - common combinations
# If sign says "FIRSTNAME LASTNAME", remove 'u' from both
names_with_u = [
    "dusan", "rudolf", "julius", "lukas", "kubo", "kubik", "kuban",
    "juraj", "juro", "ludovit", "ludvik", "ludka", "august",
    "ursulo", "ursula", "zuzana", "zuza", "gustaf", "gustav",
    "ruzena", "ruzicka", "kunova", "kunovska", "kubova", "bukova",
    "burgr", "burda", "burian", "bugaj", "bugar", "bugos",
    "sucharda", "suchacek", "sudor", "sulak", "sulek", "suma",
    "jurica", "juricek", "kukucka", "kukula", "kukulova",
    "mudrak", "mucska", "muhova", "mukova", "mula", "muller",
    "pukan", "pukanic", "pukos", "puha", "pukalovic",
    "rubin", "rubint", "rudnak", "rudas", "rusnok", "rusnak",
    "tucek", "tucny", "turek", "turcan", "turkova", "turkovic",
    "vugrinec", "vukovic", "vukmanic", "vukomanovic"
]

# Remove 'u' from each
test_cases = []
for name in names_with_u:
    cleaned = name.replace('u', '')
    if cleaned:  # not empty
        test_cases.append((name, cleaned, cleaned))

# Also try common firstname:lastname pairs
pairs = [
    ("dusan kuban", "dsan", "kban"),
    ("julius rudolf", "jlis", "rdolf"),
    ("lukas juraj", "lkas", "jraj"),
    ("kubik dusan", "kbik", "dsan"),
    ("rudolf burian", "rdolf", "brian"),
    ("zuzana ruzena", "zzana", "rzena"),
    ("gustav august", "gstaf", "agst"),
    ("juro kubik", "jro", "kbik"),
    ("ludovit muller", "ldovit", "mller"),
    ("ursula kunova", "rsla", "knova"),
]
test_cases.extend(pairs)

# Also try reversed (lastname:firstname)
for orig, first, last in pairs[:]:
    test_cases.append((orig + " rev", last, first))

print(f"Testing {len(test_cases)} name combinations...")

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
