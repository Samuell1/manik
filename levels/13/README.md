# Level 13 (Kuchyna12)

**URL:** https://manik.sk/hra/kuchyna12/

## Odkiaľ
- Level 12: PRIEVAN markery + kluc.txt vzor
- Čísla markerov (5,8,2,4,9,6,2) použité ako T9 klávesy
- X pozície (2,2,3,2,3,2,1) vybrali písmená: K,U,C,H,Y,N,A
- KUCHYNA + 12 = **kuchyna12**

## Popis
"Vošiel si do zaujímavej kuchyne .." (You entered an interesting kitchen)

## Hinty
1. nájdi v skrinke potrebnú šifru (find the necessary cipher in the cabinet)
2. chrobáčika pozná každý (everyone knows the beetle/ladybug)
3. niečo je na tejto kuchyni dôležité (something is important about this kitchen)

## Obrazky
- **obrazok.jpg** - kuchyňa s skrinkami, lienkou, a textom

## Clickable areas
- **skrinka** (coords: 503, 75, 655, 242) - cabinet
- **../latrina/** (coords: 745, 550, 788, 587) - lightbox, vyžaduje 401 auth

## Analýza obrázku

### Lienka (Ladybug)
- V strednom okne skrinky je obrázok lienky
- Hint: "chrobáčika pozná každý"
- Slovensky: lienka, slniečko sedembodkové

### Text na obrázku
```
LANO MASŤ MÄTA AUDI
NOHY OSOH BOKY ROKY
```

**Preklad slov:**
- LANO = rope
- MASŤ = ointment
- MÄTA = mint (herb)
- AUDI = car brand
- NOHY = legs
- OSOH = benefit/profit
- BOKY = sides/hips
- ROKY = years

### Šifra z 8 slov
Použitím pozícií 1,2,3,4,1,2,3,4:
- LANO[1]=L, MASŤ[2]=A, MÄTA[3]=T, AUDI[4]=I
- NOHY[1]=N, OSOH[2]=S, BOKY[3]=K, ROKY[4]=Y
- **Výsledok: LATINSKY** (= "in Latin" / "po latinsky")

### Interpretácia
- LATINSKY je inštrukcia - prelož do latinčiny
- "chrobáčik" = lienka (ladybug)
- Lienka latinský = **Coccinella septempunctata** (7-bodková lienka)
- septem = 7, punctata = bodkovaná

### Latrina
- Vyžaduje autentifikáciu (401)
- Testované kombinácie: lienka:coccinella, coccinella:septempunctata, latinsky:*, a mnohé ďalšie
- Zatiaľ nenájdené správne credentials

### Skrinka.psd
- PSD súbor z Adobe Photoshop
- Obsahuje text "Pridaj k tomuto suboru koncovku .psd"
- JFIF data (možný JPEG embedded)

## Kompletná analýza obrázku

### Objekty v kuchyni:
- skrinka, lienka, taniere, poháre, dvierka, stôl, stolička
- ružová/fialová miska, rádio, sklené nádoby
- oválne ozdoby na dvierkach (pletené)

### Dôležité pozorovania:
1. **Zrkadlová symetria** - kuchyňa je perfektne zrkadlovo symetrická
2. **Lienka** - 7-bodková (Coccinella septempunctata)
3. **8 slov** - usporiadané 4x2 grid
4. **Červená šípka** - ukazuje na latrina

### Testované kombinácie (500+):
- Všetky kombinácie: latinsky, lienka, coccinella, septempunctata
- Kuchynské prvky: skrinka, taniere, pohar, dvierka, stol, miska
- Čísla: 7, 8, 4, 13, sedem, siedem
- Zrkadlové: zrkadlo, symetria, odraz, speculum
- Obrátené slová: lienka↔akneil, latinsky↔yksnitál

### Kľúčové hinty:
1. LATINSKY = inštrukcia na preklad do latinčiny
2. Septempunctata = 7-bodková (scientific name lienky)
3. Zrkadlová symetria kuchyne môže byť hint

## Status
IN PROGRESS - 500+ kombinácií testovaných, latrina stále 401
