import re

from aocd import data, submit

lines = data.split('\n')
numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]

print(data)
print(lines)
print(numbers)
