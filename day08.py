from collections import Counter
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

with open('day8.in', 'r') as file:
	digits = next(file).strip()

width, height = 25, 6
line_length = width * height

layers = [layer for layer in grouper(digits, line_length)]
counters = [Counter(layer) for layer in layers]

min_layer = min(range(len(layers)), key=lambda l: counters[l]['0'])
check = counters[min_layer]['1'] * counters[min_layer]['2']


def visible_color(pixel_column):
	filtered = (pixel for pixel in pixel_column if c != '2')
	return filtered.next()

visible = [visible_color(pixel_column) for pixel_column in zip(*layers)]

def render(layer):
	lines = grouper(layer, linelength)
	for line in lines:
		print(''.join(line).replace('0', ' '))

print('Part 1:', check)
print('Part 2:')
render(visible)