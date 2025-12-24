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
- **Dlhé číslo:** 54574643248646545231231478456537145301 (38 číslic)

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

## Status
**IN PROGRESS** - 1000+ kombinácií testovaných bez úspechu.

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
