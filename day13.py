import re

from scipy.optimize import linprog
import numpy as np

from aoc import get_input

puzzle = get_input(day=13, as_list=False)

pattern = re.compile(r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)""")
total = 0
for machine in puzzle.split('\n\n'):
    A_x, A_y, B_x, B_y, prize_x, prize_y = map(int, re.fullmatch(pattern, machine).groups())

    min_score = float('inf')
    for i in range(101):
        for j in range(101):
            if (i*A_x + j*B_x, i*A_y + j*B_y) == (prize_x, prize_y):
                score = 3*i + j
                min_score = min(score, min_score)
    if min_score != float('inf'):
        total += min_score
print(total)


# 13-2
total = 0
for i, machine in enumerate(puzzle.split('\n\n')):
    A_x, A_y, B_x, B_y, prize_x, prize_y = map(int, re.fullmatch(pattern, machine).groups())

    prize_x += 10000000000000
    prize_y += 10000000000000

    res = linprog(c=[3, 1], A_eq=[[A_x, B_x],[A_y, B_y]], b_eq=[prize_x, prize_y])

    if res.x is not None:
        a, b = res.x.astype(np.int64)

        N = 2  # correct floating point to int inaccuracies
        for i in range(a-N, a+N):
            for j in range(b-N, b+N):
                if i*A_x + j*B_x == prize_x and i*A_y + j*B_y == prize_y:
                    total += 3*i + j
                    continue
print(total)
