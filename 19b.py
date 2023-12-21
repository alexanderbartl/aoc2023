import re
from copy import deepcopy
from math import prod

from aocd import data, submit


def parse_workflows(lines):
    result = {}
    for line in lines:
        match = re.match(r'(\w+)\{(.*)}', line)
        if not line:
            break
        rules = []
        for raw_rule in match.group(2).split(','):
            match2 = re.match(r'(\w)([<>])(\d+):(\w+)', raw_rule)
            if not match2:
                rules.append(('*', raw_rule))
            else:
                rules.append((match2.group(2), match2.group(1), int(match2.group(3)), match2.group(4)))
        result[match.group(1)] = rules
    return result


def process(ranges, workflow='in'):
    if workflow == 'A':
        return prod(r[1] - r[0] + 1 for r in ranges.values())
    if workflow == 'R':
        return 0

    result = 0
    for rule in workflows[workflow]:
        ranges = deepcopy(ranges)
        fwd_ranges = deepcopy(ranges)
        if rule[0] == '*':
            result += process(ranges, rule[1])
            break
        elif rule[0] == '>':
            if rule[2] < ranges[rule[1]][0]:
                result += process(fwd_ranges, rule[3])
                break
            elif rule[2] >= ranges[rule[1]][1]:
                continue
            else:
                fwd_ranges[rule[1]] = (rule[2] + 1, ranges[rule[1]][1])
                ranges[rule[1]] = (ranges[rule[1]][0], rule[2])
                result += process(fwd_ranges, rule[3])
        elif rule[0] == '<':
            if rule[2] > ranges[rule[1]][1]:
                result += process(fwd_ranges, rule[3])
                break
            elif rule[2] <= ranges[rule[1]][0]:
                continue
            else:
                fwd_ranges[rule[1]] = (ranges[rule[1]][0], rule[2] - 1)
                ranges[rule[1]] = (rule[2], ranges[rule[1]][1])
                result += process(fwd_ranges, rule[3])
    return result


workflow_lines, part_lines = data.split('\n\n')
workflows = parse_workflows(workflow_lines.split('\n'))
print(workflows)

submit(process({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}))
