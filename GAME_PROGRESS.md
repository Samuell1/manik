# HRA by MNK - Postup hrou

## Pravidla hry
- Nie je kompatibilna s mobilnymi zariadeniami
- Urcena len pre pokrocilych uzivatelov so znalostou HTML
- Vsetky udaje sa pisu BEZ diakritiky
- Nepouzivaju sa medzery, ale mozu byt pouzite pomlcky alebo "_" znaky
- Vsetky levely su na domene http://manik.sk/hra/
- Hesla sa nemaju crackovat ani hackovat

## Tipy
- Starostlivo studujte vsetky indicie viackrat
- Indicie mozu byt metafory
- Nie vsetko je viditelne na prvy pohlad
- Niektore slova z indicii mozu byt nazvy suborov na stiahnutie
- Kazdy level je riesitelny logickym myslenim

---

## Level 01
**URL:** https://manik.sk/hra/level_01/

**Popis:** Nachadzas sa pred pivnicou, kde ma ulozene archivne vino..

**Obrazok:** obrazok.jpg

**Napoveda:** kliknutim na klucovu dierku sa dostanes do druheho levelu

**Riesenie:** Klucova dierka v obrazku vedie na level_02/

**Status:** COMPLETED

---

## Level 02
**URL:** https://manik.sk/hra/level_02/

**Popis:** Zmizli vsetky flase a jedine, co ti zostalo je najstarsi sud.

**Obrazok:** obrazok.jpg

**Napoveda:** Poriadne sa v pivnici poobzeraj a zisti kto ti archivne vinko zobral

**Riesenie:** Na stene pivnice je napis "Petra" - treba ist na /petra/

**Status:** COMPLETED

---

## Level 03
**URL:** https://manik.sk/hra/petra/

**Popis:** Petra, ktorej si veril, ze sa ti postara o tvoju pivnicu ta pekne sklamala

**Obrazok:** obrazok.jpg (fotka)

**Napoveda:** Na tejto fotke nie je vsetko uplne v poriadku, mozno ma zlu hlavicku

**Hint:** "Zla hlavicka" = v obrazku je skryta informacia o zahrade

**Riesenie:** Treba ist na /zahrada/

**Status:** COMPLETED

---

## Level 04
**URL:** https://manik.sk/hra/zahrada/

**Popis:** Petra sa uz dlhsi cas nenachadza na svojej zahrade, ale ma tu zaparkovane auto

**Obrazok:** obrazok.jpg

**Napoveda:**
- Cislo levelu je dolezite
- Spravna kombinacia umoznuje vstup do 5. levelu

**Subor:** /zahrada/vino4.txt (cislo 4 = cislo levelu)

**Prihlasovacie udaje:**
- Meno: otvor
- Heslo: dvere

**Riesenie:** Najst subor vino4.txt, ziskat prihlasovacie udaje, ist na /v_dome/

**Status:** COMPLETED

---

## Level 05
**URL:** https://manik.sk/hra/v_dome/

**Autentifikacia:** otvor / dvere (HTTP Basic Auth)

**Popis:** Dom je prazdny, ale oplatilo by sa dobre preskumat kuchynu

**Obrazok:** obrazok.jpg s image map (5 klikatelnych oblasti)

**Obrazky:** 1.jpg, 2.jpg, 3.jpg, 4.jpg - normalne fotky
**Skryty subor:** 5.jpg - je to RAR archiv (zasifrovaný)

**Image map detail:**
- 5.jpg ma rel="zeby_tu?" - hint na riesenie

**Napoveda:**
- prezrel by som vsetko radsej dva krat
- spravne slovo je klucom ku pokracovaniu

**RIESENIE NAJDENE!**

**Pismena skryte v obrazkoch:**
- 1.jpg: **N** (v lavom hornom rohu - popolnik s cigaretami)
- 2.jpg: **I** (v lavom hornom rohu - stara zehlicka)
- 3.jpg: **V** (v lavom hornom rohu - zehlicka na uhlie)
- 4.jpg: **O** (v lavom hornom rohu - sedadlo bicykla)

**Heslo pre RAR:** VINO (pismena v poradi 3-2-1-4 alebo NIVO preusporiadane)

**Obsah RAR archivu:** pokracovanie.txt

**Riesenie:** Heslo "vino" otvori RAR archiv, obsahuje subor pokracovanie.txt

**Obsah pokracovanie.txt:**
```
http://manik.sk/hra/lampas/
```

**Status:** COMPLETED

---

## Level 06
**URL:** https://manik.sk/hra/lampas/

**Obrazok:** Stary kovovy lampas (bez svetla)

**Popis:** Na chodbe nesvieti svetlo, lampa je nepouzitelna

**Link:** Obrazok linkuje na /dielna/ (vyžaduje autentifikáciu)

**Napoveda:**
- zo 7 pismenovej veci, ktora tu ocividne chyba vyskrtni pismeno "I"
- poskladanim dvoch spravnych slov z ostatnych pismen sa dostanes do dielne

**Analyza:**
- 7 pismenova vec = LAMPION (L-A-M-P-I-O-N)
- Bez I = LAMPON (L-A-M-P-O-N) = 6 pismen
- Mozne 2 slova: PAN + LOM, MOL + PAN, NAP + LOM...

**Skusene kombinacie:** pan:lom, lom:pan, mol:pan, pan:mol, nap:lom

**Status:** IN PROGRESS - hladam spravne prihlasovacie udaje
