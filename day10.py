from collections import defaultdict
from itertools import combinations, zip_longest
from math import atan2, dist, tau, pi
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def angle(P, Q):
    """Compute angle of line PQ, in (-pi/4, 3pi/4]"""
    D = Q - P
    theta = atan2(D.y, D.x)
    angle = tau + theta if theta < -tau / 4 else theta
    return round(angle, 10)

with open('day10.in', 'r') as file:
    asteroid_map = [line.strip() for line in file]

# Part 1

asteroids = [
    Point(x, y)
    for y, line in enumerate(asteroid_map)
    for x, character in enumerate(line)
    if character == '#'
]

asteroid_lines = {P: defaultdict(list) for P in asteroids}
for P, Q in combinations(asteroids, 2):
    theta = angle(P, Q)
    theta_ = theta + (pi if theta <= pi / 2 else -pi)
    asteroid_lines[P][theta].append(Q)
    asteroid_lines[Q][theta_].append(P)

best_location = max(asteroid_lines, key=lambda P: len(asteroid_lines[P]))
nasteroids = len(asteroid_lines[best_location])


# Part 2

P = best_location
lines = asteroid_lines[P]

for line in lines.values():
    line.sort(key=lambda Q: dist(P, Q))

sorted_lines = (lines[angle] for angle in sorted(lines))
destroyed_asteroids = [
    asteroid
    for line in zip_longest(*sorted_lines)
    for asteroid in line
    if asteroid is not None
]
destroyed = destroyed_asteroids[199]

print('Part 1:', best_location, nasteroids)
print('Part 2:', destroyed.x * 100 + destroyed.y)
