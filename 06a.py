import re

from aocd import data, submit

lines = data.split('\n')
numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

answer = 1
for race in range(len(numbers[0])):
    duration, record = numbers[0][race], numbers[1][race]
    options = 0
    for time in range(1, duration):
        distance = time * (duration - time)
        if distance > record:
            options += 1
    answer *= options

submit(answer)
