from collections import Counter

from aocd import data, submit

lines = data.split('\n')

cards = Counter({k: 1 for k in range(1, len(lines) + 1)})
for line in lines:
    card, numbers = line.split(': ')
    card = int(card.replace('Card ', ''))
    winning_, mine_ = numbers.split(' | ')
    winning = set(map(int, winning_.split()))
    mine = set(map(int, mine_.split()))
    overlap = len(winning & mine)
    for i in range(card + 1, card + overlap + 1):
        if i > len(lines):
            break
        cards[i] += cards[card]

answer = sum(cards.values())
print(answer)
submit(answer)
