from collections import defaultdict
from itertools import combinations

from aoc import get_input


puzzle = get_input(day=8)
R, C = len(puzzle), len(puzzle[0])

antennas = defaultdict(set)
for r, row in enumerate(puzzle):
    for c, char in enumerate(row):
        if char != '.':
            antennas[char].add((r, c))

def nodes1(r_a, c_a, r_b, c_b):
    dr = r_b - r_a
    dc = c_b - c_a

    if int(dr) == dr and int(dc) == dc: 
        r_n1 = r_b + dr
        c_n1 = c_b + dc
        if 0 <= r_n1 < R and 0 <= c_n1 < C:
            yield r_n1, c_n1
        
        r_n2 = r_a - dr
        c_n2 = c_a - dc
        if 0 <= r_n2 < R and 0 <= c_n2 < C:
            yield r_n2, c_n2

def nodes2(r_a, c_a, r_b, c_b):
    dr = r_b - r_a
    dc = c_b - c_a

    for direction in (1, -1):
        i = 0
        r_n = r_b
        c_n = c_b
        while 0 <= r_n < R and 0 <= c_n < C:
            dr_step = direction * i * dr
            dc_step = direction * i * dc

            if int(dr_step) == dr_step and int(dc_step) == dc_step:
                r_n = r_b + dr_step
                c_n = c_b + dc_step
                if 0 <= r_n < R and 0 <= c_n < C:
                    yield r_n, c_n
            i += 1

antinodes1 = set()
antinodes2 = set()
for A in antennas.values():
    for (r_a, c_a), (r_b, c_b) in combinations(A, 2):
        antinodes1 |= set(nodes1(r_a, c_a, r_b, c_b))
        antinodes2 |= set(nodes2(r_a, c_a, r_b, c_b))
print(len(antinodes1))
print(len(antinodes2))
