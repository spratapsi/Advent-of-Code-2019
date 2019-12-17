from collections import defaultdict
from day13_intcode import IntCode
# import os
# import time

EMPTY, WALL, BLOCK, PADDLE, BALL = 0, 1, 2, 3, 4

class Grid(defaultdict):
    def __init__(self):
        super().__init__(int)
        self.ball = 0
        self.paddle = 0

    def score(self):
        return self[-1, 0]

    def update(self, x, y, value):
        if value == BALL:
            self.ball = x
        elif value == PADDLE:
            self.paddle = x
        grid[x, y] = value

    def draw(self):
        x_min, x_max = 0, 44
        y_min, y_max = 0, 22

        mask = {EMPTY: ' ', WALL: 'W', BLOCK: 'X', PADDLE: '-', BALL: 'o'}

        string = '\n'.join(
            ''.join(mask.get(grid[x, y], ' ') for x in range(x_min, x_max + 1))
            for y in range(y_min, y_max + 1)
        )
        string += f'\nScore: {grid[-1, 0]}'

        os.system('cls')
        print(string)


with open('day13.in') as file:
    program = [int(x) for x in next(file).split(',')]

computer = IntCode(program)
computer[0] = 2

grid = Grid()

computer.start()
while computer.outputs:
    x, y, value = computer.read(3)
    grid.update(x, y, value)

# Part 1

nblocks = sum(value == BLOCK for value in grid.values())

# Part 2

LEFT, STAY, RIGHT = -1, 0, 1

while not computer.finished:
    while computer.outputs:
        x, y, value = computer.read(3)
        grid.update(x, y, value)

    ball, paddle = grid.ball, grid.paddle
    instruction = LEFT if ball < paddle else RIGHT if ball > paddle else 0
    computer.input(instruction)
    # grid.draw()
    # time.sleep(.025)

print('Part 1:', nblocks)
print('Part 2:', grid.score())