import re

from aocd import data, submit

lines = data.split('\n')
start_y = [i for i, line in enumerate(lines) if 'S' in line][0]
start_x = lines[start_y].index('S')

distances = {(start_x, start_y): 0}
queue = [(start_x, start_y)]

while queue:
    x, y = queue.pop(0)
    distance = distances[(x, y)]
    if distance == 64:
        break
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (x + dx, y + dy) in distances:
            continue
        try:
            if lines[y + dy][x + dx] == '#':
                continue
        except IndexError:
            continue
        distances[(x + dx, y + dy)] = distance + 1
        queue.append((x + dx, y + dy))

submit(len([d for d in distances.values() if d % 2 == 0]))
