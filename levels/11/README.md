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

## Možné príčiny
1. "Závodník" je špecifické meno ktoré nepoznám
2. Čísla v obrázku majú iný význam (nie ASCII)
3. Potrebná informácia z Level 09 "lazy" puzzle
4. Kultúrna referencia na slovenský motorsport
5. Spojenie dvoch "laz" z Level 09 a Level 11
