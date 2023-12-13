import re

from debug import data, submit

lines = data.split('\n')


def check_line(springs, expected):
    known_springs = springs[:springs.index('?')] if '?' in springs else springs
    actual = [len(x) for x in known_springs.split('.') if x]

    if springs == known_springs:
        return actual == expected

    if not actual:
        return True

    return len(actual) <= len(expected) and \
        actual[:-1] == expected[:len(actual) - 1] and \
        actual[-1] <= expected[len(actual) - 1]


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
for i, line in enumerate(lines):
    print(i)
    springs, counts = line.split(' ')
    counts = [int(count) for count in counts.split(',')]
    answer_a += len(list(permutate(springs, counts)))
    for _ in permutate('?'.join([springs] * 5), counts * 5):
        answer_b += 1

print()
print(answer_a)
print(answer_b)
submit(answer_b)
