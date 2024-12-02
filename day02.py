from aoc import get_input


def monotonic(values):
    return (all(v2 >= v1 for v1, v2 in zip(values[:-1], values[1:])) or
        all(v2 <= v1 for v1, v2 in zip(values[:-1], values[1:])))

def maxdiff(values, minimum, maximum):
    return all(minimum <= abs(v1 - v2) <= maximum
               for v1, v2 in zip(values[:-1], values[1:]))

# 2-1
safe = 0
for row in get_input(day=2):
    report = [int(v) for v in row.split()]

    if monotonic(report) and maxdiff(report, minimum=1, maximum=3):
        safe += 1
print(safe)

# 2-2
safe = 0
for row in get_input(day=2):
    report = [int(v) for v in row.split()]

    for i in range(len(report)):
        dampened_report = report[:]
        del dampened_report[i]

        if monotonic(dampened_report) and maxdiff(dampened_report, minimum=1, maximum=3):
            safe += 1
            break
print(safe)
