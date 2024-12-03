import re

from aoc import get_input


memory = get_input(day=3, as_list=False)

# 3-1
pattern = r'(mul)\((\d+)\,(\d+)\)'
print(sum(int(operand1) * int(operand2) for operator, operand1, operand2 in 
          re.findall(pattern, memory)))

# 3-2
total = 0
enabled = True
pattern = r'((mul)\((\d+)\,(\d+)\))|(do\(\))|(don\'t\(\))'
for _, operator, operand1, operand2, do, dont in re.findall(pattern, memory):
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif enabled:
        total += int(operand1) * int(operand2)
print(total)
