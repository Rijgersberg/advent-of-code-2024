from tqdm import tqdm

from aoc import get_input


puzzle = get_input(day=6)

map = set()
for c, line in enumerate(reversed(puzzle)):
    for r, char in enumerate(line):
        if char == '#':
            map.add(complex(real=r, imag=c))
        elif char == '^':
            start_pos = complex(real=r, imag=c)

R, C = len(puzzle), len(puzzle[0])
start_direction = 0 + 1j  # up

def play(map, pos, direction):
    history = {(pos, direction)}

    pos += direction
    while 0 <= pos.imag < R and 0 <= pos.real < C:
        if (pos, direction) in state:
            return 'loop'
        
        history.add((pos, direction))
        
        if pos + direction in map:
            direction *= 0 - 1j  # rotate 90 degrees right
        else:
            pos += direction
    return {pos for pos, _ in history}

# 6-1
print(len(play(map, start_pos, start_direction)))

# 6-2
loops = 0
for r in tqdm(range(R)):
    for c in range(C):
        new_map = map.copy()
        pos = complex(real=c, imag=r)

        if not pos in map and not pos == start_pos:
            new_map.add(pos)
            result = play(new_map, start_pos, start_direction)
            if result == 'loop':
                loops += 1
print(loops)
