from day09_intcode import IntCode

with open('day15.in') as file:
    program = [int(n) for n in next(file).split(',')]

def grid_to_string(grid):
    mask = {None: ' ', WALL: '#', ALLOWED: '.', OXYGEN: 'o', -1: 'x'}

    x_min, x_max = int(min(z.real for z in grid)), int(max(z.real for z in grid))
    y_min, y_max = int(min(z.imag for z in grid)), int(max(z.imag for z in grid))

    return '\n'.join(
        ''.join(mask[grid.get(x + 1j*y, (None, None))[0]] for x in range(x_min, x_max + 1))
        for y in range(y_max, y_min - 1, -1)
    )


directions = NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4
responses = WALL, ALLOWED, OXYGEN = 0, 1, 2

instructions = {NORTH: 1j, SOUTH: -1j, WEST: -1, EAST: 1}

def find_oxy(position, state, dist=0):
    global record
    record[position] = (state, dist)
    for dir in directions:
        new_dist = dist + 1
        new_pos = position + instructions[dir]
        if new_pos in record:
            continue
        computer.input(dir)
        new_state = computer.read()
        if new_state == WALL:
            record[new_pos] = (WALL, -1)
        elif new_state == OXYGEN:
            return new_pos, new_dist
        elif new_state == ALLOWED:
            return find_oxy(new_pos, new_state, new_dist)
            computer.input({1: 2, 2: 1, 3: 4, 4: 3}[dir])  # Go back
            computer.read()


def find_all_positions(position, state, dist=0):
    global record
    record[position] = (state, dist)
    for dir in directions:
        new_dist = dist + 1
        new_pos = position + instructions[dir]
        if new_pos in record:
            continue
        computer.input(dir)
        new_state = computer.read()
        if new_state == WALL:
            record[new_pos] = (WALL, -1)
        else:
            find_all_positions(new_pos, new_state, new_dist)
            computer.input({1: 2, 2: 1, 3: 4, 4: 3}[dir])
            computer.read()


computer = IntCode(program)
computer.start()

record = {}
oxy_pos, oxy_dist = find_oxy(position=0j, state=ALLOWED)

record = {}
find_all_positions(oxy_pos, state=OXYGEN)
time_to_fill = max(t[1] for t in record.values())

print('Part 1:', oxy_dist)
print('Part 2:', time_to_fill)
print('Maze:', grid_to_string(record), sep='\n')