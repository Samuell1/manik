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

### Možné vzory
- 8 slov, 4 písmená každé
- Prvé písmená: L, M, M, A, N, O, B, R = LMMANOBR?
- Možno anagramy alebo šifra súvisiaca s lienkou

### Latrina
- Vyžaduje autentifikáciu (401)
- Potrebné nájsť username:password

## Status
IN PROGRESS - analyzujem text a lienku
