from collections import defaultdict
from functools import cmp_to_key

from aoc import get_input


puzzle = get_input(day=5, as_list=False)
rulelines, updatelines = puzzle.split('\n\n')

rules = defaultdict(set)
for rule in rulelines.splitlines():
    first, second = [int(p) for p in rule.split('|')]
    rules[first].add(second)

def correct_order(update):
    for i, p in enumerate(update):
        for first in update[0:i]:
            if not p in rules[first]:
                return False
        for second in update[i+1:]:
            if not second in rules[p]:
                return False
    return True

score1 = 0
score2 = 0
for update in updatelines.splitlines():
    update = [int(p) for p in update.split(',')]

    if correct_order(update):
        score1 += update[len(update) // 2]
    else:
        fixed = sorted(update, key=cmp_to_key(
            lambda p1, p2: 1 if p2 in rules[p1] else -1))
        score2 += fixed[len(fixed) // 2]

print(score1)
print(score2)

