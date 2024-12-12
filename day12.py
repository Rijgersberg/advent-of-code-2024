from aoc import get_input

puzzle = get_input(day=12)

R, C = len(puzzle), len(puzzle[0])
def neighbors(r, c):
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc

def dfs(plant, r, c):
    if (r, c) in visited:
        return set()
    if puzzle[r][c] != plant:
        return set()
    
    visited.add((r, c))
    region = {(r, c)}

    for nr, nc in neighbors(r, c):
        region |= dfs(plant, nr, nc)
    return region

def perimeter(plants):
    edges = set()
    for r, c in plants:
        for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            edges.add((r, c, direction))
    
    perim = set()
    for r, c, (dr, dc) in edges:
        if (r+dr, c+dc, (-dr, -dc)) not in edges:
            perim.add((r, c, (dr, dc)))
    return perim

# 12-2
def segments(perim):
    segs = []

    while perim:
        r, c, (dr, dc) = perim.pop()
        segs.append((r, c, (dr, dc)))
  
        if dc in (-1, 1):  # vertical fence
            for rn in range(r+1, R):
                neighbor = (rn, c, (dr, dc))
                if neighbor in perim:
                    perim -= {neighbor}
                else:
                    break  # segment ended
            for rn in range(r-1, -1, -1):
                neighbor = (rn, c, (dr, dc))
                if neighbor in perim:
                    perim -= {neighbor}
                else:
                    break  # segment ended

        elif dr in (-1, 1):  # horizontal fence
            for cn in range(c+1, C):
                neighbor = (r, cn, (dr, dc))
                if neighbor in perim:
                    perim -= {neighbor}
                else:
                    break  # segment ended
            for cn in range(c-1, -1, -1):
                neighbor = (r, cn, (dr, dc))
                if neighbor in perim:
                    perim -= {neighbor}
                else:
                    break  # segment ended
    return segs

visited = set()
price1 = 0
price2 = 0
for r, row in enumerate(puzzle):
    for c, plant in enumerate(row):
        area = dfs(plant, r, c)
        perim = perimeter(area)
        price1 += len(area) * len(perim)
        
        segs = segments(perim)
        price2 += len(area) * len(segs)
print(price1, price2)
