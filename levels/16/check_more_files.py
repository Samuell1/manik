#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

base_url = "https://manik.sk/hra/opilec/"
auth = HTTPBasicAuth("abc123", "123abc")

# More specific file names
files_to_check = [
    # Based on the hint - fence, municipal office
    "oprotiuradu.txt", "oproti.txt", "naproti.txt",
    "plot.txt", "napis.txt", "napisy.txt",
    "obecnyurad.txt", "urad.txt", "obecny.txt",
    "fence.txt", "sign.txt", "opposite.txt",
    
    # Location specific
    "lom.txt", "rimavica.txt", "lomnadrimavicou.txt",
    "forgacs.txt", "forgacsfalva.txt",
    
    # With 'u' theme
    "bezU.txt", "bezu.txt", "odstranu.txt", "u.txt",
    "maloeu.txt", "maleu.txt", "odstranU.txt",
    
    # Common archive extensions
    "hint.zip", "hint.rar", "napis.zip", "kluc.zip",
    "data.txt", "info.txt", "readme.txt",
    
    # Photo variations
    "obecnyurad.jpg", "urad.jpg", "plot.jpg", "napis.jpg",
    "foto.jpg", "fotka.jpg", "obrazok2.jpg",
    "hint.jpg", "pomoc.jpg", "sign.jpg",
    
    # PNG variations
    "napis.png", "plot.png", "hint.png", "urad.png",
    
    # Subdirectories
    "hint/", "data/", "files/", "images/",
]

print("Checking for more hidden files on /opilec/...")

for filename in files_to_check:
    try:
        url = base_url + filename
        r = requests.get(url, auth=auth, timeout=10, verify=False)
        if r.status_code == 200:
            print(f"\n*** FOUND: {filename} ***")
            if '.jpg' in filename or '.png' in filename:
                print(f"Image file - {len(r.content)} bytes")
            else:
                print(f"Content: {r.text[:500]}")
        elif r.status_code == 403:
            print(f"FORBIDDEN: {filename}")
        elif r.status_code != 404:
            print(f"{filename}: Status {r.status_code}")
    except Exception as e:
        pass

print("\nDone")
