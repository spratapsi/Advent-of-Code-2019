from itertools import count
from operator import add, mul

with open('day2.in') as input_file:
	intcode = [int(n) for n in input_file.read().split(',')]

operations = {1: add, 2: mul}

intcode[1] = 12
intcode[2] = 2

for pos in count(start=0, step=4):
	if intcode[pos] == 99:
		break
	opcode, posx, posy, pos_result = intcode[pos:pos+4]

	operation = operations[opcode]
	x = intcode[posx]
	y = intcode[posy]

	intcode[pos_result] = operation(x, y)

print(intcode[0])