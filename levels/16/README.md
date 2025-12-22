# Level 16 (Opilec)

**URL:** https://manik.sk/hra/opilec/

## Prihlasovacie údaje
- **Username:** abc123
- **Password:** 123abc

**Odkiaľ:** Level 15 - RGB hex kódy zo žltého a modrého štvorca
- Žltý štvorec RGB(171,193,35) = #ABC123 = abc123
- Modrý štvorec RGB(18,58,188) = #123ABC = 123abc

## Popis
"Opitý Štefan ti toho veľa povedať nevedel .."

## HTML komentáre
- `<!-- encipher -->` - hint na šifrovanie
- `<!-- dolezita zastavka je v Lome nad Rimavicou -->` - dôležitá zastávka

## Hinty
1. stiahni 'ŠPZ' (download license plate)
2. kľúč je názov podniku, ktorý ho vyrobil (key is the company name that made it)

## Clickable areas
- **../kamenista_dolina/** (coords: 733, 538, 785, 589) - vyžaduje auth

## Obrazok
- **obrazok.jpg** - muž v kockovanej košeli ("opitý Štefan") pri drevenej budove

## Analýza

### Lom nad Rimavicou
- Z vylet/den3: najvyššie položená slovenská obec (1015m)
- Film "Zemianska česť" (1957) sa tu nakrúcal

### ŠPZ (evidenčné číslo vozidla)
- Hľadám súbor "ŠPZ" na stiahnutie
- "kľúč" = heslo pre dešifrovanie (encipher hint)
- "podnik ktorý ho vyrobil" = výrobca ŠPZ/auta?

## Testované súbory (404)
- spz, SPZ, ŠPZ (rôzne varianty, URL encoded)
- ecv, ECV, plate, cislo, tanier
- skoda, skoda120, aznp, auto, car
- cipher, encipher, encrypted, data
- lom, rimavica, zastavka
- Rôzne prípony: .txt, .rar, .zip, .jpg, .enc, .dat

## Analýza vylet/den3
- Škoda 120 zmienená v príbehu
- Vodič zo Sardínie ich zviezol
- Obrázky den3 stiahnuté - zatiaľ žiadne auto/ŠPZ

## Google Street View analýza (od používateľa)
- **Číslo zastávky:** 060146
- **PSČ:** 976 53 Sihla
- **Autobusový dopravca:** SAD Zvolen (Slovenská autobusová doprava)
- Zastávka "Lom nad Rimavicou, obec"

## Čo hľadať na Street View
1. Viditeľná ŠPZ na akomkoľvek vozidle
2. Názov výrobcu autobusu (IVECO, SOR, Karosa, Setra)
3. Nápisy a čísla v okolí zastávky
4. Staré autá (Škoda 120 z príbehu)

## NÁJDENÝ SÚBOR: ZV414BC

**ŠPZ autobusu nájdená na Google Street View:** ZV 414BC

**Súbor:** `ZV414BC` - obsahuje zašifrovaný text (encipher.it formát)

**Obsah:**
```
EnCt29461dc1f9e7e9e5e1d20996c137e37288f0ee0fc9461dc1f9e7e9e5e1d20996cbwfLn5phXAO...
```

**Formát:**
- `EnCt` - prefix (Encipher Text)
- 64 hex znakov - salt/IV
- Base64 dáta - zašifrovaný obsah
- `IwEmS` - suffix

## Dešifrovanie

**Formát:** encipher.it (AES encryption)
- ENCT format: EnCt + 64 hex (salt/IV) + Base64 ciphertext + IwEmS
- Pravdepodobne 16-znakový kľúč
- AES-CBC alebo AES-CCM s PBKDF2 key derivation

**Problém:** Potrebujeme správne heslo (názov podniku/výrobcu)

**Testované heslá (500+, všetky neúspešné):**

### Výrobcovia autobusov:
- karosa, KAROSA, Karosa, karosavysokemyto, vysokemyto
- sor, SOR, sorlibchavy, libchavy
- iveco, IVECO, ivecobus, irisbus, IRISBUS
- ikarus, IKARUS, man, MAN, mercedes, MERCEDES
- setra, SETRA, neoplan, NEOPLAN, solaris, SOLARIS

### Výrobca EČV (Turčan Delta):
- turcandelta, TURCANDELTA, turcan delta, TURCAN DELTA
- turcandeltasro, kostanynadturcom
- spm, spmsecurity (nový výrobca od 2022)

### Dopravcovia:
- sadzvolen, SAD Zvolen, sadlucenec, SAD Lucenec
- sad, SAD (www.sadlc.sk - z cestovného poriadku)

### Škoda Auto (z vylet/den3 príbehu):
- skoda, SKODA, skoda120, skodaauto
- aznp, AZNP, mladaboleslav

### Miesta:
- zvolen, lom, rimavica, sihla, brezno
- lomnadrimavicou, vysoke myto

### Ostatné:
- opilec, stefan, manik, hra
- autobus, bus, spz, ecv

**Metódy šifrovania skúšané:**
- AES-128-CBC, AES-256-CBC
- AES-CCM (SJCL štýl)
- PBKDF2 s 1, 1000, 10000 iteráciami
- Priamy kľúč (16 bytes) aj key derivation
- Rôzne kombinácie salt/IV z hex časti

## Dopravca z obrázku vylet/den3/029.jpg
- **SAD Lučenec a.s.** (www.sadlc.sk)
- Zastávka Utekáč, Drahová
- Cieľové stanice: Lom nad Rimavicou, Utekáč (Dlhá Lúka, Havrilovo)

## Google Street View - autobus (NÁJDENÉ!)
- **ŠPZ:** ZV 414BC (okres Zvolen)
- **Dopravca:** Slovenská autobusová doprava Zvolen, a.s. (www.sadzv.sk)
- **Model:** CROSSWAY (nápis viditeľný na autobuse)
- **Výrobca:** IVECO (IVECO Crossway)
- **Logo:** SAD - modrý a červený kruh

## Ďalší level
- **URL:** https://manik.sk/hra/kamenista_dolina/
- **Status:** 401 (credentials neznáme)

## Rozšírené testovanie hesiel (1000+)

### Algoritmy encipher.it (testované)
- PBKDF2-SHA1 s 1000 iteráciami
- AES-ECB pre generovanie kľúča
- AES-CTR pre dešifrovanie
- Rôzne kombinácie salt (8/16 bytes) a nonce (8 bytes)

### ROT13 variácie (všetky neúspešné)
- CROSSWAY → PEBFFJNL
- IVECO → VIRPB
- IRISBUS → VEVFOHF
- SAD → FNQ

### Ďalšie testované kategórie
- Výrobcovia autobusov: IVECO, Irisbus, Karosa, SOR, MAN, Mercedes, Setra, Neoplan
- Dopravcovia: SAD Zvolen, SAD Lučenec, Arriva
- Výrobcovia ŠPZ: Turčan Delta, SPM Security
- Lokality: Zvolen, Lom, Rimavica, Sihla, Vysoké Mýto
- Rodná spoločnosť: CNH Industrial, FIAT
- Brute force: všetky 3-4 písmenkové kombinácie (450,000+)

### Algoritmy (testované)
- encipher.it (PBKDF2-SHA1 + AES-CTR)
- OpenSSL EVP_BytesToKey
- Priamy MD5/SHA256 hash ako kľúč
- AES-CBC, AES-CFB, AES-OFB módy

## Status
**IN PROGRESS** - Zašifrovaný súbor nájdený, heslo zatiaľ neznáme

### Čo vieme:
1. Súbor ZV414BC obsahuje encipher.it šifrovaný text
2. Autobus na Google Street View je IVECO Crossway
3. Dopravca je SAD Zvolen (www.sadzv.sk)
4. Hint: "kľúč je názov podniku, ktorý ho vyrobil"

### Možné interpretácie "podnik ktorý ho vyrobil":
1. **Výrobca autobusu** - IVECO, Irisbus (všetky testované)
2. **Výrobca ŠPZ** - Turčan Delta, SPM Security (testované)
3. **Dopravca** - SAD Zvolen (testované)
4. **Niečo iné** - názov podniku/hostinca? lokálna firma?

### Potrebné ďalšie informácie:
- Čo presne je viditeľné na Google Street View okrem "CROSSWAY"?
- Je tam nejaký iný nápis na autobuse alebo v okolí?
- Existuje nejaký lokálny podnik/hostinec v Lome nad Rimavicou?
