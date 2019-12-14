from itertools import accumulate
from typing import NamedTuple

with open('day03.in') as file:
    wire_segments = {wire: line.split(',') for wire, line in enumerate(file)}

class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    @property
    def norm(self):
        """Manhattan norm"""
        return abs(self.x) + abs(self.y)

X = Point(1, 0)
Y = Point(0, 1)

dirs = {'R': X, 'U': Y, 'L': -X, 'D': -Y}

def path(segments):
    """Expand a list of segments into a path of unit steps.
    E.g.: ['R2', 'U3'] -> (X, X, Y, Y, Y)"""
    for segment in segments:
        direction = dirs[segment[0]]
        nsteps = int(segment[1:])
        for step in range(nsteps):
            yield direction

steps = {0: {}, 1: {}}  # For each wire (0, 1), store dict of {position: #steps}
for wire, segments in wire_segments.items():
    positions = accumulate(path(segments))
    for step, position in enumerate(positions):
        if position not in steps[wire]:
            steps[wire][position] = step

intersections = steps[0].keys() & steps[1].keys()

mindist = min(position.norm for position in intersections)
minstep = min(steps[0][pos] + steps[1][pos] for pos in intersections)

print('Part 1:', mindist)
print('Part 2:', minstep)
