#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# More targeted guesses based on the puzzle structure
test_cases = [
    # If the sign says house number + name with 'u'
    ("domu", "dom", "dom"),
    ("domu14", "dom14", "dom14"),
    ("domu12", "dom12", "dom12"),
    
    # Family name plaques - plural forms
    ("kubanovci", "kbanovci", "kbanovci"),
    ("dusanovci", "dsanovci", "dsanovci"),
    ("burianovci", "brianovci", "brianovci"),
    ("lukacovci", "lkacovci", "lkacovci"),
    ("rudolfovci", "rdolfovci", "rdolfovci"),
    
    # Family name plaques - singular possessive
    ("kubanov", "kbanov", "kbanov"),
    ("dusanov", "dsanov", "dsanov"),
    ("burianov", "brianov", "brianov"),
    
    # "DOM U ..." pattern
    ("domujakuba", "dom", "jakba"),
    ("domudusana", "dom", "dsana"),
    ("domuburku", "dom", "brk"),
    
    # General patterns with u in common positions
    ("usadlost", "sadlost", "sadlost"),
    ("ustatie", "statie", "statie"),
    ("usadenie", "sadenie", "sadenie"),
    
    # If the sign mentions "kamenista" (next level name)
    ("kamenistaudoli", "kamenista", "doli"),  # Kamenista dolina
    ("udolina", "dolina", "dolina"),
    ("udoli", "doli", "doli"),
    
    # Place names with u
    ("rimavicu", "rimavic", "rimavic"),
    ("lomu", "lom", "lom"),
    
    # If sign says "NAPROTI URADU" (opposite the office)
    ("naprotiuradu", "naproti", "rad"),
    ("oprotiuradu", "oproti", "rad"),
    
    # Building with 'u' - kultúrny dom, požiarna zbrojnica
    ("kulturnydomu", "kltrny", "dom"),
    ("poziarnej", "poziarnej", "poziarnej"),  # no u
    
    # Cooperative/JRD sign
    ("druzstvo", "drzstvo", "drzstvo"),
    ("druzstva", "drzstva", "drzstva"),
    ("jrd", "jrd", "jrd"),  # no u
    
    # Simple single syllable words
    ("kut", "kt", "kt"),
    ("sud", "sd", "sd"),
    ("muk", "mk", "mk"),
    ("buk", "bk", "bk"),
    ("dub", "db", "db"),
    ("pub", "pb", "pb"),
    ("tuk", "tk", "tk"),
    
    # If it's a two-word sign where both have 'u'
    ("dusankuban", "dsan", "kban"),
    ("rudolfburian", "rdolf", "brian"),
    ("lukacjuraj", "lkac", "jraj"),
    ("jurajlukac", "jraj", "lkac"),
    
    # Random possibilities
    ("student", "stdent", "stdent"),
    ("studen", "stden", "stden"),
    ("studenka", "stdenka", "stdenka"),
    ("studnicka", "stdnicka", "stdnicka"),
    
    # Pub/restaurant
    ("kruhu", "krh", "krh"),  # "Pri kruhu" (at the circle)
    ("dubku", "dbk", "dbk"),  # "Pri dubku" (at the little oak)
    ("buuk", "bk", "bk"),
    
    # Blacksmith mentioned in heritage
    ("kuzna", "kzna", "kzna"),
    ("kuznaa", "kzna", "kzna"),
    ("vyhna", "vyhna", "vyhna"),  # no u
    
    # Maybe it's just the word "úrad" backwards or something
    ("darum", "darm", "darm"),
    ("urrad", "rrad", "rrad"),
]

print(f"Testing {len(test_cases)} final combinations...")

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
