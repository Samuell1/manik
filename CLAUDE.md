# HRA by MNK - Slovak Puzzle Game

## What This Is
A Slovak online puzzle adventure game ("psychodventura") at https://manik.sk/hra/

The game consists of multiple levels, each requiring solving puzzles to find URLs and authentication credentials to progress.

## Goal
Solve all levels of the puzzle game and document progress.

## Folder Structure
```
/home/user/manik/
├── claude.md          - This file (project overview)
├── GAME_PROGRESS.md   - Detailed progress, solutions, and current status
└── levels/            - Downloaded assets and analysis per level
    ├── 10/            - Level 10 files
    └── 11/            - Level 11 files (current)
```

## Where To Find Information
- **Current progress & status**: See `GAME_PROGRESS.md`
- **Level-specific analysis**: See `levels/<number>/README.md`
- **Downloaded images/files**: See `levels/<number>/`

## Game Rules
- No diacritics in answers
- No spaces (use - or _)
- All levels on manik.sk/hra/
- Passwords should not be cracked/hacked

## DÔLEŽITÉ: Analýza obrázkov
Pri každom obrázku VŽDY skontroluj:
1. **Vizuálne** - čo je viditeľné na obrázku (čísla, text, vzory)
2. **Strings/kód** - `strings obrazok.jpg` pre skryté textové dáta
3. **Metadáta** - EXIF, komentáre, autor
4. **Skryté súbory** - názvy súborov môžu byť skryté v obrazku (napr. "kluc.txt")
5. **Koniec súboru** - možné pripojené dáta za obrazkom
6. **HTML kód stránky** - image mapy, komentáre, entity

## DÔLEŽITÉ: Commitovanie
- Pri každom dôležitom zistení COMMITUJ zmeny
- Ukladaj progress priebežne, nie len na konci
- Dokumentuj nájdené skryté súbory a kľúče v README.md pre daný level

## DÔLEŽITÉ: Použitie výsledkov hádaniek
- Keď nájdeš výsledok z hádanky, ZAMYSLI SA ako ho použiť
- Výsledok môže byť:
  - Inštrukcia (napr. "LATINSKY" = prelož do latinčiny)
  - Kľúč k ďalšej šifre
  - Časť username:password kombinácie
  - Hint na ďalší krok
- Nikdy nepredpokladaj, že výsledok je priamo URL - analyzuj jeho VÝZNAM

## DÔLEŽITÉ: Testovanie kombinácií
- Pri hľadaní username:password skúšaj VŠETKY kombinácie medzi relevantnými slovami
- Vytvor zoznam kandidátov (výsledky šifier, preklady, synonymá, súvisiace slová)
- Systematicky testuj: slovo1:slovo2, slovo2:slovo1 pre každú dvojicu
- Testuj aj s číslami levelu, reverzné slová, a variácie bez diakritiky

## Context Files (auto-load)
@GAME_PROGRESS.md
@levels/13/README.md
