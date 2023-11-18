import re

with open('debug.txt') as f:
    data = f.read()

lines = data.split('\n')

numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]


def submit(value):
    print(f'would submit value {value}')
    pass
