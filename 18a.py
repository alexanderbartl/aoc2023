from aocd import data, submit

lines = data.split('\n')

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

current = (0, 0)
trench = [current]
for line in lines:
    direction, steps, color = line.split(' ')
    for _ in range(int(steps)):
        current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
        trench.append(current)

min_x = min(x for x, y in trench)
max_x = max(x for x, y in trench)
min_y = min(y for x, y in trench)
max_y = max(y for x, y in trench)

outside = set([(x, min_y) for x in range(min_x, max_x + 1) if (x, min_y) not in trench]
              + [(x, max_y) for x in range(min_x, max_x + 1) if (x, max_y) not in trench]
              + [(min_x, y) for y in range(min_y, max_y + 1) if (min_x, y) not in trench]
              + [(max_x, y) for y in range(min_y, max_y + 1) if (max_x, y) not in trench])
visited = set()
while len(outside) > len(visited):
    current = next(p for p in outside if p not in visited)
    visited.add(current)
    for direction in directions.values():
        new = (current[0] + direction[0], current[1] + direction[1])
        if new not in visited and new not in trench and min_x <= new[0] <= max_x and min_y <= new[1] <= max_y:
            outside.add(new)

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print('#' if (x, y) in trench else '.' if (x, y) in outside else '+', end='')
    print()

total_area = (max_x + 1 - min_x) * (max_y + 1 - min_y)

submit(total_area - len(outside))
