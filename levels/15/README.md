# Level 15 (Doma v izbe)

**URL:** https://manik.sk/hra/doma_v_izbe/

## Prihlasovacie údaje
- **Username:** utekac
- **Password:** havrilovo

**Odkiaľ:** Level 14 - autobusová zastávka v Utekáči/Drahová
- Posledné dve cieľové stanice: Utekáč, Havrilovo

## Popis
"Nachádzaš sa v izbe .."

## Hinty
- bez indícií (žiadne oficiálne hinty)

## Clickable areas
- **pec.jpg** (coords: 732, 459, 781, 514) - lightbox, detailná fotka pece
- **../opilec/** (coords: 427, 539, 470, 591) - vyžaduje auth (401)

## Obrazok
- obrazok.png - izba so zelenou stenou
- V pravom hornom rohu: **žltý a modrý štvorec** (možný hint)
- Červené šípky ukazujú na klikateľné oblasti
- Objekty: posteľ, pec, hodiny, lampa, ikony (Panna Mária, Ježiš), kríž, umývadlo

## Analýza

### Farby v rohu
- Žltý štvorec (#FFFF00?)
- Modrý štvorec (#0000FF?)
- Možná súvislosť s credentials

### Objekty v izbe
- Pec (stove) - má detail v pec.jpg
- Posteľ (bed) - modrá prikrývka
- Hodiny (clock) - na stene vľavo
- Ikony (icons) - náboženské obrazy
- Kríž (cross) - medzi ikonami
- Lampa (lamp) - na poličke
- Umývadlo (sink) - pri peci

## Testované kombinácie (všetky 401)
- zlta:modra, modra:zlta
- yellow:blue, blue:yellow
- postel:pec, pec:postel
- hodiny:lampa, izba:pec

## Ďalší level
- **URL:** https://manik.sk/hra/opilec/
- **Status:** 401 (credentials neznáme)

## Status
IN PROGRESS - hľadám credentials pre /opilec/
