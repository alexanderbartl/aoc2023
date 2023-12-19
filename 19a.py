import re
from functools import partial

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
                rules.append((lambda x: True, raw_rule))
            elif match2.group(2) == '>':
                rules.append(
                    (partial(lambda x, a, b: x[a] > b, a=match2.group(1), b=int(match2.group(3))), match2.group(4)))
            elif match2.group(2) == '<':
                rules.append(
                    (partial(lambda x, a, b: x[a] < b, a=match2.group(1), b=int(match2.group(3))), match2.group(4)))
        result[match.group(1)] = rules
    return result


def is_accepted(part, workflow='in'):
    if workflow == 'A':
        return True
    if workflow == 'R':
        return False
    for rule, new_workflow in workflows[workflow]:
        if rule(part):
            return is_accepted(part, new_workflow)


workflow_lines, part_lines = data.split('\n\n')
workflows = parse_workflows(workflow_lines.split('\n'))
print(workflows)

part_numbers = [list(map(int, re.findall(r'-?\d+', line))) for line in part_lines.split('\n')]
submit(sum(p[0] + p[1] + p[2] + p[3]
           for p in part_numbers if is_accepted({"x": p[0], "m": p[1], "a": p[2], "s": p[3]})))
