from collections import Counter

from aoc import get_input


rows = [(int(id) for id in row.split())
        for row in get_input(day=1)]
l1, l2 = (list(l) for l in zip(*rows))

l1.sort()
l2.sort()

# 1-1
print(sum(abs(id2 - id1) for id1, id2 in zip(l1, l2)))

# 1-2
counts = Counter(l2)
print(sum(v1 * counts[v1] for v1 in l1))
