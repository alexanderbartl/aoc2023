from aocd import data, submit

lines = data.split('\n')

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

current = (0, 0)
trench = {current}
for line in lines:
    direction, steps, color = line.split(' ')
    for _ in range(int(steps)):
        current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
        trench.add(current)

min_x = min(x for x, y in trench)
max_x = max(x for x, y in trench)
min_y = min(y for x, y in trench)
max_y = max(y for x, y in trench)

# for y in range(min_y, max_y + 1):
#     for x in range(min_x, max_x + 1):
#         print('#' if (x, y) in trench else '.', end='')
#     print()

is_inside = False
total_area = len(trench)
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) in trench:
            if (x, y + 1) in trench:
                is_inside = not is_inside
            continue
        if is_inside:
            total_area += 1

submit(total_area)
