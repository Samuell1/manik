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

## Status
**IN PROGRESS** - Rozsiahle hľadanie súboru "pomaličky pustí ďalej", 300+ kombinácií testovaných
