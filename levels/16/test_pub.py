#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Pub/restaurant related words
test_cases = [
    # "BUFET" variations
    ("bufet", "bfet", "bfet"),
    ("bufetuana", "bfet", "ana"),
    ("bufetujana", "bfet", "jana"),
    
    # "POHOSTINSTVO U ..." - from previous analysis
    ("pohostinstvouburku", "pohostinstvo", "brk"),
    ("uhajnika", "hajnika", "hajnika"),
    ("uzorana", "zorana", "zorana"),
    ("ubrata", "brata", "brata"),
    ("ustefana", "stefana", "stefana"),  # U Štefana (At Štefan's)
    ("uopilca", "opilca", "opilca"),  # At the drunkard's
    
    # With village/location names
    ("ulomcana", "lomcana", "lomcana"),
    ("urimavicana", "rimavicana", "rimavicana"),
    
    # Common pub names
    ("uhajduka", "hajdka", "hajdka"),
    ("uvysadnika", "vysadnika", "vysadnika"),  # At the settler's
    ("utokara", "tokara", "tokara"),  # At the turner's
    ("ukameniara", "kameniara", "kameniara"),  # At the stonemason's
    ("upustiara", "pstiara", "pstiara"),  # At the hermit's
    
    # "URPINER" related (beer from previous analysis)
    ("urpiner", "rpiner", "rpiner"),
    ("pivovarupri", "pivovar", "pri"),
    
    # Simple pub words
    ("krcmu", "krcm", "krcm"),
    ("vycapu", "vycap", "vycap"),
    ("pivo", "pivo", "pivo"),  # no u
    ("vinu", "vin", "vin"),
    
    # "ÚTULŇA" / "ÚTUĽOK" (shelter, also slang for cheap pub)
    ("utulna", "tlna", "tlna"),
    ("utulok", "tlok", "tlok"),
    
    # "HUMNO" (barn, sometimes used for pubs)
    ("humno", "hmno", "hmno"),
    
    # Slovak slang for pub
    ("pajzel", "pajzel", "pajzel"),  # no u
    ("krcm", "krcma", "krcma"),
    
    # "STANICA" (station) - bus stop related
    ("stanica", "stanica", "stanica"),  # no u
    ("autobusova", "atobsova", "atobsova"),
    ("zastavkua", "zastavka", "zastavka"),
    
    # Combined
    ("bufetstanica", "bfet", "stanica"),
    ("krcmaburian", "krcma", "brian"),
]

print(f"Testing {len(test_cases)} pub-related combinations...")

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
