from collections import Counter

from aocd import data, submit

solution_a = 0
solution_b = 0
for game in data.split('\n'):
    game_id, results = game.split(': ')
    game_id = int(game_id[5:])
    counts = Counter()
    for result in results.split('; '):
        for color_block in result.split(', '):
            count, color = color_block.split(' ')
            counts[color] = max(counts[color], int(count))

    if counts['red'] <= 12 and counts['green'] <= 13 and counts['blue'] <= 14:
        solution_a += game_id
    solution_b += counts['red'] * counts['green'] * counts['blue']

submit(solution_a)
submit(solution_b)
