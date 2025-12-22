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
**IN PROGRESS** - Zašifrovaný súbor nájdený, heslo zatiaľ neznáme (1000+ hesiel testovaných)

### Čo vieme:
1. Súbor ZV414BC obsahuje encipher.it šifrovaný text
2. Autobus na Google Street View je IVECO Crossway
3. Dopravca je SAD Zvolen (www.sadzv.sk)
4. Hint: "kľúč je názov podniku, ktorý ho vyrobil"

### Rozšírené testovanie hesiel (December 2025):

**Testované kategórie (všetky neúspešné):**

1. **Výrobcovia autobusov:**
   - IVECO, Irisbus, Karosa, SOR, MAN, Mercedes, Setra, Neoplan
   - Kombinácie: ivecocrossway, ivecoczech, irisbusiveco
   - Vysoké Mýto (továreň), Sodomka (zakladateľ)

2. **Výrobcovia ŠPZ:**
   - Turčan Delta, SPM Security, turcandeltasro

3. **Dopravcovia:**
   - SAD Zvolen, SAD Lučenec, sadzvolen, sadzv, autobusovadoprava

4. **Lokality:**
   - Lom nad Rimavicou, Zvolen, Sihla, Kokava nad Rimavicou
   - lomnadrimavicou, 1015 (nadmorská výška), 060146 (číslo zastávky)

5. **Historické spoločnosti:**
   - Karosa, AZNP, Sodomka, Forgáč

6. **Podniky v okolí:**
   - krčma u Havlíčkov (z filmu Zemianska česť)
   - Koliba Studienka, Penzión Vrchár, Chata Molik
   - Drevenice Drevené kráľovstvo

7. **Všeobecné:**
   - podnik, firma, vyrobca, autobus, kluc, heslo
   - Všetky 3-4 písmenkové kombinácie (450,000+)
   - Čísla 0-10000

### Možné interpretácie "podnik ktorý ho vyrobil":
1. **Výrobca autobusu** - IVECO, Irisbus (všetky testované)
2. **Výrobca ŠPZ** - Turčan Delta, SPM Security (testované)
3. **Dopravca** - SAD Zvolen (testované)
4. **Krčma kde sa opil Štefan** - u Havlíčkov? (testované)
5. **Niečo viditeľné na Google Street View** - ???

### Potrebné ďalšie informácie:
- Čo presne je viditeľné na Google Street View okrem "CROSSWAY"?
- Je tam nejaký iný nápis na autobuse alebo v okolí zastávky?
- Je na autobuse nejaké firemné logo alebo znak okrem SAD?
- Existuje nejaká tabuľka alebo cedula na zastávke?

## Session December 2025 - Rozšírené testovanie

### Nové testované kategórie:
1. **Karosa** (pôvodný výrobca pred IVECO):
   - karosa, KAROSA, karosavysokemyto, karosa as
   - Sodomka (zakladateľ), Josef Sodomka
   - Vysoké Mýto (lokalita továrne)

2. **SAD Zvolen detaily:**
   - sad, SAD, sadzvolen, SADZVOLEN, sadzv
   - slovenskaautobusovadoprava, autobusovadoprava

3. **Forgácsfalva** (maďarský názov Lomu nad Rimavicou):
   - forgacsfalva, forgacs, Forgacs

4. **Lokálne podniky pri Kokave nad Rimavicou:**
   - Kokavská Izba, Pizzéria Favore, Koliba Studienka
   - Reštaurácia KA-MO, Hostinec v Horách

5. **Slovaské slová s diakritikou:**
   - ŠPZ, Štefan, kľúč, krčma, zastávka

6. **Algoritmy testované:**
   - encipher.it (PBKDF2-SHA1 + AES-CTR)
   - SJCL s CCM, GCM, OCB2 módmi
   - Rôzne kombinácie salt/IV

### Celkom testované:
- 500,000+ hesiel (všetky 3-4 písmenkové kombinácie)
- 10,000 čísel
- 2,000+ špecifických slov a variácií
- Algoritmy: Python PyCryptodome + Node.js SJCL

### Záver:
Heslo nebolo nájdené. Potrebné dodatočné informácie z Google Street View
alebo iný pohľad na hint "podnik ktorý ho vyrobil".
