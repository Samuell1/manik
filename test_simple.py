#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Simple two-word combinations that might be on a pub sign
# Word1 with 'u' : Word2 with 'u'
test_cases = [
    # BUFET + name
    ("bufet kubik", "bfet", "kbik"),
    ("bufet julius", "bfet", "jlis"),
    ("bufet dusan", "bfet", "dsan"),
    ("bufet lukac", "bfet", "lkac"),
    
    # U + surname (At [person's])
    ("u kubika", "", "kbika"),  # Skip empty
    ("ukubika", "kbika", "kbika"),
    ("ulukaca", "lkaca", "lkaca"),
    ("udusana", "dsana", "dsana"),
    ("ujuliana", "jliana", "jliana"),
    
    # [Name] PUB/BUFET style
    ("julius bufet", "jlis", "bfet"),
    ("dusan bufet", "dsan", "bfet"),
    ("kubik bufet", "kbik", "bfet"),
    
    # Surname + Surname
    ("kubik dusan", "kbik", "dsan"),
    ("dusan kubik", "dsan", "kbik"),
    ("julius rudolf", "jlis", "rdolf"),
    ("rudolf julius", "rdolf", "jlis"),
    ("lukas juraj", "lkas", "jraj"),
    ("juraj lukas", "jraj", "lkas"),
    
    # POHOSTINSTVO related
    ("pohostinstvo ukubika", "pohostinstvo", "kbika"),
    
    # Simple words
    ("kurina husta", "krina", "hsta"),
    ("husta kurina", "hsta", "krina"),
    ("tukova muka", "tkova", "mka"),
    ("muka tukova", "mka", "tkova"),
    
    # Location-based
    ("lom rimavicu", "lom", "rimavic"),
    ("rimavicu lom", "rimavic", "lom"),
    ("lomu rimavica", "lom", "rimavica"),
    
    # URPINER beer (from ad seen on Street View)
    ("urpiner pub", "rpiner", "pb"),
    ("pub urpiner", "pb", "rpiner"),
    ("urpiner bufet", "rpiner", "bfet"),
    ("bufet urpiner", "bfet", "rpiner"),
    
    # Common Slovak words
    ("cukrar huby", "ckrar", "hby"),
    ("huby cukrar", "hby", "ckrar"),
    ("klubova huta", "klbova", "hta"),
    ("huta klubova", "hta", "klbova"),
    
    # "Pri" (At/By) patterns  
    ("pri pukli", "pri", "pkli"),
    ("pri dubku", "pri", "dbk"),
    ("pri studni", "pri", "stdni"),
    
    # Forgács family related (founders)
    ("forgacsovu", "forgacsov", "forgacsov"),
    ("uforgacsov", "forgacsov", "forgacsov"),
]

# Filter out empty usernames
test_cases = [(o, u, p) for o, u, p in test_cases if u]

print(f"Testing {len(test_cases)} simple combinations...")

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
