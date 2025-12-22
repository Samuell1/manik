# Level 14 (Latrina)

**URL:** https://manik.sk/hra/latrina/

## Prihlasovacie údaje
- **Username:** alleniccoc (coccinella reversed)
- **Password:** atatcnupmetpes (septempunctata reversed)

**Odkiaľ:** Level 13 - zrkadlová kuchyňa
- LATINSKY cipher = prelož do latinčiny
- lienka = Coccinella septempunctata
- Zrkadlo = obe slová otočené

## Popis
"Zdá sa, že na latrine nie je nič zaujímavé .."

## HTML komentár
`<!-- Base64 -->` - hint na Base64 encoding!

## Hinty
1. textový 'súbor' budeš potrebovať ako prvý (text file first)
2. vraví sa, že trikrát meraj a raz reš (measure 3x, cut once)
3. pálenú hlinu s poškodenou hlavičkou nerozbalíš (burned clay with damaged header can't unpack)
4. tretí deň ti urýchli hľadanie (third day speeds up search)

## Clickable areas
- **../doma_v_izbe/** (coords: 730, 330, 788, 380) - vyžaduje auth

## RIEŠENIE ✓

### Krok 1: subor.txt
- Súbor `subor.txt` obsahuje Base64 kódovaný text
- Hint "trikrát meraj" = dekóduj 3x Base64
- Po 3x dekódovaní: "Potrebujes stiahnut subor: terakota"

### Krok 2: terakota
- "Pálená hlina" = terakota (terracotta)
- Súbor `terakota` je ZIP s poškodenou hlavičkou
- Prvé 4 bajty (00 00 00 00) treba nahradiť ZIP hlavičkou (50 4B 03 04)
- Po oprave ZIP obsahuje: odkaz na manik.sk/vylet

### Krok 3: Výlet - Deň 3
- Hint "tretí deň" = pozri /vylet/den3/
- Hľadaj "zastávku s častými odchodmi autobusov"
- Obrázok 029.jpg - autobusová zastávka s cestovným poriadkom
- "Dve posledné cieľové stanice sú dôležité"

### Krok 4: Credentials
- Cieľové stanice: **Utekáč** (Dlhá Lúka), **Utekáč** (Havrilovo)
- Credentials pre /doma_v_izbe/: `utekac:havrilovo`

## Súbory
- obrazok.jpg - obrázok latríny
- subor.txt - Base64 encoded (3x)
- terakota - ZIP s poškodenou hlavičkou
- 029.jpg - obrázok autobusovej zastávky (z vylet/den3/)

## Ďalší level
- **URL:** https://manik.sk/hra/doma_v_izbe/
- **Auth:** utekac:havrilovo
- **Level:** 15

## Status
VYRIEŠENÉ ✓
