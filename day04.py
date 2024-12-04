import re

from aoc import get_input


puzzle = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

puzzle = get_input(day=4)

# 4-1
def search(puzzle, word, r, c, found, dr, dc):
    if not (0 <= r < len(puzzle) and 0 <= c < len(puzzle[0])):
        return False
    
    target = word[len(found)]
    
    if puzzle[r][c] == target:
        if found + target == word:
            return True
        else:
            return search(puzzle, word, r+dr, c+dc, found+target, dr, dc)
    else:
        return False


total = 0
for r in range(len(puzzle)):
    for c in range(len(puzzle[0])):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if (dr, dc) != (0, 0):
                    total += search(puzzle, "XMAS", r, c, '', dr, dc)
print(total)

# 4-2
crosses = ['M.M\n.A.\nS.S', 'M.S\n.A.\nM.S', 'S.M\n.A.\nS.M', 'S.S\n.A.\nM.M']
total = 0
for r in range(1, len(puzzle)-1):
    for c in range(1, len(puzzle[0])-1):
        candidate = f'{puzzle[r-1][c-1]}.{puzzle[r-1][c+1]}\n.{puzzle[r][c]}.\n{puzzle[r+1][c-1]}.{puzzle[r+1][c+1]}'
        candidate = re.sub(r'[^MAS\n]', '.', candidate)
        total += candidate in crosses
print(total)
