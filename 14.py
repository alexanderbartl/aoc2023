from copy import copy

from aocd import data, submit

lines = data.split('\n')


def move_to_north_edge(lines):
    no_of_lines = len(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '.':
                for y2 in range(y, no_of_lines):
                    if lines[y2][x] == '#':
                        break
                    elif lines[y2][x] == 'O':
                        lines[y] = lines[y][:x] + 'O' + lines[y][x + 1:]
                        lines[y2] = lines[y2][:x] + '.' + lines[y2][x + 1:]
                        break
    return lines


def rotate(lines):
    return list(''.join(l) for l in zip(*reversed(lines)))


def calculate_weight(lines):
    return sum(line.count('O') * (len(lines) - y) for y, line in enumerate(lines))


def fingerprint(lines):
    return '\n'.join(lines)


print('part A:', calculate_weight(move_to_north_edge(copy(lines))))

previous_configurations_list = [fingerprint(lines)]
weights = [calculate_weight(lines)]
for i in range(1, 1_000_000_001):
    for direction in range(4):
        lines = move_to_north_edge(lines)
        lines = rotate(lines)
    if fingerprint(lines) in previous_configurations_list:
        cycle_start = previous_configurations_list.index(fingerprint(lines))
        cycle_length = i - cycle_start
        print('part B:', weights[cycle_start + (1_000_000_000 - cycle_start) % cycle_length])
        break
    weights.append(calculate_weight(lines))
    previous_configurations_list.append(fingerprint(lines))
