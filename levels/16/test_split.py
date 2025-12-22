#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

url = "https://manik.sk/hra/kamenista_dolina/"

# Try splitting words - first part username, second part password
# Original phrase with 'u', then split after removing 'u'
test_cases = [
    # "POZOR CUDZÍ" (Beware strangers)
    ("pozorcudzi", "pozor", "cdzi"),
    ("pozorcudzi", "pozor", "cudzi"),  # only remove u from second
    
    # "SÚKROMNÝ POZEMOK" (Private land) - various splits
    ("sukromnypozemok", "skromny", "pozemok"),
    ("sukromnypozemok", "skromne", "pozemok"),
    
    # "DOM KUBÍKA" (Kubík's house)
    ("domkubika", "dom", "kbika"),
    ("domkubana", "dom", "kbana"),
    
    # "U HAJDUKA" (At Hajdúk's) - very Slovak
    ("uhajduka", "hajdka", "hajdka"),
    ("uhajduk", "hajdk", "hajdk"),
    
    # "CUKRÁREŇ" (confectionery)
    ("cukraren", "ckraren", "ckraren"),
    
    # "FUTBALOVÉ IHRISKO" (football field)
    ("futbaloveihrisko", "ftbalove", "ihrisko"),
    
    # "OBECNÝ ÚRAD" itself? (Municipal office)
    ("obecnyurad", "obecny", "rad"),
    ("obecnyurad", "obecnyrad", "obecnyrad"),
    
    # "POŽIARNA ZBROJNICA" (fire station)
    ("poziarnazbrojnica", "poziarna", "zbrojnica"),
    
    # "KULTÚRNY DOM" (cultural house)
    ("kulturnydom", "kltrny", "dom"),
    ("kulturnydom", "kltrnydom", "kltrnydom"),
    
    # "JEDNOTNÉ ROĽNÍCKE DRUŽSTVO" (old collective farm)
    ("jrd", "jrd", "jrd"),
    ("druzstvo", "drzstvo", "drzstvo"),
    
    # "HOSTINEC U HÁJNIKA" (Inn at forester's)
    ("hostinecuhajnika", "hostinec", "hajnika"),
    
    # "ČERPADLO" / "PUMPA" (pump - common at water wells)
    ("pumpa", "pmpa", "pmpa"),
    ("cerpadlo", "cerpadlo", "cerpadlo"),  # no u
    
    # "STUDŇA" / "STUDNICA" (well)
    ("studna", "stdna", "stdna"),
    ("studnica", "stdnica", "stdnica"),
    
    # "MLYNÁRKA" (miller's) - old mill?
    ("mlynarka", "mlynarka", "mlynarka"),  # no u
    
    # "VODÁRNA" / "VODOVOD" (water supply)
    ("vodarna", "vodarna", "vodarna"),  # no u
    
    # "OVČIARŇA" / "KUZŇA" (sheepfold/forge)
    ("ovcarna", "ovcarna", "ovcarna"),
    ("kuzna", "kzna", "kzna"),
    
    # "TOKÁR" style surnames
    ("tokar", "tokar", "tokar"),
    
    # "ĎURKOV DVOR" (Ďurko's courtyard)
    ("durkovdvor", "drkov", "dvor"),
    ("durkovdom", "drkov", "dom"),
    
    # Simple two words with u
    ("dudukuran", "ddk", "ran"),
    ("kukurica", "kkrica", "kkrica"),  # corn
    
    # "MÚZEUM" (museum)
    ("muzeum", "mzem", "mzem"),
    
    # "ÚTULOK" / "ÚTUĽŇA" (shelter)
    ("utulok", "tlok", "tlok"),
    ("utulna", "tlna", "tlna"),
    
    # Names of settlements mentioned
    ("drabsko", "drabsko", "drabsko"),  # Drábsko - nearby village
    ("sihla", "sihla", "sihla"),  # Sihla - nearby village
    ("polianka", "polianka", "polianka"),  # Polianka
    ("javorina", "javorina", "javorina"),  # Javorina
    
    # With 'u' variants
    ("chlipniacku", "chlipniack", "chlipniack"),  # Chlipniačky area
    
    # "OBECNÝ DOM" (municipal house)
    ("obecnydom", "obecny", "dom"),
    ("obecnydom", "obecnydom", "obecnydom"),  # no u
    
    # Try exact names from search
    ("limbora", "limbora", "limbora"),  # Chata Limbora
    ("kovacica", "kovacica", "kovacica"),  # Chata Kovačica
    ("vrchar", "vrchar", "vrchar"),  # Penzion Vrchar
    
    # With u added/removed
    ("limboru", "limbor", "limbor"),
    ("kovacicu", "kovacic", "kovacic"),
    ("vrcharu", "vrchar", "vrchar"),
    
    # More common fence signs
    ("vstupzakazany", "vstp", "zakazany"),
    ("zakazvstup", "zakaz", "vstp"),
    ("vstup", "vstp", "vstp"),
    ("zakaz", "zakaz", "zakaz"),  # no u
    ("pozorpes", "pozor", "pes"),
    ("zlyupes", "zly", "pes"),  # with u
    ("zlypes", "zlyupes", "zlyupes"),
]

print(f"Testing {len(test_cases)} split combinations...")

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
