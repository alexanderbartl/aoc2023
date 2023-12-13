import re

from aocd import data, submit

lines = data.split('\n')


def check_line(springs, expected):
    actual = []
    for i, spring in enumerate(springs):
        if spring == '#' and (i == 0 or springs[i - 1] == '.'):
            actual.append(1)
        elif spring == '#' and springs[i - 1] == '#':
            actual[-1] += 1
        elif spring == '?':
            if not actual:
                return True
            return len(actual) <= len(expected) and \
                springs[i:].replace('?', '#').count('#') >= sum(expected[len(actual):]) and \
                actual[:-1] == expected[:len(actual) - 1] and \
                actual[-1] <= expected[len(actual) - 1]

    return actual == expected


def permutate(springs, expected):
    if not check_line(springs, expected):
        return
    if '?' not in springs:
        yield springs
    else:
        yield from permutate(springs.replace('?', '#', 1), expected)
        yield from permutate(springs.replace('?', '.', 1), expected)


answer_a = 0
answer_b = 0
for line in lines:
    # print('.', end='', flush=True)
    springs, counts = line.split(' ')
    counts = [int(count) for count in counts.split(',')]
    answer_a += len(list(permutate(springs, counts)))
    # answer_b += len([config for config in permutate('?'.join([springs] * 5), counts * 5)])

print()
print(answer_a)
print(answer_b)
# submit(answer_b)
