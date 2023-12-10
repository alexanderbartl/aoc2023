import re

from aocd import data, submit

lines = data.split('\n')

start = [(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == 'S'][0]
visited = ({start}, {start})

paths = ([start], [start])
while paths[0][-1] != paths[1][-1] or len(visited[0]) == 1:
    for i, path in enumerate(paths):
        x, y = path[-1]
        candidates = []
        if lines[y][x] == '|':
            candidates = [(x, y - 1), (x, y + 1)]
        elif lines[y][x] == '-':
            candidates = [(x - 1, y), (x + 1, y)]
        elif lines[y][x] == 'L':
            candidates = [(x + 1, y), (x, y - 1)]
        elif lines[y][x] == 'J':
            candidates = [(x - 1, y), (x, y - 1)]
        elif lines[y][x] == 'F':
            candidates = [(x + 1, y), (x, y + 1)]
        elif lines[y][x] == '7':
            candidates = [(x - 1, y), (x, y + 1)]
        elif lines[y][x] == 'S':
            if lines[y - 1][x] in '|F7':
                candidates.append((x, y - 1))
            if lines[y + 1][x] in '|LJ':
                candidates.append((x, y + 1))
            if lines[y][x - 1] in '-LF':
                candidates.append((x - 1, y))
            if lines[y][x + 1] in '-J7':
                candidates.append((x + 1, y))
            candidates = candidates[i:i + 1]
        path.append([c for c in candidates if c not in visited[i]][0])
        visited[i].add(path[-1])

print(len(paths[0]) - 1)
# submit(len(paths[0]) - 1)

answer_b = 0
inside = False
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if (x, y) in paths[0] or (x, y) in paths[1]:
            if lines[y][x] in '|F7':
                inside = not inside
            print(lines[y][x], end='')
        else:
            if inside:
                answer_b += 1
                print('I', end='')
            print(' ', end='')
    print()

print(answer_b)
submit(answer_b)
