from collections import defaultdict
from day9_intcode import IntCode

with open('day11.in') as file:
    program = [int(n) for n in next(file).strip().split(',')]

BLACK, WHITE = 0, 1

def color_grid(program, initial_color):
    color_grid = defaultdict(lambda: BLACK)
    position, direction = 0j, 1j
    TURN_LEFT, TURN_RIGHT = 1j, -1j
    directions = {0: TURN_LEFT, 1: TURN_RIGHT}

    computer = IntCode(program)
    computer.start()
    color_grid[position] = initial_color

    while not computer.finished:
        color = color_grid[position]
        computer.input(color)

        new_color, instruction = computer.outputs[-2:]

        color_grid[position] = new_color
        direction *= directions[instruction]
        position += direction

    return color_grid

def grid_to_string(grid):
    mask = {BLACK: ' ', WHITE: '#'}

    x_min, x_max = int(min(z.real for z in grid)), int(max(z.real for z in grid))
    y_min, y_max = int(min(z.imag for z in grid)), int(max(z.imag for z in grid))

    return '\n'.join(
        ''.join(mask[grid[x + 1j*y]] for x in range(x_min, x_max + 1))
        for y in range(y_max, y_min - 1, -1)
    )

grid_1 = color_grid(program, initial_color=BLACK)
grid_2 = color_grid(program, initial_color=WHITE)
grid_2_string = grid_to_string(grid_2)

print('Part 1:', len(grid_1))
print('Part 2:', grid_2_string, sep='\n')