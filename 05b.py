import re

from aocd import data, submit

seed_line, *maps_lines = data.split('\n\n')
seeds = [int(x) for x in seed_line.replace('seeds: ', '').split(' ')]

maps = [[list(map(int, re.findall(r'-?\d+', line))) for line in lines.split('\n') if not line.endswith(':')] for lines
        in maps_lines]
maps.reverse()

for location in range(1, 1_000_000_000):
    if location % 100_000 == 0:
        print(location)
    value = location
    for map_ in maps:
        for dest_start, src_start, length in map_:
            if dest_start <= value < dest_start + length:
                value = src_start + value - dest_start
                break
    for j in range(0, len(seeds), 2):
        if seeds[j] <= value < seeds[j] + seeds[j + 1]:
            submit(location)
            raise SystemExit()
