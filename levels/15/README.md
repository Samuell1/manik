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

### Farby
- zlta:modra, modra:zlta, zlty:modry, modry:zlty
- yellow:blue, blue:yellow, green:blue
- zelena:stena, stena:zelena, farba:zelena
- gelb:blau (nemecky), jaune:bleu (francúzsky)

### Objekty z izby
- postel:pec, pec:postel, hodiny:lampa
- stol:stolica, obraz:stena, okno:dvere
- ikona:kriz, maria:jezis, jezis:maria

### Alkohol/opilec súvisiace
- vino:pivo, pivo:vino, palinka:slivovica
- opity:triezvy, spanok:kocovina
- frankovka:modra (z výletu)

### Vlajky
- ukrajina:vlajka, svedsko:vlajka
- ukraine:flag, sweden:flag

### Ostatné
- bez:indicii, stvorec:farba
- doma:izbe, izbe:doma
- koordináty: 732:459, 427:539

### Možné interpretácie žltý+modrý
1. Yellow + Blue = Green (stena je zelená)
2. Vlajka Ukrajiny/Švédska
3. RGB hodnoty
4. Semafór/signál

## Ďalší level
- **URL:** https://manik.sk/hra/opilec/
- **Status:** 401 (credentials neznáme)

## Status
IN PROGRESS - hľadám credentials pre /opilec/
- 300+ kombinácií testovaných
- Žltý/modrý štvorec ostáva záhadou

## Ďalšie pokusy potrebné
- Steganografia v PNG/JPG
- Analýza pixelov v rohových štvorcoch
- Slovenské idiomy a frázy
- Súvislosť s predchádzajúcimi levelmi
- Možná referencia na vylet/výlet story
