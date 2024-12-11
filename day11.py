from collections import defaultdict

from aoc import get_input

line = [int(stone) for stone in get_input(day=11, as_list=False).split()]

counts = defaultdict(int)
for stone in line:
    counts[stone] += 1

for t in range(75):
    newcounts = defaultdict(int)
    for stone, count in counts.items():
        if stone == 0:
            newcounts[1] += count
        elif len(str(stone)) % 2 == 0:
            stonestr = str(stone)
            
            stone1 = int(stonestr[:len(stonestr) // 2])
            stone2 = int(stonestr[len(stonestr) // 2:])
            
            newcounts[stone1] += count
            newcounts[stone2] += count
        else:
            newcounts[stone*2024] += count
    counts = newcounts
    
    if t == 24 or t == 74:
        print(sum(counts.values()))