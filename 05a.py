import re

from aocd import data, submit

seed_line, *maps_lines = data.split('\n\n')
seeds = [int(x) for x in seed_line.replace('seeds: ', '').split(' ')]

locations = []
for value in seeds:
    for raw_map in maps_lines:
        lines = raw_map.split('\n')
        numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in lines if not line.endswith(':')]

        for dest_start, src_start, length in numbers:
            if src_start <= value < src_start + length:
                value = dest_start + value - src_start
                break
    locations.append(value)

submit(min(locations))
