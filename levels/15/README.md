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

## RIEŠENIE ✓

### Kľúčový objav: RGB hex kódy
V pravom hornom rohu obrázka sú dva farebné štvorce:
- **Žltý štvorec**: RGB(171, 193, 35) = hex **#ABC123**
- **Modrý štvorec**: RGB(18, 58, 188) = hex **#123ABC**

Hex kódy farieb sú priamo credentials:
- Username: **abc123** (zo žltého štvorca)
- Password: **123abc** (z modrého štvorca)

### Prečo "bez indícií"?
Hint "bez indícií" bol pravdivý - neboli žiadne textové hinty.
Odpoveď bola priamo zakódovaná vo vizuálnom prvku (farby štvorcov).

## Obrazky
- **obrazok.png** - izba so zelenou stenou, nábytok, ikony, pec
  - V pravom hornom rohu: žltý a modrý štvorec (kľúčový hint!)
- **pec.jpg** - detail pece s otvorenou debnou

## Viditeľné objekty v izbe
- Zelená stena
- Ikony: Panna Mária (modrá), Ježiš (zlatá svätožiara)
- Kríž medzi ikonami
- Hodiny (slnečný dizajn)
- Luster (drevený)
- Posteľ s modrým prehozom
- Pec/sporák
- Umývadlo
- Zelená fľaša na stole

## Detail pece (pec.jpg)
- Biely smaltovaný štítok na peci
- Otvorená drevená debna (uhlák)
- Modrá smaltovaná miska na peci
- Čierny hrniec, pokrievka

## Ďalší level
- **URL:** https://manik.sk/hra/opilec/
- **Auth:** abc123:123abc
- **Level:** 16

## Status
VYRIEŠENÉ ✓
