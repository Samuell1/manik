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

**RIESENIE NAJDENE!**

**Analyza:**
- 7 pismenova vec ktora chyba v lampasi = SVIECKA (sviečka/candle)
- SVIECKA (7 pismen) → bez I = SVECKA (6 pismen)
- Dve slova z pismen S-V-E-C-K-A: **VEK** (vek/age) + **CAS** (čas/time)

**Prihlasovacie udaje pre /dielna/:**
- Meno: vek
- Heslo: cas

**Riesenie:** SVIECKA chyba v lampasi, bez I = SVECKA, slova VEK+CAS = prihlasovacie udaje

**Status:** COMPLETED

---

## Level 07
**URL:** https://manik.sk/hra/dielna/

**Autentifikacia:** vek / cas (HTTP Basic Auth)

**Popis:** Poriadne sa poobzeraj v tejto dielni

**Obrazok:** obrazok.jpg s image map (6 klikatelnych oblasti)

**Image map oblasti:**
- dielna.jpg (lightbox) - roh dielne so starou pieckou
- policka.jpg (lightbox) - policky s naradim
- okno.jpg (lightbox) - hrdzavy pant na okne
- skrinka.jpg (lightbox) - skrinka s naradim, viditelny SOLVEX
- ../pred_domom/ - vyzaduje dalsiu autentifikaciu
- pokracovanie.rar - zasifrovany RAR archiv

**Napoveda:**
- poriadne sa rozhliadni v tejto dielni
- zahryznuty zub casu je dolezity
- vysledok slovom je klucom k pokracovaniu

**Analyza RAR hesla:**
- "zahryznuty zub casu" = metafora pre plynutie casu
- Level 7 = SEDEM

**Heslo pre RAR:** sedem

**Obsah pokracovanie.txt:**
```
Aby si sa dostal z dielne von oknom budes
potrebovat dva nazvy produktov
v ktorych sa vyskytuje pismeno 'X'
```

**Produkty s X viditelne v obrazkoch:**
- SOLVEX (skrinka.jpg - modra plechovka)
- ??? (hladam druhy produkt)

**Skusene kombinacie pre /pred_domom/:**
- solvex + sikaflex, primalex, chemfix, bondex, unifix, ferex, akfix, murexin
- solvex + humorex, sonax, vertex, xerox, inox, nexus
- solvex + latex, flux, epoxy, wax, lux, dex, rex
- solvex + primax, naxos, oxidex, tyczka, toxol, tectyl
- Viacero stoviek kombinacii...

**Poznamky z obrazkov:**
- skrinka.jpg: SOLVEX viditelne (modra plechovka)
- dielna.jpg: SATLOOK (bez X), modra plynova flasa s moznym textom HUMOREX
- policka.jpg: tuby tmelov/silikonov (nezname znacky)
- Hlavny obrazok: sprejovacie plechovky na polici hore

**Dalsie skusene kombinacie:**
- humorex, humidex, humorek (mozny text na pravej strane dielna.jpg)
- Rozne znacky tmelov: sikaflex, chemfix, akfix, soudaflex
- Rozne znacky farieb: primalex, bondex, colorex
- Genericke slova: wax, fix, mix, box, latex, flux

**Status:** COMPLETED

**RIESENIE NAJDENE!**
- Produkt 1: **SOLVEX** (skrinka.jpg)
- Produkt 2: **HUMDREX** (dielna.jpg - text na pravej strane)
- Prihlasovacie udaje pre /pred_domom/: `solvex:humdrex`

---

## Level 08
**URL:** https://manik.sk/hra/pred_domom/

**Autentifikacia:** solvex / humdrex (HTTP Basic Auth)

**Popis:** Vyskocil si z dielne, zbadal si stareho suseda s dolezitymi informaciami

**Obrazok:** obrazok.jpg - scena zo slovenskej dediny, sused na zahrade

**Napoveda:**
- neznáme 'meno' suseda sa dozvieš zo súboru najbežnejšieho komprimovaného audio formátu (MP3)
- ďalšiu indíciu dostaneš preskúmaním nájdeného
- dôležitú informáciu použi na webe najčítanejších správ na Slovensku (SME.sk)
- sused a obec ťa odnavigujú ďalej

**Najdene subory:**
- meno.mp3 - obsahuje skryty text: "Meno suseda je heslo do suboru: ID.rar"
- ID.rar - zasifrovany archiv, heslo = meno suseda

**ID3 tagy v meno.mp3:**
- Title: Preskumaj
- Artist: Subor

**Status:** IN PROGRESS - hladam meno suseda pre ID.rar
