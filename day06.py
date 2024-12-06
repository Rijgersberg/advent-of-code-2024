from copy import deepcopy
from collections import defaultdict

from tqdm import tqdm

from aoc import get_input


puzzle = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

puzzle = get_input(day=6)

map = {}
for c, line in enumerate(reversed(puzzle)):
    for r, char in enumerate(line):
        if char == '#':
            map[complex(real=r, imag=c)] = char
        elif char == '^':
            start_pos = complex(real=r, imag=c)

start_direction = 0 + 1j
R, C = len(puzzle), len(puzzle[0])

def play(map, pos, direction):
    visited = {pos}
    state = {(pos, direction)}

    pos += direction

    while 0 <= pos.imag < R and 0 <= pos.real < C:
        if (pos, direction) in state:
            return 'loop'
        
        visited.add(pos)
        state.add((pos, direction))
        
        if map.get(pos + direction, '') == '#':
            direction *= 0 - 1j  # rotate 90 degrees right
        else:
            pos += direction
    return visited

# 6-1
print(len(play(map, start_pos, start_direction)))

# 6-2
loops = 0
for r in tqdm(range(R)):
    for c in range(C):
        new_map = deepcopy(map)
        pos = complex(real=c, imag=r)

        if not new_map.get(pos, '') == '#' and not pos == start_pos:
            new_map[pos] = '#'
            result = play(new_map, start_pos, start_direction)
            if result == 'loop':
                loops += 1
print(loops)
