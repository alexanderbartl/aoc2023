from aocd import data, submit
import re

sum = 0
for line in data.split('\n'):
    while True:
        if line.startswith('1') or line.startswith('one'):
            sum += 10
            break
        if line.startswith('2') or line.startswith('two'):
            sum += 20
            break
        if line.startswith('3') or line.startswith('three'):
            sum += 30
            break
        if line.startswith('4') or line.startswith('four'):
            sum += 40
            break
        if line.startswith('5') or line.startswith('five'):
            sum += 50
            break
        if line.startswith('6') or line.startswith('six'):
            sum += 60
            break
        if line.startswith('7') or line.startswith('seven'):
            sum += 70
            break
        if line.startswith('8') or line.startswith('eight'):
            sum += 80
            break
        if line.startswith('9') or line.startswith('nine'):
            sum += 90
            break
        if line.startswith('0') or line.startswith('zero'):
            sum += 0
            break
        else:
            line = line[1:]
    while True:
        if line.endswith('1') or line.endswith('one'):
            sum += 1
            break
        if line.endswith('2') or line.endswith('two'):
            sum += 2
            break
        if line.endswith('3') or line.endswith('three'):
            sum += 3
            break
        if line.endswith('4') or line.endswith('four'):
            sum += 4
            break
        if line.endswith('5') or line.endswith('five'):
            sum += 5
            break
        if line.endswith('6') or line.endswith('six'):
            sum += 6
            break
        if line.endswith('7') or line.endswith('seven'):
            sum += 7
            break
        if line.endswith('8') or line.endswith('eight'):
            sum += 8
            break
        if line.endswith('9') or line.endswith('nine'):
            sum += 9
            break
        if line.endswith('0') or line.endswith('zero'):
            sum += 0
            break
        else:
            line = line[:-1]

submit(sum)
