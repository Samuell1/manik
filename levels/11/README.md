# Level 11 (1464928)

**URL:** https://manik.sk/hra/1464928/

## Ako sme sa sem dostali
- Level 10: KRAL FRANTISEK → 36139887223419 → .ne súbor
- .ne súbor: "Použi úplne posledné slovo z Kafkovho popisu tabuľky a skonvertuj ho do hexadecimálneho tvaru"
- **DÔLEŽITÉ:** Kafkov popis má DLHŠIU verziu, posledné slovo je "rychlejsie" (nie "pasovala")
- rychlejsie → hex = 727963686c656a736965
- Digits only: 727963686656736965 (18 digits)
- First 6: 727963, Last 6: 736965
- Sum: 727963 + 736965 = **1464928** (7 digits!)

## Popis stránky
"Na lazoch za kopcom si objavil navždy odparkované auto pána inžiniera"
(On the meadows behind the hill you discovered the forever parked car of Mr. Engineer)

## Hint
- Číslice závodného auta označujú poradie nepotrebných písmen samotného závodníka
- (The racing car digits indicate the order of unnecessary letters of the racer himself)

## Obrazok Analysis
- **obrazok.jpg** - závodné auto s číslami
- Obsahuje clickable area → "../na_lazoch/"
- Car displays: **SALTO 15**
- Red pipe wrench (hasák) on right side

## Numbers in Image
| Location | Numbers | ASCII Decode |
|----------|---------|--------------|
| Top left | 42 64 677 7 | * @ (677 too high) |
| Diagonal | 36 248 216 37 | $ ř Ř % (extended ASCII) |
| Right side | 92 100 135 77 | \ d ? M (sum=404) |
| On car | 122 65 51 123 | z A 3 { |
| Below car | 100 114 97 107 | **"drak"** (dragon) ✓ |
| Bottom | "Ho 292 987 3" | Initials? Numbers? |

## Ďalší level
- **URL:** https://manik.sk/hra/na_lazoch/
- **Status:** 401 (vyžaduje autentifikáciu)
- Potrebné nájsť username:password z hintu o závodníkovi

## Hlavná analýza

### Štandardná interpretácia hintu
- Závodník: **SALTO** (viditeľné na aute)
- Číslo auta: **15** → číslice 1 a 5 = pozície nepotrebných písmen
- SALTO: S(1) A(2) L(3) T(4) O(5)
- Remove positions 1,5 (S and O) = **ALT**

### Alternatívna interpretácia (DRAK)
- DRAK (from ASCII 100 114 97 107)
- D(1) R(2) A(3) K(4) - only 4 letters
- Remove position 1 only = **RAK**

## Testované kombinácie (500+)

### Základné kombinácie (všetky 401)
- salto:alt, alt:salto
- drak:rak, rak:drak
- salto:drak, drak:salto
- alt:rak, rak:alt
- salto:rak, drak:alt

### Transformácie slov (všetky 401)
- kafka:afk, zoltan:oltn
- skoda:kod, hasak:asa
- zavodnik:avonik, pretekar:rekar
- jazdec:azdc, pilot:ilo
- vodic:odi, motor:oto
- kopec:ope, lazoch:azoh

### Encoding pokusy (všetky 401)
- ASCII encoded: salto:657684, drak:826575
- Hex encoded: salto:414c54, drak:52414B
- Base64: salto:QUxU
- Caesar cipher shifts (+15, -15, +1, -1, +5, -5)
- Position sums: salto:33, salto:34, salto:67

### Regionálne názvy (všetky 401)
- cerovo:lazy, lazy:cerovo
- rykyncice:alt, krupina:rupna
- litava:itaa, bzenica:alt

### Škoda modely (všetky 401)
- felicia:elia, fabia:abi
- octavia:ctaia, favorit:avort

### Anagramy SALTO (všetky 401)
- talos:alo, slota:lot
- altos:lto, otlas:tla

### Case varianty (všetky 401)
- SALTO:ALT, Salto:Alt
- DRAK:RAK, Drak:Rak

### Číselné kombinácie (všetky 401)
- salto:15, 15:alt, salto15:alt
- 361:404, 404:alt, salto:404
- salto:33, salto:34 (position sums)

## Analýza čísel

### Sum of number groups
- 42+64+677+7 = 790
- 36+248+216+37 = 537
- 92+100+135+77 = **404** (HTTP Not Found!)
- 122+65+51+123 = 361
- 100+114+97+107 = 418

### "Ho 292 987 3" interpretácie
- Ho = Holmium (element 67)?
- Ho = Initials (Horák, Holub, Homola)?
- 292 987 = coordinates? Patent number? Phone?

### ASCII letters found
- Unique letters: d, r, a, k, M, A, z
- "drak" clearly intentional
- Other letters scattered but no clear word

## Spojenie s Level 9

Level 9 hint: "výsledok z dvoch lazov ťa pustí do ďalšieho levelu"
- Suggests TWO "laz" (meadows) provide the answer
- Level 11 destination: /na_lazoch/ (on the meadows)
- Possible connection between Level 9 and Level 11 puzzles

## Možné príčiny neúspechu

1. **Neznámy závodník** - "Závodník" môže byť špecifická osoba (slovenský pretekár?)
2. **Encoding/decoding** - User hint suggests encode/decode step needed
3. **Level 9 spojenie** - May need to solve Level 9 "lazy" puzzle first
4. **Skrytý súbor** - May be a hidden file with additional hints (like .ne in Level 10)
5. **Kultúrna referencia** - Slovak motorsport or cultural reference unknown to us

## Potrebné ďalšie kroky

1. Research Slovak rally/racing drivers associated with "SALTO" or number 15
2. Investigate Level 9 "lazy" puzzle more thoroughly
3. Look for hidden files or alternate interpretations
4. Consider the encoding/decoding hint from user

## Status
**IN PROGRESS** - 500+ kombinácií testovaných, riešenie nenájdené
