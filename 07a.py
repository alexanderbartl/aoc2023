from collections import Counter

from aocd import data, submit


def get_kind_value(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 9
    elif len(counts) == 2 and 4 in counts.values():
        return 8
    elif len(counts) == 2:
        return 7
    elif len(counts) == 3 and 3 in counts.values():
        return 6
    elif len(counts) == 3:
        return 5
    elif len(counts) == 4:
        return 4
    return 3


def convert_label(label):
    if label == 'T':
        return 10
    elif label == 'J':
        return 11
    elif label == 'Q':
        return 12
    elif label == 'K':
        return 13
    elif label == 'A':
        return 14
    return int(label)


def get_label_value(hand):
    return sum(convert_label(hand[i]) * 10 ** (8 - 2 * i) for i in range(len(hand)))


def get_value(line):
    hand = line.split(' ')[0]
    return 1e10 * get_kind_value(hand) + get_label_value(hand)


lines = sorted(data.split('\n'), key=get_value)

answer = 0
for rank, line in enumerate(lines):
    _, bid = line.split(' ')
    answer += int(bid) * (rank + 1)

assert answer == 250370104
print(answer)
# submit(answer)
