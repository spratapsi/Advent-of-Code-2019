from itertools import count
from operator import add, mul

def pointer_jump(n):
	"""Adds a .jump attribute to a function"""
	def dec(f):
		f.jump = n
		return f

class IntCode(list):
	def init(self, intcode):
		super().__init__(intcode)

	def traverse(self):
		pointer = 0

		operations = {
			1: self.add,
			2: self.mul,
			99: self.stop,
		}

		while True:
			opcode = self[pointer]
			operation = operations(opcode)
			try:
				operation(pointer)
			except StopIteration:
				return

			pointer += operation.jump

	@pointer_jump(1)
	def stop(self, pos):
		raise StopIteration

	@pointer_jump(4)
	def add(self, pos):
		posx, posy, pos_result = self[pos+1:pos+4]
		self[pos_result] = self[posx] + self[posy]

	@pointer_jump(4)
	def mul(self, pos):
		posx, posy, pos_result = self[pos+1:pos+4]
		self[pos_result] = self[posx] * self[posy]


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