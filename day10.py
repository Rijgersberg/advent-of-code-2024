from functools import cache

from aoc import get_input


puzzle = get_input(day=10)
map = [[int(h) for h in row] for row in puzzle]
R, C = len(map), len(map[0])


trailheads = set()
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 0:
            trailheads.add((r, c))

def neighbors(r, c):
    for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        rn, cn = r+dr, c+dc
        if 0 <= rn < R and 0 <= cn < C:
            yield rn, cn

# 10-1
def dfs(r, c):
    visited.add((r, c))

    current = map[r][c]

    if current == 9:
        return {(r, c)}
    
    trailends = set()
    for rn, cn in neighbors(r, c):
        if (rn, cn) not in visited and map[rn][cn] - current == 1:
            trailends |= dfs(rn, cn)
    return trailends

total = 0
for r, c in trailheads:
    visited = set()
    trailends = dfs(r, c)
    total += len(trailends)
print(total)

# 10-2
@cache
def dfs2(r, c):
    current = map[r][c]

    if current == 9:
        return [[(r, c)]]
    
    trailends = []
    for rn, cn in neighbors(r, c):
        if map[rn][cn] - current == 1:
            for path in dfs2(rn, cn):
                trailends.append([(r, c)] + path)
    return trailends

print(sum(len(dfs2(r, c)) for r, c in trailheads))
