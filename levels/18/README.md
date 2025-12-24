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

## Testované súbory (404)
- cyklotura, pomaly, slow, pomalicky, slowly
- Hex súčtov: 1d, 15, e, 27, 25, 2be
- Slovenské čísla: dvadsatdevat, devat, strnast, dvadsatjeden
- Hex kódovania: 647661, 6465766174, 64766164
- Pomalé zvieratá: korytnacka, slimak, turtle, snail
- Šifra dekódovaná: skol, tsrp, asad, orim, tupo, irks, dahl, bado
- Kombinácie: cyklotura_napriec_slovenskom, CNS, cns
- /vylet/den7-den20 neexistujú
- Jednoduché čísla 0-9, 29, 21, 37, 39

## Ďalší level
- **URL:** https://manik.sk/hra/??? (clickable area v obrazku)
- **Status:** Hľadám "súbor ktorý pomaly pustí ďalej"

## Status
**IN PROGRESS** - napoveda.rar rozšifrované, hľadám ďalší súbor podľa hintu "CYKLOTURA NAPRIEC SLOVENSKOM"
