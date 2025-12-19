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
- 200+ kombinácií testovaných - všetky vracajú 401

## Status
IN PROGRESS - správna interpretácia hintu zatiaľ nenájdená
Potrebná dodatočná analýza alebo hint od užívateľa
