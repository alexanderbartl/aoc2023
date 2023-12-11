from aocd import data

lines = data.split('\n')

empty_lines = [i for i, line in enumerate(lines) if line == '.' * len(line)]
empty_columns = [j for j in range(len(lines[0])) if all(line[j] == '.' for line in lines)]
galaxies = [(x, y) for y, line in enumerate(lines) for x, char in enumerate(line) if char == '#']

distance_a = distance_b = 0
for g1 in galaxies:
    for g2 in galaxies:
        empty_space = len([l for l in empty_lines if min(g1[1], g2[1]) < l < max(g1[1], g2[1])]) + \
                      len([c for c in empty_columns if min(g1[0], g2[0]) < c < max(g1[0], g2[0])])
        distance_a += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]) + empty_space
        distance_b += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]) + 999_999 * empty_space

print(distance_a // 2, distance_b // 2)
