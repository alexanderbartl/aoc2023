from aocd import data, submit

lines = data.split('\n')

answer = 0
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
            if surroundings.strip('.'):
                answer += int(line[x:x + length])
submit(answer)
