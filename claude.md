# HRA by MNK - Slovak Puzzle Game

## What This Is
A Slovak online puzzle adventure game ("psychodventura") at https://manik.sk/hra/

The game consists of multiple levels, each requiring solving puzzles to find URLs and authentication credentials to progress.

## Current Status
- **Levels 1-10**: SOLVED
- **Level 11**: IN PROGRESS - stuck on /na_lazoch/ authentication

## Files
- `GAME_PROGRESS.md` - Detailed solutions and progress for all levels
- `levels/` - Downloaded assets and analysis for each level

## What Needs To Be Done

### Level 11 - SALTO 15 Puzzle
- **URL**: /1464928/
- **Next**: /na_lazoch/ (requires auth, returns 401)
- **Hint**: "Racing car digits indicate position of unnecessary letters of the racer himself"
- **Key elements**: Car with "SALTO 15", numbers decode to "drak" (dragon)
- **Main theory**: SALTO minus positions 1,5 = ALT
- **Problem**: 500+ combinations tested, none work

### Possible Approaches
1. Research Slovak motorsport for "SALTO" reference
2. Find hidden files on Level 11
3. Complete Level 9 "two laz" puzzle first (mentioned as connected)
4. Different interpretation of "závodník" (racer)
5. Look for hidden text in image

## Game Rules
- No diacritics in answers
- No spaces (use - or _)
- All levels on manik.sk/hra/
- Passwords should not be cracked/hacked

## Key Patterns in This Game
1. Hidden text in images
2. Hex/file header manipulation
3. Periodic table encoding (Level 10: KRAL FRANTISEK)
4. Letter position removal (Level 11: digits indicate positions)
5. External website references (SME.sk)
6. Word puzzles and anagrams
