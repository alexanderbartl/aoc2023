from aocd import data, submit
import re

sum = 0
for line in data.split('\n'):
    match = re.match(r'[^\d]*(\d).*(\d)[^\d]*', line)
    if match:
        sum += int(match.group(1) + match.group(2))
    else:
        match = re.match(r'.*(\d).*', line)
        sum += int(match.group(1) + match.group(1))
submit(sum)
