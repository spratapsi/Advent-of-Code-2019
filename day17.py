from typing import NamedTuple
from day13_intcode import IntCode
import os
import time

class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def turn_left(self):
        return Point(-self.y, self.x)

    def turn_right(self):
        return Point(self.y, -self.x)

with open('day17.in') as f:
    program = [int(n) for n in next(f).split(',')]

# Part 1

computer = IntCode(program)
computer[0] = 2
computer.start()

view = ''.join(chr(output) for output in computer.read())

grid = {
    Point(x, y): char
    for x, line in enumerate(view.split('\n'))
    for y, char in enumerate(line)
}

def is_intersection(P):
    x, y = P
    cross = [(x-1, y), (x, y-1), (x  , y), (x, y+1), (x+1, y)]
    return all(grid.get(P, '.') == '#' for P in cross) 

alignment_check = sum((P.x * P.y) for P in grid if is_intersection(P))

# Part 2

position = next(P for P, char in grid.items() if char in '^<v>')
direction = {
    '^': Point(-1, 0),
    '<': Point(0, -1),
    '>': Point(0,  1),
    'v': Point(1, 0),
}[grid[position]]

def walk(grid, pos, dir):
    actions = {'L': lambda P: P, 'LF': Point.turn_left, 'RF': Point.turn_right}
    while True:
        for letter, actions in actions.items():
            new_dir = action(dir)
            new_pos = pos + new_dir
            if grid.get(new_pos) == '#':
                pos, dir = new_pos, new_dir
                yield letter
                break
        else:
            return


# Found the solution by hand by running the command:
# print(''.join(walk(grid, position, direction)))

MAIN = 'A,A,B,C,B,C,B,C,B,A'
A = 'L,10,L,8,R,8,L,8,R,6'
B = 'R,6,R,8,R,8'
C = 'R,6,R,6,L,8,L,10'

for function in (MAIN, A, B, C):
    inputs = (ord(c) for c in function + '\n')
    computer.input(*inputs)

computer.input(ord('n'), ord('\n'))

print('Part 1:', alignment_check)
print('Part 2:', computer.outputs.pop())