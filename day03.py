from itertools import accumulate

with open('day3.in') as file:
    wire_segments = [line.split(',') for line in file]

dirs = {'R': 1, 'U': 1j, 'L': -1, 'D': -1j}

def norm(z):
    """Manhattan norm"""
    return abs(z.real) + abs(z.imag)

def path(segments):
    """Expand a list of segments into a path of unit steps.
    E.g.: ['R2', 'U3'] -> (1, 1, 1j, 1j, 1j)"""
    for segment in segments:
        direction = dirs[segment[0]]
        nsteps = int(segment[1:])
        for step in range(nsteps):
            yield direction

steps = {0: {}, 1: {}}  # For each wire (0, 1), store dict of {position: #steps}
for wire, segments in enumerate(wire_segments):
    positions = accumulate(path(segments))
    for step, position in enumerate(positions):
        if position not in steps[wire]:
            steps[wire][position] = step

intersections = steps[0].keys() & steps[1].keys()

mindist = min(norm(position) for position in intersections)
minstep = min(steps[0][pos] + steps[1][pos] for pos in intersections)

print('Part 1:', mindist)
print('Part 2:', minstep)