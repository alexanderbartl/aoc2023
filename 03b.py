from aocd import data, submit

lines = data.split('\n')

numbers = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char in '0123456789' and (x == 0 or line[x - 1] not in '0123456789'):
            for length in range(1, 100):
                if x + length == len(line) or line[x + length] not in '0123456789':
                    break
            surroundings = (line[x - 1] if x > 0 else '') + (line[x + length] if x + length < len(line) else '')
            if y > 0:
                surroundings += lines[y - 1][max(x - 1, 0):x + length + 1]
            if y < len(line) - 1:
                surroundings += lines[y + 1][max(x - 1, 0):x + length + 1]
            if '*' in surroundings:
                numbers.append({"number": int(line[x:x + length]), "x": x, "y": y, "length": length})

answer = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != '*':
            continue
        adjacent = [n["number"] for n in numbers if
                    n["x"] - 1 <= x <= n["x"] + n["length"] and n["y"] - 1 <= y <= n["y"] + 1]
        if len(adjacent) == 2:
            print('found gear at', x, y, adjacent)
            answer += adjacent[0] * adjacent[1]

print(answer)
submit(answer)
