# Level 17 (Kamenista dolina)

**URL:** https://manik.sk/hra/kamenista_dolina/

## Prihlasovacie údaje
- **Username:** krcma
- **Password:** skodov

**Odkiaľ:** Level 16 - nápis "KRCMA u SKODOV" na plote v obci Sihla
- Odstránením malého 'u' → krcma:skodov

## Popis
"V krásnej doline .."

## HTML komentár
`<!-- mnoho z indicii su subory -->` - mnoho hintov sú súbory!

## Hinty
1. tentokrát buď veľmi obozretný
2. použi skúsenosti z predchádzajúcich levelov
3. niektoré veci využiješ viackrát
4. len jedna z možností je správna
5. vždy si rád pozeral videá
6. zišla by sa ti pomôcka
7. chýba ti dôležitý riadok
8. výsledok je postup do ďalšieho levelu

## Clickable areas
- **../na_vyhliadke/** (coords: 12, 299, 57, 346) - ďalší level

## Nájdené súbory

### obrazok.jpg
- Scéna z Kamenistej doliny
- Na konci súboru je ukrytý **YouTube video ID: 1hHcWSUxQB8**
- Nájdené cez `strings obrazok.jpg | tail`

### pomocka (Base64)
- Súbor: `https://manik.sk/hra/kamenista_dolina/pomocka`
- Po dekódovaní z Base64 obsahuje vzor z bodiek:
```
*****************************************************
*                                                   *
*                     .......                       *
*                ........... ......                 *
*                                                   *
* .......... ........... ... .. ...... ..... ...    *
* ........ ...... . ........ ......... ..... .....  *
* ...... ....... ... ...                            *
*                                                   *
* ............. . ............. ........ .......    *

*                                                   *
*                        S..... O...... P...... SR  *
*                                                   *
*****************************************************
```
- Šablóna na konci: S..... O...... P...... SR
- Bodky pravdepodobne reprezentujú nejaký kód alebo písmená

### riadok (RAR archív) ✓ ROZŠIFROVANÉ
- Súbor: `https://manik.sk/hra/kamenista_dolina/riadok`
- Má poškodený header (00 00 00 00 namiesto "Rar!")
- Po oprave prvých 4 bajtov na 52 61 72 21 → RAR archív
- **Heslo:** `1hHcWSUxQB8` (YouTube video ID z obrazok.jpg!)
- **Obsah rozšifrovaného súboru:**
```
*   4 3      9      1    6    7   2   8      5      *
```
- Toto je "chýbajúci riadok" z pomocka šablóny!
- Čísla 4, 3, 9, 1, 6, 7, 2, 8, 5 = permutácia čísel 1-9
- Pravdepodobne inštrukcie na preusporiadanie alebo výber písmen

## YouTube video analýza

### Video info
- **ID:** 1hHcWSUxQB8
- **Názov:** Meandre Kamenistého Potoka
- **Kanál:** Mnk (@MnkFcbk)
- **Dĺžka:** 7:32
- **Dátum:** 31.12.2013

### Popis kanála
`.. pisces mortui solum cum flumine natant ..`
- Latinská fráza: "Mŕtve ryby len plávajú s prúdom"
- Možný hint pre heslo alebo credentials

## Interpretácia šablóny S..... O...... P...... SR

Možné významy:
1. **ŠOP SR** = Štátna ochrana prírody Slovenskej republiky
   - Meandre Kamenistého potoka je chránený areál pod CHKO Poľana
2. **Prvé písmená slov** z nejakej frázy
3. **Slová začínajúce na S, O, P** + skratka SR

## Kamenistá dolina - geografické info
- 25 km dlhá dolina s Kamenistým potokom
- Chránený areál: Meandre Kamenistého potoka (2.5 km)
- Vodná nádrž Hronček v strede doliny
- Prístup z obcí Sihla alebo Hronec
- Lesná železnička v minulosti
- Tunelom točitých schodov z hrádze nádrže

## Ďalší level
- **URL:** https://manik.sk/hra/na_vyhliadke/
- **Status:** 401 - vyžaduje auth

## Analýza riadku

Čísla z riadku: **4 3 9 1 6 7 2 8 5**

Toto je permutácia 1-9. Možné interpretácie:
1. **Pozície písmen** - vybrať N-té písmeno z 9-písmenového slova
2. **Preusporiadanie** - preskupiť 9 písmen podľa tejto postupnosti
3. **Výber slov** - vybrať slová z pomocka šablóny

### Pomocka štruktúra (dĺžky slov):
- Riadok 3: 7 = "Meandre"
- Riadok 4: 11+6 = "Kamenisteho Potoka"
- Riadok 6: 10+11+3+2+6+5+3 (7 slov)
- Riadok 7: 8+6+1+8+9+5+5 (7 slov)
- Riadok 8: 6+7+3+3 (4 slová)
- Riadok 10: 13+1+13+8+7 (5 slov)
- Riadok 13: S(6) O(7) P(7) SR(2) = "Statna Ochrana Prirody SR"

### Testované 9-písmenové slová:
- KAMENISTY → pozície 4,3,9,1,6,7,2,8,5 = EMYKISATN ❌
- VYHLIADKE → pozície 4,3,9,1,6,7,2,8,5 = LHEVADYKI ❌

### Potrebné:
- Zistiť presný text na informačnej tabuli z YouTube videa
- Screenshot z videa obsahuje túto tabuľu

## Status
**IN PROGRESS** - RAR rozšifrovaný, čakám na text z tabule vo videu
