#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

base_url = "https://manik.sk/hra/opilec/"
auth = HTTPBasicAuth("abc123", "123abc")

# Try to find hidden files
files_to_check = [
    "hint.txt", "napoveda.txt", "napis.txt", "plot.txt",
    "urad.txt", "obecny.txt", "obecnyurad.txt",
    "kluc.txt", "heslo.txt", "password.txt",
    "sign.txt", "fence.txt", "text.txt",
    "lomnadrimavicou.txt", "lom.txt",
    "image.jpg", "napis.jpg", "plot.jpg",
    "foto.jpg", "photo.jpg", "picture.jpg",
    "obecnyurad.jpg", "urad.jpg",
    ".hidden", "secret.txt", "tajne.txt",
    "riešenie.txt", "riesenie.txt", "solution.txt",
    "pomoc.txt", "help.txt",
]

print("Checking for hidden files on /opilec/...")

for filename in files_to_check:
    try:
        url = base_url + filename
        r = requests.get(url, auth=auth, timeout=10, verify=False)
        if r.status_code == 200:
            print(f"\n*** FOUND: {filename} ***")
            print(f"Content preview: {r.text[:300]}")
        elif r.status_code != 404:
            print(f"{filename}: Status {r.status_code}")
    except Exception as e:
        print(f"Error with {filename}: {e}")

print("\nDone")
