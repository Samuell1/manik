# Level 10 (Kopec)

**URL:** https://manik.sk/hra/kopec/

## Popis
V lese si objavil tajne laboratorium Ing. Zoltana Kafku, inziniera

## Klucove objavy
1. Obrazok obsahuje text "KRAL FRANTISEK" a "http://bit.ly/"
2. HTML komentar: <!-- kafka-vynalezy -->
3. bit.ly/kafka-vynalezy → Facebook album s Kafkovymi vynalezmi

## Dekodovanie KRAL FRANTISEK
KRAL FRANTISEK = KR-AL-F-RA-N-TI-SE-K (prvky periodickej tabulky)
- Kr=36, Al=13, F=9, Ra=88, N=7, Ti=22, Se=34, K=19
- Concatenated: 36139887223419 (14 cislic!)

## Hint
- za ziskane 14 miestne cislo pridaj typ suboru z tabulky podla hodnoty cisla tohto levelu
- z vysledku zrataj prvych a poslednych 6 cisiel
- 7 miestny sucet pouzi do URL

## Kafkova tabulka
- Facebook album obsahuje Kafkovu abecedne zoradenu periodicku tabulku
- 10. prvok v abecednom poradi = Ba (Barium) = atomove cislo 56

## Subory
- obrazok.jpg - obrazok rozhladne s textom
- page.html - HTML stranka levelu

## Status
**COMPLETED** - Level 11 nájdený na /1464928/

## PROGRESS UPDATE

### Súbor nájdený!
- **36139887223419.ne** - ASCII text file
- Inštrukcie: "Použi úplne posledné slovo z Kafkovho popisu tabuľky a skonvertuj ho do hexadecimálneho tvaru"

### Kafkov popis tabuľky (posledné slovo):
"...lebo som dlho nemohol nájsť samohlásku, ktorá by do názvu **pasovala**."

### Konverzia:
- pasovala → hex = **7061736f76616c61**

### Skúšané:
- Hex ako URL: 404
- Hex ako filename: 404  
- Hex ako heslo: ?
- Rôzne výpočty s hex: 404

### RIEŠENIE NÁJDENÉ!

**Kľúčový objav:** Kafkov popis tabuľky má DLHŠIU verziu!
- Kratšia verzia končí: "...ktorá by do názvu **pasovala**."
- ÚPLNÁ verzia pokračuje: "Takto sa dajú prvky medzi sebou zlučovať prehľadnejšie a nové zlúčeniny môžem vynachádzať **rychlejsie**."

**Posledné slovo = rychlejsie** (NIE pasovala!)

**Výpočet:**
1. rychlejsie → hex = 727963686c656a736965 (20 znakov)
2. Digits only: 727963686656736965 (18 číslic)
3. First 6: 727963
4. Last 6: 736965
5. Sum: 727963 + 736965 = **1464928** (7 číslic!)

**Level 11 URL:** https://manik.sk/hra/1464928/
