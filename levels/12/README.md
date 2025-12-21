# Level 12 (Na lazoch)

**URL:** https://manik.sk/hra/na_lazoch/

## Prihlasovacie údaje
- **Username:** vrak
- **Password:** auto

**Odkiaľ:** CP850 kódovanie čísel z Level 11:
- 118 114 97 107 = "vrak" (wreck/shipwreck)
- 97 117 116 111 = "auto" (car)

## Popis
"Ocitol si sa pred starým opusteným domom .." (You found yourself in front of an old abandoned house)

## Hinty
1. nie je všetko tak, ako sa na prvý pohľad môže zdať (things aren't as they seem)
2. **prievan** roztrieskal všetky okná na dome (dekódované z HTML entít &#112;&#114;&#105;&#101;&#118;&#97;&#110;)
3. v hrnci na verande si našiel Nokiu 6310i
4. 'X' ťa navedie na správnu stopu
5. k výsledku pridaj číslo aktuálneho levelu (12) a použi URL do ďalšieho levelu

## Obrazky
- **obrazok.jpg** - hlavný obrázok (starý opustený dom s rozbitými oknami)
- **stena.jpg** - lightbox (coords: 299, 381, 341, 425) - zobrazuje stenu s číslovanými markermi

## Analýza stena.jpg
V obrázku stena.jpg sú viditeľné location-pin markery s číslami a písmenami:
- Markery obsahujú páry: 8R, 4E, 2I, 5P, 2N, 9V, 6A
- Písmená tvoria slovo **PRIEVAN** (keď sa preskupia)
- Čísla: 8, 4, 2, 5, 2, 9, 6 (suma = 36)

## Nokia 6310i
- Starý telefón s T9 klávesnicou
- T9 kódovanie: 2=ABC, 3=DEF, 4=GHI, 5=JKL, 6=MNO, 7=PQRS, 8=TUV, 9=WXYZ
- PRIEVAN v T9: P=7, R=7, I=4, E=3, V=8, A=2, N=6 → 7743826
- 'X' je na klávese 9, pozícia 2 (WXYZ)

## Testované interpretácie (všetky 404)
- **prievan12**, prievan_12, prievan-12, 12prievan
- **7743838** (T9 číslo 7743826 + 12)
- **49** (suma T9 číslic 37 + 12)
- **48** (suma markerov 36 + 12)
- Rôzne čísla: 137, 149, 219, 207, 85 (matematické operácie s markermi)
- Slovné variácie: vietor12, draft12, nokia12, stena12
- Transformácie: alphabet shifts, ASCII kódy, hex konverzie

## Kľúčové otázky
1. Čo presne je "výsledok" ktorý sa má sčítať s 12?
2. Ako sa má interpretovať 'X' - ako marker, násobenie, alebo T9 kláves?
3. Aký je vzťah medzi číslami na markeroch a písmenami?

## Nájdený skrytý súbor: kluc.txt

V obrazok.jpg cez `strings` sa nachádza názov súboru **kluc.txt**!

**Obsah kluc.txt:**
```
.X.
.X.
..X
.X.
..X.
.X.
X..
```

**Analýza vzoru:**
- 7 riadkov (zodpovedá 7 písmenám PRIEVAN)
- X pozície: 2, 2, 3, 2, 3, 2, 1
- Rôzne dĺžky riadkov: 3, 3, 3, 3, 4, 3, 3
- Hint: 'X' ťa navedie na správnu stopu

**Číslo domu:** 581 (viditeľné na obrazok.jpg)

## Status
IN PROGRESS - analyzujem vzor z kluc.txt
