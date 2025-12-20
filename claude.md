# HRA by MNK - Complete Game Progress

## Game Overview
- **URL**: https://manik.sk/hra/
- **Type**: Slovak online puzzle adventure ("psychodventura")
- **Rules**: No diacritics, no spaces (use - or _), all levels on manik.sk/hra/

---

## Completed Levels

### Level 01 → /level_01/
- Click keyhole in image → /level_02/

### Level 02 → /level_02/
- Find "Petra" text on wall → /petra/

### Level 03 → /petra/
- "Bad header" hint → /zahrada/

### Level 04 → /zahrada/
- File: vino4.txt
- **Auth**: `otvor:dvere` → /v_dome/

### Level 05 → /v_dome/
- Hidden letters in images: N, I, V, O → password "VINO" for RAR
- RAR contains: pokracovanie.txt → /lampas/

### Level 06 → /lampas/
- Missing item: SVIECKA (candle, 7 letters)
- Remove I → SVECKA → words VEK + CAS
- **Auth**: `vek:cas` → /dielna/

### Level 07 → /dielna/
- RAR password: "sedem" (level 7)
- Find products with X: SOLVEX + HUMDREX
- **Auth**: `solvex:humdrex` → /pred_domom/

### Level 08 → /pred_domom/
- meno.mp3 → ID.rar (password: "dominik")
- SME.sk article c/4868666 → village Rykynčice, Ing. Zoltán Kafka

### Level 09 → /do_dediny/
- **Auth**: `sever:juh` (navigation = cardinal directions)
- HTML comment: `<!-- Wiktória je kamarátka -->`
- Image number: 383935303445343437 → ASCII "89504E447" (corrupted PNG header)
- Hints mention: "two laz" will give access to next level

### Level 10 → /kopec/
- KRAL FRANTISEK = periodic table elements
- Kr(36) Al(13) F(9) Ra(88) N(7) Ti(22) Se(34) K(19) = **36139887223419**
- File: 36139887223419.ne → use "rychlejsie" (last word of Kafka's description)
- rychlejsie → hex → digits → first 6 + last 6 = **1464928**

---

## Level 11 - UNSOLVED

### URL
https://manik.sk/hra/1464928/

### Next Level
https://manik.sk/hra/na_lazoch/ (requires auth - returns 401)

### Image Contents
- Rusty Škoda wagon with "SALTO 15" on door
- Red pipe wrench (clickable → /na_lazoch/)
- Numbers scattered:
  - 42 64 677 7
  - 36 248 216 37
  - 92 100 135 77 (sum = 404!)
  - 122 65 51 123
  - **100 114 97 107 = ASCII "drak"** (dragon)
  - Ho 292 987 3

### Hint
"Číslice závodného auta označujú poradie nepotrebných písmen samotného závodníka"
(The racing car digits indicate the position of unnecessary letters of the racer himself)

### Main Interpretation
- Car has "SALTO 15"
- Digits = 1 and 5
- SALTO: S(1) A(2) L(3) T(4) O(5)
- Remove positions 1,5 → S and O removed → **ALT**

### Key Discoveries
1. **DRAK**: 100 114 97 107 = ASCII "drak" (dragon)
2. **KARD**: Reversed = 107 97 114 100 = "kard" (sword in Hungarian)
3. **KOD**: SKODA → remove 1,5 = "kod" (code in Slovak)
4. **RAK**: DRAKA → remove 1,5 = "rak" (crab in Slovak)
5. **AFK**: KAFKA → remove 1,5 = "afk"

### Tested Combinations (500+, all 401)
```
salto:alt, alt:salto, drak:alt, alt:drak
skoda:kod, kod:skoda
kafka:afk, zoltan:oltn
zavodnik:avonik
drak:rak, draka:rak, rak:drak
hasak:asa (wrench transformation)
homola:omoa (Slovak racing driver)
lazy:alt, laz:alt, lazoch:alt
dominik:alt, wiktoria:alt, rykyncice:alt
All Slovak car models, racing terms, surnames
All description words with 1,5 rule
```

### Possible Missing Pieces
1. Specific Slovak motorsport/cultural reference
2. Hidden file on Level 11 not yet found
3. Level 9 "two laz" puzzle connection
4. Different interpretation of "závodník" (racer)
5. Something hidden in the image

---

## Key Patterns Used in This Game

1. **Hidden text in images** (Levels 2, 5)
2. **File headers/hex manipulation** (Level 3, 9)
3. **Numbered files** (Level 4: vino4.txt)
4. **Word puzzles** (Level 6: SVIECKA → VEK:CAS)
5. **Product names in images** (Level 7: SOLVEX, HUMDREX)
6. **External websites** (Level 8: SME.sk)
7. **Periodic table encoding** (Level 10: KRAL FRANTISEK)
8. **Hex conversion** (Level 10: rychlejsie → hex)
9. **Letter position removal** (Level 11: SALTO 15 → ALT)

---

## Files Structure
```
/home/user/manik/
├── claude.md (this file)
├── GAME_PROGRESS.md
└── levels/
    ├── 10/
    │   ├── 36139887223419.ne
    │   └── kafka_tabulka.md
    └── 11/
        ├── README.md
        ├── obrazok.jpg
        └── page.html
```

---

## Next Steps for Level 11
1. Research Slovak racing history for "SALTO" reference
2. Look for hidden files with different naming patterns
3. Try Level 9 puzzle completion first ("two laz" hint)
4. Analyze image more carefully for hidden text
5. Consider that "závodník" might be a specific person's name
