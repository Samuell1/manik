# Level 18 (Na vyhliadke)

**URL:** https://manik.sk/hra/na_vyhliadke/

## Prihlasovacie údaje
- **Username:** prekrasne
- **Password:** vyhlady

**Odkiaľ:** Level 17 - súbor /prezident dešifrovaný s YouTube video ID

## Popis
"Nachádzaš sa pod vyhliadkou a chceš sa dostať hore, ale potrebuješ sa popasovať s číslami .."

## Hinty
1. traja páni ti pomôžu nájsť kalkulačku
2. nie je všetko také, ako sa na prvý pohľad zdá
3. kalkulačka má rada 8 miestne čísla
4. výsledok z kalkulačky určuje deň a počet posledných číslic z dlhého čísla, ktoré treba zrátať
5. vyhľadaj potrebnú nápovedu a odomkni ju výsledkom z kalkulačky
6. použi výsledok zrátaných číslic
7. súčet správnych číslic slovom preveď do hexadecimálneho tvaru
8. nájdi súbor, ktorý ťa pomaly pustí ďalej

## Analýza obrázka

### Horná časť:
- **8-miestne číslo:** 43657381
- **Traja páni:** Gustáv Ivan František = **GIF** (hint na kalkulacka.gif)
- **Dlhé číslo:** 545746432486465452312314784565371453014 (39 číslic - OPRAVENÉ!)

### Dolná časť - šifra:
```
SKLO  PRST  DÁŠA  MIRO  PUTO  RISK  DLHÁ  DOBA
1243  4321  2341  4321  3214  2143  1432  3412
```

## Nájdené súbory
- **obrazok.jpg** - hlavný obrázok s číslami a šifrou
- **kalkulacka.gif** - Windows kalkulačka (nájdené cez GIF = Gustáv Ivan František)
- **napoveda** - RAR archív, **HESLO: 9** ✓

## napoveda.rar - ROZŠIFROVANÉ ✓

**Heslo:** `9`

**Obsah:**
```
--------------------------------------------
HRA by MNK | Slovenska online psychodventura
--------------------------------------------

          Napoveda je nasledovna

       CYKLOTURA NAPRIEC SLOVENSKOM

--------------------------------------------
```

## Analýza čísla 43657381

### sqrt(43657381) = 6607.373...
- Možno deň = 6, počet = 6 alebo 7
- Suma posledných 6 číslic dlhého čísla: 14
- Suma posledných 7 číslic: 21

### Upside-down na kalkulačke
- 43657381 otočené = IBELSgEh

### Ďalšie výpočty
- Suma číslic 43657381: 37
- Heslo "9" naznačuje: počet = 9
- Suma posledných 9 číslic (537145301): **29**
- 29 v hex = **1D**
- 29 po slovensky = "dvadsatdevat"

## CYKLOTURA NAPRIEC SLOVENSKOM

- Známa cyklistická akcia cez Slovensko
- Oficiálna stránka: http://manik.sk/slovensko/ (vracia 403)
- Súvisí s /vylet/ - existujú den1-den6
- Možno treba hľadať súbor súvisiaci s cykloturou

## Šifra - dekódovanie

Čísla pod slovami sú permutácie 1234, určujú poradie písmen:
- SKLO (1243) → SKOL
- PRST (4321) → TSRP
- DÁŠA (2341) → ÁSAD (ASAD)
- MIRO (4321) → ORIM
- PUTO (3214) → TUPO
- RISK (2143) → IRKS
- DLHÁ (1432) → DÁHL
- DOBA (3412) → BADO

## Postup riešenia

1. ✓ Kalkulačka s 8-miestnym číslom 43657381
2. ✓ Nájsť kalkulacka.gif (GIF = Gustáv Ivan František)
3. ✓ Odomknúť napoveda.rar heslom "9"
4. ✓ Získať hint: CYKLOTURA NAPRIEC SLOVENSKOM
5. ⏳ Suma správnych číslic slovom previesť do hex
6. ⏳ Nájsť súbor ktorý "pomaly pustí ďalej"
7. ⏳ Získať credentials pre ďalší level

## Testované súbory (404) - Rozsiahle hľadanie

### Základné kombinácie
- cyklotura, pomaly, slow, pomalicky, slowly
- Hex súčtov: 1d, 15, e, 27, 25, 2be, 7a, 9d, 23
- Slovenské čísla: dvadsatdevat, devat, strnast, dvadsatjeden, trinast, tridsatpat
- /vylet/den7-den20 neexistujú

### Hex kódovania slov
- dvadsatdevat → 647661647361746465766174
- trinast → 7472696e617374
- devat → 6465766174
- stodvadsatdva → 73746f64766164736174647661

### Šifra dekódovaná
- SKOL, TSRP, ASAD, ORIM, TUPO (Slovak!), IRKS, DAHL, BADO
- PUTO → TUPO je jediná dvojica kde oba výrazy sú zmysluplné slovenské slová

### Miesta z cykloturistiky deň 9
- krpacovo, zajezova, polomy, slatinskelazy, kalinka, detva, stožok, klokoc
- Všetky miesta z trasy testované

### Pomaly súvisiace slová
- lenivec, slimak, korytnacka, snek (pomalé zvieratá)
- volky, pomalky, volky-pomalky (idiom)
- zvolna, postupne, opatrne, zdlhavo
- zavora, lanovka, sedacka, vytah, stupanie

### MNK kalkulačka hodnoty
- Riadky: 2240, 6700, 8200/8205/8209, 0031
- Stĺpce: 2680, 2720, 4003, 0001
- Suma viditeľných: 35

### Výpočty
- Dlhé číslo suma: 157 (hex 9D)
- Suma bez 5-ok: 122 (hex 7A = 'z')
- Suma len 5-ok: 35 (= MNK suma!)
- Posledných 9 číslic suma: 29 (hex 1D)
- Posledných 5 číslic suma: 13 (hex D)

## Ďalší level
- **URL:** https://manik.sk/hra/??? (clickable area v obrazku)
- **Status:** Hľadám "súbor ktorý pomaly pustí ďalej"

## Nové objavy

### kalkulacka.gif má 2 frame-y!
- **Frame 0**: Štandardný Windows Calculator s "0."
- **Frame 1**: "Kalkulačka by MNK" s vlastným rozložením:
  ```
  M: 2  2  4  0
  N: 6  7  0  0
  K: 8  2  0  ?
     0  0  3  1
  ```
- Suma viditeľných číslic: 35 (hex: 23)
- MNK = meno autora hry

### /slovensko/ prístupné s auth!
- URL: https://manik.sk/slovensko/
- Obsahuje 13 dní cykloturistiky (den01-den13)
- Deň 9 (den09/): trasa 108km, končí v Zaježovej

## Kľúčový objav

**Suma číslic MNK kalkulačky (35) = Suma všetkých 5-ok v dlhom čísle (7×5=35)**

Toto naznačuje, že MNK kalkulačka "filtruje" číslicu 5.
- "Správne" číslice = tie čo zostanú po odstránení 5-ok
- Suma "správnych" číslic = 157 - 35 = **122**
- 122 v hex = **7A** (ASCII = 'z')
- 122 po slovensky = "stodvadsatdva"

## Teórie na vyriešenie

1. **Hexadecimálny súbor**: Názov súboru je hex kód sumy (napr. 7a, 1d)
2. **Slovenské číslo ako súbor**: Slovenský názov čísla (dvadsatdevat, stodvadsatdva)
3. **Pomaličky ako kľúčové slovo**: Súbor súvisí s niečím pomalým
4. **Deň 9 z cykloturistiky**: Niečo špecifické z trasy

## Dodatočné testovanie (Session 24/12)

### Level 10 štýl hex konverzia
- "dvadsatdevat" → hex 647661647361746465766174 (24 digits)
- First 6 + Last 6: 647661 + 766174 = **1413835** → 404
- "devetnast" → hex obsahuje 'e', sum = 1263950 → 404

### Cipher slová s all-digit hex:
- PRST → 50525354 (all digits) → 404
- DASA → 44415341 (all digits) → 404
- TSRP → 54535250 (all digits) → 404
- ASAD → 41534144 (all digits) → 404

### Day 9 cycling tour analýza:
- Trasa: Krpáčovo → Zaježová/Polomy (108km)
- "Pohodička na Zaježke" = relaxed pace = SLOWLY!
- Podpolianske folklórne slávnosti v Detve
- slavnosti.jpg v den09/
- Citát obsahuje "prekrásna" a "výhľadov" = Level 18 credentials!

### Testované kategórie (500+ kombinácií, všetky 404):
- Slovenské synonymá "pomaly": zvolna, postupne, nenahlivo, vahavo, vlecuco, lenivo
- Idiomy: pomaly_dalej_zajdes, isto, pomaly_ale_isto
- Súbory s príponami: .gif, .ne, .rar, .zip, .txt, .jpg
- Day 9 miesta: zaježova, polomy, detva, kalinka, slatinskelazy
- Hex hodnoty: 1d, 7a, 23, 25, 13
- Slovenské čísla: dvadsatdevat, stodvadsatdva, trinast, desat, tridsatpat
- MNK grid hodnoty: 2240, 6700, 8200, 0031
- Cipher dekódované: tupo, skol, tsrp, asad, orim, bado
- 8-digit number: 43657381 s rôznymi príponami
- Long number časti: prvých 14, posledných 14

### Kľúčové poznatky z Day 9:
- Citát: "Slovensko naše, prekrásna krajina, výhľadov plná kraj..."
  - "prekrásna" = username Level 18
  - "výhľadov" = password Level 18
  - Toto potvrdzuje spojenie s Day 9!
- GIF frame duration: 10000ms = 10 seconds = "slow" animation

## Dodatočné testovanie (Session 24/12 - pokračovanie)

### "Správne číslice" interpretácie:
1. **Posledných 9 číslic**: sum = 29 → "dvadsatdevat" → 404
2. **Bez 5-ok**: sum = 122 → "stodvadsatdva" → 404
3. **MNK suma**: 35 → "tridsatpat" → 404
4. **Permutácie - správne pozície**: 1,2,2,4,1,3 → sum = 13 → 404
5. **Počet správnych pozícií**: 6 → "sest" → 404

### Matematické operácie s 43657381:
- Digit sum: 37
- Reversed: 18375634
- Hex: 0x29a28a5
- Sqrt: 6607.37
- mod 35: 26
- // 35: 1247353

### Level 10 štýl sumy:
- "dvadsatdevat" hex → first6 + last6 = 1413835 → 404
- "trinast" hex → first6 + last6 = 1364643 → 404
- "devetnast" hex → sum = 1263950 → 404

### Ďalšie testované kategórie:
- Day 9 citát slová: krajina, plna, kraj, horach, nadhery, tronia, udoliach, sumi, lubezny, haj
- Číslo 9 variácie: deviatka, deviaty, 9_den, cislo9
- "Pustí" variácie: pusti_dalej, pustenie, uvolni, volno
- GIF duration: 10000, 10sec, 10sekund
- Calculator display: 0.29, nula, bodka

## Session 24/12 - Frame Connection Analysis

### KĽÚČOVÝ OBJAV: K row má poslednú číslicu 5!
- K row v MNK kalkulačke: **8 2 0 5** (nie 8 2 0 ?)
- Opravená MNK suma: **40** (nie 35)
- Frame 1 detailne ukazuje: M=2240, N=6700, K=8205, Bottom=0031

### Digit mapping medzi Frame 0 (Standard) a Frame 1 (MNK)
Standard → MNK:
```
7→2, 8→2, 9→4
4→6, 5→7, 6→0
1→8, 2→2, 3→0
0→0
```

**Unchanged digits**: Len 2 a 0 ostávajú rovnaké!
- Zaujímavé: 8-digit číslo 43657381 NEobsahuje 0, 2, ani 9

### Digit mapping aplikovaný na 43657381
- 43657381 → **60072028**
- Suma mapped digits: **25**

### Difference calculations (Standard - MNK)
- Sum of differences: **14**
- Sum of absolute differences: **36**
- Sum of XORs: **50**

### Cipher "správne pozície" analýza
Permutácie: 1243, 4321, 2341, 4321, 3214, 2143, 1432, 3412
- Počet pozícií kde digit = pozícia: **6** (2+0+0+0+2+0+2+0)
- Suma číslic na správnych pozíciach: **13** (1+2+2+4+1+3)

### Level 10 štýl výpočty (word → hex → first6+last6)
| Slovo | Hex výsledok |
|-------|-------------|
| dvadsatdevat (29) | 1413835 |
| styridsat (40) | 1473653 |
| tridsatpat (35) | 1453443 |
| dvadsatpat (25) | 1353835 |
| strnast (14) | 1354846 |
| tridsatsest (36) | 1404643 |
| patdesiat (50) | 1402348 |
| sest (6) | 1393947 |
| trinast (13) | 1364643 |

### Testované súbory (všetky 404)
- Mapped values: 60072028, 25, dvadsatpat
- MNK readings: 2240, 6700, 8205, 0031, 2240670082050031
- Differences: 14, 36, 50
- Diagonals: 2701, 0020
- Grid sums: 17176, 9454
- MNK letters: 131411, 778775, 4D4E4B
- Cipher decoded: skol, tsrp, asad, orim, tupo, irks, dahl, bado
- Slow animals: korytnacka, zelva, slimak, lenivec
- Calculator ops: sqrt, odmocnina, vypocet, sucet
- Number operations: 6607, 4850820, 18375634

### MNK Letter Analysis
- M=13, N=14, K=11 (letter positions)
- Sum = 38 = počet číslic v dlhom čísle!

### Unchanged digits in long number
- 2 appears 3× at positions 8, 17, 20
- 0 appears 1× at position 36
- Sum of "unchanged" digits = 6

## Session 24/12/2025 - Pokračovanie analýzy

### Overené fakty:
1. **Dlhé číslo má 39 číslic** končiacich na 3014 (nie 38/301)
2. **Suma posledných 9 číslic = 28** ("dvadsatosem" - obsahuje 'o','m' v hex → NEPLATNÉ)
3. **MNK kalkulačka**: M=8, N=13, K=15, Bottom=4, Total=40
4. **Transformované 43657381 → 60072028**, suma = 25
5. **Šifra dekódované**: SKOL, TSRP, ASAD, ORIM, **TUPO** (jediné SK slovo!), IRKS, DAHL, BADO
6. **den09/009.jpg** = cyklista POMALY idúca cez trávu (relevantné!)

### Testované výpočty (všetky 404):
| Suma | Slovak word | Hex calculation | Result |
|------|-------------|-----------------|--------|
| 3 | tri | 747269 + 747269 | 1494538 |
| 6 | sest | 736573 + 657374 | 1393947 |
| 25 | dvadsatpat | 647661 + 706174 | 1353835 |
| 29 | dvadsatdevat | 647661 + 766174 | 1413835 |
| 35 | tridsatpat | 747269 + 706174 | 1453443 |
| 39 | tridsatdevat | 747269 + 766174 | 1513443 |
| 40 | styridsat | 737479 + 736174 | 1473653 |

### Testované kategórie súborov (2000+ kombinácií):
- Všetky vypočítané hodnoty s/bez prípon
- Slovenské číslovky (jeden-päťdesiat)
- Pomaly/pomaličky varianty
- Šifra dekódované slová (tupo, skol, irks, atď.)
- Cyklotura/slovensko súvisiace
- MNK grid hodnoty
- Hex stringy ako názvy
- den09 obrázky a lokácie (Kláštorisko, Zaježová, Sekier)

### Neprebádané možnosti:
1. Súbor v úplne inom adresári
2. Iná interpretácia "správne číslice"
3. Kultúrna/lokálna referencia ktorú nepoznám
4. Chýbajúci krok v logickom postupe

## Status
**IN PROGRESS** - 2000+ kombinácií testovaných bez úspechu.

### Čo vieme s istotou:
1. K row = 8205, MNK suma = 40
2. Frame 0 a Frame 1 majú digit mapping (len 2 a 0 nezmenené)
3. 43657381 vyhýba sa "unchanged" digits (0, 2, 9)
4. MNK letters (13+14+11=38) = počet číslic dlhého čísla
5. napoveda.rar heslo = 9, obsah = "CYKLOTURA NAPRIEC SLOVENSKOM"
6. PUTO→TUPO je jediná šifra kde oba sú slovenské slová (kód 3214)
7. /slovensko/den09/009.jpg = cyklista pomaly tlačí bicykel cez trávu
8. /slovensko/den09/099.jpg = kozy, súčet číslic (0+9+9=18) = číslo levelu

### Kľúčové výpočty (všetky 404):
| Suma | Slovensky | Hex formula | Výsledok |
|------|-----------|-------------|----------|
| 29 | dvadsatdevat | first6+last6 | 1413835 |
| 40 | styridsat | first6+last6 | 1473653 |
| 13 | trinast | first6+last6 | 1364643 |
| 37 | tridsatsedem | first6+last6 | 1311925 |
| 122 | stodvadsatdva | first6+last6 | 1385127 |
| 157 | stopatdesiatsedem | first6+last6 | N/A |
| 10 | desat | hex | 6465736174 |

### Testované kategórie súborov (všetky 404):
- Slovenské číslovky: jeden až dvadsat, dvadsatdevat, trinast, atď.
- Pomaly varianty: pomaly, pomalicky, zvolna, pozvolna, postupne
- Hex hodnoty: 1d, 7a, 23, 25, 0a, atď.
- Level 10 štýl výpočty: 1413835, 1364643, 1473653, atď.
- Cipher dekódované: tupo, skol, tsrp, asad, orim, bado
- Den09 miesta: krpacovo, zajezova, detva, kalinka, sihla
- Cyklotura: bicykel, cyklista, luka, trava, polana
- Názvy z čísel: 43657381, 537145301, 099, 009

### Neprebádané možnosti:
1. Úplne iná interpretácia "správne číslice"
2. Skrytý súbor v inom adresári (/slovensko/den09/?)
3. Kombinácia viacerých hintov
4. Kultúrna referencia ktorú nepoznám

### Session 24/12/2025 - nové objavy:
- den09/009.jpg = cyklista v tráve = "pomaly" (slow movement)
- den09/099.jpg = kozy, 0+9+9=18 = level číslo
- PUTO→TUPO jediná "správna" šifra, suma kódu = 10
- Žiadne clickable areas v Level 18 HTML okrem image mapy

## Session 24/12 - Rozsiahle testovanie

### Testované prístupy (1000+ kombinácií):
1. **Slovak number words** - všetky čísla 1-29 a ich hex konverzie
2. **Cipher transformations** - SKOL, TSRP, TUPO, atď.
3. **MNK calculator values** - 2240, 6700, 8205, 0031
4. **Level 10 style sums** - first6 + last6 z hex slov
5. **Den09 files** - obrázky 009.jpg, 099.jpg
6. **Hash values** - MD5/SHA1 kľúčových slov
7. **Background searches** - číselné rozsahy 1000000-1500000

### Kľúčové poznatky:
- MNK mapped 43657381 = 60072028, suma = 25
- Všetky cipher permutácie na pozíciách 1-4 dávajú sumu 16
- napoveda heslo = 9, obsahuje "CYKLOTURA NAPRIEC SLOVENSKOM"
- GIF má 10s delay medzi framami
- den09/099.jpg existuje (obrázok s kozami, 0+9+9=18!)

### Neprebádané teórie:
1. Kombinácia cipher slov s den09 obrázkami
2. Skrytý odkaz v kalkulačka.gif (okrem MNK framu)
3. Špecifický súbor v /slovensko/ adresári
4. Alternatívna interpretácia "pomaličky"

## Session 24/12/2025 - KRITICKÝ OBJAV

### OPRAVA: Dlhé číslo má 39 číslic!
Pôvodne som mal 38-číslicové číslo končiace "...301", ale obrazok.jpg jasne ukazuje:
- **545746432486465452312314784565371453014** (39 číslic, končí na **3014**!)

### Prepočty s opraveným číslom:
- Last 9 digits: **371453014** (nie 537145301)
- Sum of last 9: **28** (nie 29!)
- 28 = "dvadsatosem" → hex obsahuje písmená (6f, 6d)

### Slovak slová s ALL-DIGIT hex:
| Slovo | Hex | All digits? |
|-------|-----|-------------|
| dva | 647661 | ✓ |
| tri | 747269 | ✓ |
| styri | 7374797269 | ✓ |
| pat | 706174 | ✓ |
| sest | 73657374 | ✓ |
| sedem | 736564656d | ✗ (6d=m) |
| osem | 6f73656d | ✗ (6f=o, 6d=m) |
| devat | 6465766174 | ✓ |
| desat | 6465736174 | ✓ |

### Výpočty:
| Sum | Slovak | Hex | First6+Last6 | Result |
|-----|--------|-----|--------------|--------|
| 28 | dvadsatosem | 647661...73656d | Obsahuje písmená! | N/A |
| 25 (MNK mapped) | dvadsatpat | 64766164736174706174 | 647661+706174 | **1353835** → 404 |
| 9 (napoveda) | devat | 6465766174 | 646576+766174 | **1412750** → 404 |
| 10 | desat | 6465736174 | 646573+736174 | **1382747** → 404 |

### Den09 objavy:
- **108.jpg** existuje! Ukazuje zastávku "Zaježová rázcestie" + smer "SEKIER"
- **109.jpg** = mapa Zaježovej oblasti s vrchmi Madačka 745m, Lukový Vrch 804m
- Images 101-120 existujú (okrem 102, 106)

### Testované location names (všetky 404):
- zajezova, razcestie, sekier, zastavka
- madacka, lukovy, polianky, detva, krivan
- 745, 804

### Interpretácia hints:
- Hint 4: "výsledok z kalkulačky určuje deň a počet" → Day=9, Count=9
- Sum of last 9 = **28** (s opraveným číslom)
- Ale "dvadsatosem" hex obsahuje písmená → možno iný prístup?

### Ďalšie možnosti:
1. "Správne číslice" nie sú last 9, ale niečo iné
2. Použiť digits-only z hex: 64766164736174673656 → 1321317 (404)
3. Možno odpoveď je v den09 súboroch, nie v /na_vyhliadke/

## Status
**IN PROGRESS** - 2500+ kombinácií testovaných bez úspechu.

## Kľúčové spojenie: Level 18 ↔ Den09

Citát na den09 stránke obsahuje presne credentials Level 18:
- "**prekrásna** krajina" = username
- "**výhľadov** plná" = password

Obrázok 009.jpg v den09 ukazuje cyklistu **pomaly** tlačiaceho bicykel cez trávu - priama referencia na "pomaličky"!

### Čo vieme s istotou:
1. napoveda.rar heslo = 9 ✓
2. Dlhé číslo má 39 číslic, sum posledných 9 = 28
3. "dvadsatosem" má v hex písmená (6f, 6d) → nemožno použiť Level 10 formulu
4. Spojenie s den09 cez citát a "pomaly" obrázok

### Testované (všetko 404):
- Všetky sumy 1-50 so slovenským slovom → hex → first6+last6
- Názvy súborov: pomaly, pomalicky, dalej, hore, stupaj, veza, rozhladna
- Miesta z den09: zajezova, polomy, detva, klastorisko
- Šifra dekódované: tupo, skol, tsrp
- Čísla: 28, 1382747, 1353835, atď.
- Súbory s príponami: .ne, .txt, .rar, .gif

### Možné smery:
1. Súbor s iným názvom ktorý som netestoval
2. Potrebná iná autentifikácia
3. Kultúrna/lokálna referencia
4. Výpočet ktorý som nesprávne interpretoval

## Session 24/12/2025 - Rozšírené testovanie (3000+ kombinácií)

### Nové výpočty testované:

**Celková suma všetkých číslic v dlhom čísle:** 161 (NIE 157!)
- 545746432486465452312314784565371453014
- Suma = 161

**CYKLOTURA NAPRIEC SLOVENSKOM - počet písmen:**
- CYKLOTURA = 9 písmen
- NAPRIEC = 7 písmen
- SLOVENSKOM = 10 písmen
- Celkom = 26

**26 = "dvadsatsest":**
- hex = 6476616473617473657374 (22 chars)
- first6 + last6 = 647661 + 657374 = 1305035 → 404

**Cipher "správne pozície" analýza:**
Kódy: 1243, 4321, 2341, 4321, 3214, 2143, 1432, 3412
- Pozície kde digit = pozícia:
  - 1243: pozície 1,2 správne (1 a 2) = 2 správne
  - 4321: 0 správnych
  - 2341: 0 správnych
  - 4321: 0 správnych
  - 3214: pozície 2,4 správne = 2 správne
  - 2143: 0 správnych
  - 1432: pozície 1,3 správne = 2 správne
  - 3412: 0 správnych
- **Celkom správnych pozícií = 6**
- 6 = "sest" → hex 73657374 → first6+last6 = 736573+657374 = 1393947 → 404

**Nezmenené číslice v transformovanom čísle 60072028:**
- Pozície s 0 alebo 2: pozície 2,3,5,6,7
- Hodnoty: 0, 0, 2, 0, 2
- Suma = 4

**Last 9 bez 5-ky (371453014 → 37143014):**
- Suma = 23
- 23 = "dvadsattri" → hex 64766164736174747269 → first6+last6 = 647661+747269 = 1394930 → 404

### Testované adresáre a súbory:

**/hra/na_vyhliadke/ (s príponami "", .ar, .txt, .gif, .jpg, .ne):**
- Všetky vypočítané čísla: 1393947, 1413835, 1382747, 1353835, 1473653, 1305035, 1394930, 1412750
- Hex stringy: 73657374, 6465766174, 6465736174, 64766164736174
- Slovenské číslovky: dva až päťdesiat, dvadsatdevat, trinast, atď.
- Pomaly varianty: pomalicky, pomaly, zvolna, pozvolna, postupne, krok_za_krokom
- Príslovie: pomaly_dalej_zajdes, trpezlivost, zajdes, dalej
- Pomalé zvieratá: slimak, korytnacka, zelva, lenivec, snail, turtle, sloth
- Šifra dekódované: skol, tsrp, asad, orim, tupo, irks, dahl, bado
- MNK hodnoty: 2240, 6700, 8205, 0031, 31, 17176, 9454
- 8-digit a transformed: 43657381, 60072028
- GIF delay: 2710, 10000, 10sec
- Skryté súbory: secret, hidden, skryty, kluc, key, answer, odpoved, riesenie

**/hra/ root:**
- pomalicky, pomaly, dalej, 19, level19, level_19, next, dalsi_level
- Všetky vypočítané čísla

**/slovensko/den09/:**
- pomalicky, pomaly, dalej, pustit, pokracuj, riesenie, kluc, cyklotura
- Všetky vypočítané čísla

### HTML analýza:
- Image map v Level 18 je **PRÁZDNA** - žiadne clickable areas!
- Musíme nájsť súbor aby sme mohli pokračovať

### Analýza obrazok.jpg a kalkulacka.gif:
- Žiadne skryté textové reťazce v obrazok.jpg (len JPEG artefakty)
- kalkulacka.gif nemá skryté dáta na konci súboru
- GIF delay = 10000ms

### Nezodpovedané otázky:
1. Čo presne znamená "správne číslice"?
2. Prečo 28 (suma posledných 9) nemožno použiť (obsahuje hex písmená)?
3. Aká je správna interpretácia "slovom preveď do hex"?
4. Kde je súbor ktorý "pomaličky pustí ďalej"?

## Session 25/12/2025 - Pokračovanie testovania

### Hlavná teória: Sum of unchanged digits = 6
- V dlhom čísle sú len 0 a 2 "nezmenené" v MNK transformácii
- Pozície 2: 9, 18, 21 (tri dvojky)
- Pozícia 0: 37 (jedna nula)
- Sum = 2+2+2+0 = **6**
- "sest" → hex = 73657374 → first6+last6 = 736573+657374 = **1393947**
- Výsledok 1393947 je **404**

### Testované nové kategórie (všetky 404):
1. **Čísla 2-5 s Level 10 formulou:**
   - dva(2) → 1295322
   - tri(3) → 1494538
   - styri(4) → 1534748
   - pat(5) → 1412348

2. **Cipher aplikovaný na 8-digit:**
   - 43657381 s kódom 3214 → 63458371

3. **Slovak proverbs:**
   - pomaly_dalej_zajdes, zajdes, isto

4. **Music tempo:**
   - adagio, lento, largo, grave, andante

5. **Den09 locations:**
   - krpacovo, zajezova, polomy, detva, pohodicka

6. **GIF timing:**
   - 1000 (centiseconds), 10000 (ms), 10 (seconds)

7. **Cipher words:**
   - sklo, prst, dasa, miro, puto, risk, dlha, doba
   - skol, tsrp, asad, orim, tupo, irks, dahl, bado

8. **MNK related:**
   - 2240, 6700, 8205, 0031, 17176, 22427

9. **Viewpoint words:**
   - vyhliadka, veza, rozhladna, schody, stupaj

10. **Previous level references:**
    - kafka, dominik, rykyncice, vrak, auto

### Objavené den09 obrázky:
- 060.jpg (cesta cez polia)
- 108.jpg (zastávka Zaježová)
- 118.jpg (drevená chalupa)
- Images 101-122 existujú

### Bulk search výsledky:
- Rozsah 1392947-1394947 - žiadne súbory nájdené

### Aktuálne nezodpovedané otázky:
1. Prečo 1393947 nefunguje ak suma = 6?
2. Je Level 10 formula správna pre Level 18?
3. Existuje iný význam "správne číslice"?
4. Je súbor v úplne inom adresári?
5. Potrebujem kultúrnu/lokálnu znalosť?

## Status
**IN PROGRESS** - 3500+ kombinácií testovaných bez úspechu.

### Potrebné:
- Nový pohľad na hinty
- Možná kultúrna/lokálna referencia ktorú nepoznám
- Alternatívna interpretácia "správne číslice"
- Kontakt s autorom hry alebo nápoveda od niekoho kto level riešil
