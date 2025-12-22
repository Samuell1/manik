#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Two-word signs where both words contain 'u'
# First word becomes username, second becomes password after removing 'u'
words_with_u = [
    "bufet", "julius", "dusik", "dustin", "budik", "bubon", "bunka",
    "bulka", "burka", "busik", "busina", "butik", "buzar", "buzna",
    "cukar", "cupaj", "cupak", "cupat", "culik", "cupka", "curiak",
    "dudak", "dudok", "duhan", "dukat", "dulaj", "dupak", "durak",
    "fucik", "fukar", "fukat", "fuksa", "fulaj", "fumak", "funar",
    "guban", "gubac", "gulag", "gulak", "gular", "gulas", "gulat",
    "hubar", "hubat", "hucak", "hudak", "hukan", "hukat", "hulan",
    "juhas", "junak", "junka", "jurak", "jurat", "jurik", "juris",
    "kuban", "kubat", "kubik", "kudla", "kufar", "kufor", "kukal",
    "lucan", "lucka", "ludia", "ludka", "ludko", "lukas", "lukac",
    "mucha", "mucka", "mudak", "mudir", "mufak", "mukat", "mulat",
    "nukat", "nulas", "nulat", "numar", "numat", "nurak", "nurat",
    "pucan", "pucar", "pucat", "pucer", "pucka", "pudel", "puder",
    "ruban", "rubar", "rubat", "rubin", "rucaj", "rucka", "rudat",
    "sudar", "sudan", "sudca", "sudek", "sudom", "sudor", "sukat",
    "tuban", "tubar", "tucat", "tucer", "tucet", "tucik", "tucka",
    "vujan", "vujas", "vujat", "vujer", "vukaj", "vukar", "vukas",
    "zubar", "zubat", "zuber", "zubin", "zubka", "zubon", "zubor",
]

# Generate pairs
test_cases = []
for i, w1 in enumerate(words_with_u[:30]):  # Limit to first 30
    for w2 in words_with_u[:30]:
        if w1 != w2:
            u1 = w1.replace('u', '')
            u2 = w2.replace('u', '')
            if u1 and u2 and len(u1) >= 2 and len(u2) >= 2:
                test_cases.append((f"{w1} {w2}", u1, u2))

# Also try some specific common combinations
specific = [
    ("julius bufet", "jlis", "bfet"),
    ("dusan julius", "dsan", "jlis"),
    ("julius dusan", "jlis", "dsan"),
    ("bufet julius", "bfet", "jlis"),
    ("julius kubik", "jlis", "kbik"),
    ("kubik julius", "kbik", "jlis"),
    ("julius lukas", "jlis", "lkas"),
    ("lukas julius", "lkas", "jlis"),
    ("dusan kuban", "dsan", "kban"),
    ("kuban dusan", "kban", "dsan"),
    ("rudolf julius", "rdolf", "jlis"),
    ("julius rudolf", "jlis", "rdolf"),
    ("rudolf dusan", "rdolf", "dsan"),
    ("dusan rudolf", "dsan", "rdolf"),
    ("bufet dusan", "bfet", "dsan"),
    ("dusan bufet", "dsan", "bfet"),
]
test_cases.extend(specific)

print(f"Testing {len(test_cases)} two-word combinations...")

count = 0
for orig, user, pwd in test_cases:
    count += 1
    if count % 100 == 0:
        print(f"Progress: {count}/{len(test_cases)}")
    try:
        r = requests.get(url, auth=HTTPBasicAuth(user, pwd), timeout=5, verify=False)
        if r.status_code == 200:
            print(f"\n*** SUCCESS! ***")
            print(f"Original: {orig}")
            print(f"Username: {user}")
            print(f"Password: {pwd}")
            break
    except:
        pass

print(f"\nDone testing {count} combinations")
