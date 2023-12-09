import re

from aocd import data, submit

lines = data.split('\n')
numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

answer = 0
for line in numbers:
    levels = [line]
    while any(x != 0 for x in levels[-1]):
        levels.append([levels[-1][x] - levels[-1][x - 1] for x in range(1, len(levels[-1]))])
    levels.reverse()
    for i, level in enumerate(levels):
        if i == 0:
            level.append(0)
        else:
            level.append(level[-1] + levels[i - 1][-1])
    answer += levels[-1][-1]

submit(answer)
