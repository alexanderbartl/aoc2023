from aocd import data, submit


def get_pattern_score(pattern, exclude=None):
    for i in range(1, len(pattern)):
        if pattern[max(0, 2 * i - len(pattern)):i] == list(reversed(pattern[i:2 * i])):
            if i * 100 != exclude:
                return i * 100
    pattern = list(zip(*pattern))
    for i in range(1, len(pattern)):
        if pattern[max(0, 2 * i - len(pattern)):i] == list(reversed(pattern[i:2 * i])):
            if i != exclude:
                return i


answer = 0
for pattern in data.split('\n\n'):
    original_score = get_pattern_score(pattern.split('\n'))
    for i in range(len(pattern)):
        if pattern[i] == '.':
            test_pattern = pattern[:i] + '#' + pattern[i + 1:]
        elif pattern[i] == '#':
            test_pattern = pattern[:i] + '.' + pattern[i + 1:]
        else:
            continue
        score = get_pattern_score(test_pattern.split('\n'), exclude=original_score)
        if score:
            answer += score
            break

submit(answer)
