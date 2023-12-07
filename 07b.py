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
        return 1
    elif label == 'Q':
        return 12
    elif label == 'K':
        return 13
    elif label == 'A':
        return 14
    return int(label)


def get_label_value(hand):
    return 1_00_00_00_00 * convert_label(hand[0]) + 1_00_00_00 * convert_label(hand[1]) + 1_00_00 * convert_label(
        hand[2]) + 1_00 * convert_label(hand[3]) + convert_label(hand[4])


def all_joker_values(hand):
    if 'J' in hand:
        for r in '23456789TQKA':
            yield from all_joker_values(hand.replace('J', r, 1))
    else:
        yield hand


def get_value(line):
    hand = line.split(' ')[0]
    kind_value = max(get_kind_value(h) for h in all_joker_values(hand))
    return 1_00_00_00_00_00 * kind_value + get_label_value(hand)


lines = sorted(data.split('\n'), key=get_value)

answer = 0
for rank, line in enumerate(lines):
    _, bid = line.split(' ')
    answer += int(bid) * (rank + 1)

submit(answer)
