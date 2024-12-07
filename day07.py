from operator import add, mul

from aoc import get_input


puzzle = get_input(day=7)

def concat(a, b):
    return int(str(a)+str(b))

def dfs(numbers, operators, intermediate, ans):
    if not numbers:  # reached the bottom of the DFS
        return intermediate
    if intermediate > ans:  # all operators make things larger, so no use in continuing to search
        return float('inf')
    
    for op in operators:
        result = dfs(numbers[1:], operators, op(intermediate, numbers[0]), ans)
        if result == ans:
            return result
    return float('inf')

total1 = 0
total2 = 0
for line in puzzle:
    ans, operands = line.split(':')
    ans = int(ans)
    operands = [int(p) for p in operands.strip().split()]

    result = dfs(operands[1:], (mul, add), operands[0], ans)
    if result == ans:
        total1 += result

    result = dfs(operands[1:], (mul, add, concat), operands[0], ans)
    if result == ans:
        total2 += result
print(total1)
print(total2)
