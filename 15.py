from collections import defaultdict

from aocd import data, submit


def ascii_hash(string):
    result = 0
    for char in string:
        result = ((result + ord(char)) * 17) % 256
    return result


print('Part A:', sum(ascii_hash(instruction) for instruction in data.replace('\n', '').split(',')))

boxes = defaultdict(list)
for instruction in data.replace('\n', '').split(','):
    if '=' in instruction:
        label, focal_length = instruction.split('=')
        box = boxes[ascii_hash(label)]
        try:
            index = [b[0] for b in box].index(label)
            box[index] = (label, focal_length)
        except ValueError:
            box.append((label, focal_length))
    else:
        label = instruction[:-1]
        boxes[ascii_hash(label)] = [b for b in boxes[ascii_hash(label)] if b[0] != label]

focussing_power = sum((b + 1) * (i + 1) * int(lens[1]) for b, box in boxes.items() for i, lens in enumerate(box))

print('Part B:', focussing_power)
