from itertools import count
from operator import add, mul

target = 19690720

with open('day2.in') as input_file:
	intcode_ = [int(n) for n in input_file.read().split(',')]

operations = {1: add, 2: mul}

nv = ((n, v) for n in range(100) for v in range(100))

for noun, verb in nv:
	intcode = list(intcode_)
	intcode[1:3] = noun, verb
	for pos in count(start=0, step=4):
		if intcode[pos] == 99:
			break
		opcode, posx, posy, pos_result = intcode[pos:pos+4]

		operation = operations[opcode]
		x = intcode[posx]
		y = intcode[posy]

		intcode[pos_result] = operation(x, y)

	if intcode[0] == target:
		print('Result =', 100 * noun + verb)