import re

from aocd import data, submit

lines = data.split('\n')
LR = lines[0]

map_ = {line.split(' = ')[0]: line.split(' = ')[1].strip('()').split(', ') for line in lines[2:]}

steps = 0
current = 'AAA'
while True:
    current = map_[current][0 if LR[steps % len(LR)] == 'L' else 1]
    steps += 1
    if current == 'ZZZ':
        break

print(steps)
submit(steps)
