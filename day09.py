from day09_intcode import IntCode

with open('day09.in', 'r') as file:
    intcode = [int(n) for n in next(file).strip().split(',')]

BOOST1 = IntCode(intcode)
BOOST1.start()
BOOST1.input(1)

BOOST2 = IntCode(intcode)
BOOST2.start()
BOOST2.input(2)

print('Part 1:', BOOST1.read())
print('Part 2:', BOOST2.read())
