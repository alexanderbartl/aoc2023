from aocd import data, submit


def get_pattern_score(pattern):
    for i in range(1, len(pattern)):
        if pattern[max(0, 2 * i - len(pattern)):i] == list(reversed(pattern[i:2 * i])):
            return i * 100
    pattern = list(zip(*pattern))
    for i in range(1, len(pattern)):
        if pattern[max(0, 2 * i - len(pattern)):i] == list(reversed(pattern[i:2 * i])):
            return i


submit(sum(get_pattern_score(pattern.split('\n')) for pattern in data.split('\n\n')))
