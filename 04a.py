from aocd import data, submit

lines = data.split('\n')

answer = 0
for line in lines:
    card, numbers = line.split(': ')
    winning_, mine_ = numbers.split(' | ')
    winning = set(map(int, winning_.split()))
    mine = set(map(int, mine_.split()))
    answer += 2 ** (len(winning & mine) - 1) if len(winning & mine) > 0 else 0

print(answer)
submit(answer)
