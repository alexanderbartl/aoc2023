from sys import setrecursionlimit

from aocd import data, submit

setrecursionlimit(100_000)
lines = data.split('\n')


def propagate(x, y, direction, travelled_=None):
    travelled = set() if travelled_ is None else travelled_
    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]):
        return
    if (x, y, direction) in travelled:
        return
    travelled.add((x, y, direction))
    if lines[y][x] == '.':
        if direction == 'U':
            propagate(x, y - 1, 'U', travelled)
        elif direction == 'D':
            propagate(x, y + 1, 'D', travelled)
        elif direction == 'L':
            propagate(x - 1, y, 'L', travelled)
        elif direction == 'R':
            propagate(x + 1, y, 'R', travelled)
    elif lines[y][x] == '\\':
        if direction == 'U':
            propagate(x - 1, y, 'L', travelled)
        elif direction == 'D':
            propagate(x + 1, y, 'R', travelled)
        elif direction == 'L':
            propagate(x, y - 1, 'U', travelled)
        elif direction == 'R':
            propagate(x, y + 1, 'D', travelled)
    elif lines[y][x] == '/':
        if direction == 'U':
            propagate(x + 1, y, 'R', travelled)
        elif direction == 'D':
            propagate(x - 1, y, 'L', travelled)
        elif direction == 'L':
            propagate(x, y + 1, 'D', travelled)
        elif direction == 'R':
            propagate(x, y - 1, 'U', travelled)
    elif lines[y][x] == '-':
        if direction == 'L':
            propagate(x - 1, y, 'L', travelled)
        elif direction == 'R':
            propagate(x + 1, y, 'R', travelled)
        elif direction == 'U' or direction == 'D':
            propagate(x - 1, y, 'L', travelled)
            propagate(x + 1, y, 'R', travelled)
    elif lines[y][x] == '|':
        if direction == 'U':
            propagate(x, y - 1, 'U', travelled)
        elif direction == 'D':
            propagate(x, y + 1, 'D', travelled)
        elif direction == 'L' or direction == 'R':
            propagate(x, y - 1, 'U', travelled)
            propagate(x, y + 1, 'D', travelled)

    return len(set((x, y) for x, y, direction in travelled)) if travelled_ is None else None


print('Part A', propagate(0, 0, 'R'))
print('Part B', max(
    max(propagate(0, y, 'R') for y in range(len(lines))),
    max(propagate(x, 0, 'D') for x in range(len(lines[0]))),
    max(propagate(len(lines[0]) - 1, y, 'L') for y in range(len(lines))),
    max(propagate(x, len(lines) - 1, 'U') for x in range(len(lines[0]))),
))
