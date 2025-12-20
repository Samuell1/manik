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

## Obrazok
- obrazok.jpg - závodné auto s číslami
- Obsahuje clickable area → "../na_lazoch/"

## Ďalší level
- **URL:** https://manik.sk/hra/na_lazoch/
- **Status:** 401 (vyžaduje autentifikáciu)
- Potrebné nájsť username:password z hintu o závodníkovi

## Analýza hintu
- Závodník: **SALTO** (viditeľné na aute)
- Číslo auta: **15** → číslice 1 a 5 = pozície nepotrebných písmen
- SALTO bez pozícií 1,5 (S a O) = **ALT**

## Detaily z obrazka
- Rusty Škoda s nápisom "SALTO 15"
- Červený hasák (pipe wrench) na pravej strane - clickable area
- Rozptýlené čísla: 42 64 677 7, 92 100 135 77, 122 65 51 123, 100 114 97 107, atď.
- Čísla 100 114 97 107 = ASCII "drak" (dragon)
- "Ho 292 987 3" viditeľné dole

## Skúšané kombinácie (všetky 401)
- salto:alt, alt:salto
- drak:alt, alt:drak
- hasak:alt, kluc:alt
- laz:alt, lazy:alt
- kafka:alt, zoltan:alt
- A desiatky ďalších kombinácií

## Súvislosť s Level 09
- Level 09 má hint o "lazy" (lúky/lazy)
- Level 09 obrazok má číslo: 383935303445343437 → ASCII "89504E447" (PNG header?)
- Možno potrebujem najprv vyriešiť Level 09 úplne

## Ďalšie skúšané kombinácie
- KAFKA → bez pozícií 1,5 → AFK
- ZOLTAN → bez pozícií 1,5 → OLTN
- SKODA → bez pozícií 1,5 → KOD
- ZAVODNIK → bez pozícií 1,5 → AVONIK
- INZINIER → bez pozícií 1,5 → NZNER
- CERVENY (red) → bez pozícií 1,5 → ERVNY
- inzinier, pan, auto, kopec, laz varianty
- Rovnaké heslo ako meno: alt:alt, salto:salto, atď.
- Číselné: 15:15, 1:5, salto:15
- ASCII dekódované: drak, arka (z čísel v obrázku)
- Kombinácie s drak:arka, arka:drak
- Case varianty: SALTO:ALT, Drak:Arka
- Otočené pozície (ponechať 1,5): so:alt
- 300+ kombinácií testovaných - všetky vracajú 401

## Ďalšie pokusy (session 2)
- Car model names: MOSKVIC→OSKIC, WARTBURG→ARTURG, SKODA
- Slovak surnames starting with HO: HORAK→ORA, HOLUB→OLU, HORVAT→ORVT
- Racing vocabulary: preteky, pretekar, zavod, jazdec, rychlost, pilot
- Anagrams of SALTO: altos, talos, slota
- Level 9 + Level 11 combinations: rykyncice+alt, dominik+drak
- Removed vs remaining: so:alt, s:o
- DRAK formula: remove pos 1 = RAK
- Special characters: alt_drak, salto-15
- Numbers from image as credentials
- Exact case testing: SALTO:ALT, Drak:Arka

## Status
IN PROGRESS - 400+ kombinácií testovaných, všetky vracajú 401

## Dodatočná analýza (session 3)

### Čísla v obrazku - detailná analýza
- 42 64 677 7 (top left) - 677 je príliš vysoké pre ASCII
- 36 248 216 37 (diagonal) - 248, 216 sú vysoké
- 92 100 135 77 (right) - súčet = 404 (HTTP kód!)
- 122 65 51 123 (on car) = z(122) A(65) 3(51) {(123) - "zA3{" - nečitateľné
- 100 114 97 107 = "drak" ✓
- Ho 292 987 3 - "Ho" môže byť meno (Horák?) alebo prvok Holmium

### Reversed ASCII
- 100 114 97 107 = "drak" (vpred)
- 107 97 114 100 = "kard" (vzad) - "kard" = meč v maďarčine!

### Vlastník auta
- Popis hovorí "auto pána inžiniera" = Ing. Zoltán KAFKA z Level 10
- KAFKA: K(1) A(2) F(3) K(4) A(5) → bez 1,5 = AFK

### Modely áut
- SKODA: S(1) K(2) O(3) D(4) A(5) → bez 1,5 = KOD ("kód"!)
- WARTBURG → bez 1,5 = ARTURG (meno Arthur?)
- MOSKVIC → bez 1,5 = OSKIC

### Spojenie s Level 09
- Level 09 hint: "výsledok z dvoch lazov ťa pustí do ďalšieho levelu"
- Level 11 URL next = /na_lazoch/ (na lazoch = na lúkach)
- Možno potrebujem vyriešiť Level 09 puzzle najprv

### Level 09 číslo v obrazku
- 383935303445343437 → ASCII = "89504E447"
- Toto je takmer PNG header (89 50 4E 47), ale má extra "4"
- Hint: "oprav prvých 8 hex bajtov" - opraviť corrupted PNG?

### Skúšané kombinácie (nové)
- kafka:afk, afk:kafka
- skoda:kod, kod:skoda
- drak:kard, kard:drak
- wartburg:arturg
- dominik:alt, wiktoria:alt, rykyncice:alt
- lazy:alt, laz:alt, lazoch:alt
- Všetky vracajú 401

## Session 4 - Extensive testing

### Additional combinations tested (all 401):
- skoda:kod, zavodnik:avonik
- kafka:afk, zoltan:oltn
- homola:omoa (Slovak racing driver)
- hasak:asa (pipe wrench transformation)
- Description words: lazoch:azoh, kopcom:opcm, navzdy:avzy
- drak:rak (if DRAK only removes position 1)
- All meadow-related: lazy:alt, laz:alt, nalazoch:alt
- Mass test of all key words in all combinations

### File searches (all 404):
- .ne files like Level 10
- hint/napoveda/tip files
- Number-based filenames

### Total combinations tested: 500+

## Session 5 - Encoding/Decoding attempts

### User hint: "decode and encode letters"

### ASCII encoding tests (all 401):
- salto:657684 (ALT as ASCII decimal: A=65, L=76, T=84)
- salto:414c54 (ALT as hex)
- drak:826575 (RAK as ASCII: R=82, A=65, K=75)
- drak:52414B (RAK as hex)
- 100114097107:657684 (drak ASCII : alt ASCII)

### Base64 encoding (all 401):
- salto:QUxU (ALT in Base64)
- U0FMVE8:QUxU (SALTO:ALT both Base64)
- drak:cmFr (rak in Base64)

### Caesar cipher tests (all 401):
- salto:hpaid (SALTO +15)
- salto:dlwez (SALTO -15)
- salto:pai (ALT +15)
- salto:fnygb (SALTO ROT13)
- salto:bmu (ALT +1)
- salto:fqy (ALT +5)
- salto:zks (ALT -1)

### Vigenère cipher with key "15" (all 401):
- salto:tfmyp (+15151 pattern)
- salto:rvkon (-15151 pattern)

### Letter position encoding (all 401):
- salto:11220 (ALT positions: A=1, L=12, T=20)
- salto:33 (sum of ALT positions)
- salto:34 (sum of S+O positions: S=19, O=15)
- drak:18111 (RAK positions)
- 19112015:11220 (SALTO:ALT positions)

### Additional word transformations (all 401):
- virax:ira (wrench brand)
- hora:ora (mountain)
- vodic:odi (driver)
- motor:oto, koleso:oleo, volant:olat (car parts)
- felicia:elia, fabia:abi, octavia:ctaia (Škoda models)
- stillson:tilson, ridgid:idgd, bahco:ahc (tool brands)

### Reversed/anagram tests (all 401):
- kard:drak, drak:kard (kard = sword in Hungarian)
- otlas:tla (SALTO reversed)
- talos:alo, slota:lot, altos:lto

### Geographic/regional names (all 401):
- cerovo:lazy, lazy:cerovo (Camping Lazy near Cerovo)
- litava:itaa, krupina:rupna
- laz:laz, lazy:lazy, alt:laz, laz:alt

### Number-based tests (all 401):
- 404:alt (sum of 92+100+135+77)
- salto:404, drak:361
- 361:404, salto:67

## Level 9 Connection Analysis

### Downloaded Level 9 files for analysis:
- obrazok.jpg - contains number 383935303445343437
- dom.jpg - rural Slovak house
- Level 9 hint: "Wiktória je kamarátka" (Wikipedia is a friend)

### Level 9 hints suggest:
1. Find first file, fix first 8 hex bytes (corrupted PNG?)
2. Get all "lazy" (meadows)
3. Find second file using town name
4. Replace question mark
5. Result from TWO "laz" opens next level

### Cross-level connection:
- Level 9: "výsledok z dvoch lazov ťa pustí do ďalšieho levelu"
- Level 11 destination: /na_lazoch/
- Both levels reference "lazy" (meadows)
- May need to solve Level 9 fully first

## Možné príčiny
1. "Závodník" je špecifické meno ktoré nepoznám
2. Čísla v obrázku majú iný význam (nie ASCII)
3. Potrebná informácia z Level 09 "lazy" puzzle
4. Kultúrna referencia na slovenský motorsport
5. Spojenie dvoch "laz" z Level 09 a Level 11
6. Hidden clue in the image we haven't found
7. **Encoding/decoding step** - user hint suggests transformation needed
8. **Hidden file** - like .ne file in Level 10
