from collections import defaultdict
from itertools import zip_longest
from math import atan2, dist, tau
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def angle(P, Q):
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

directions = {
    P: {angle(P, Q) for Q in asteroids if Q is not P}
    for P in asteroids
}

best_location = max(asteroids, key=lambda P: len(directions[P]))
nasteroids = len(directions[best_location])

# Part 2

P = best_location
other_asteroids = (Q for Q in asteroids if Q is not P)
asteroid_lines = defaultdict(list)
for Q in other_asteroids:
    asteroid_lines[angle(P, Q)].append(Q)

for dir, asts in asteroid_lines.items():
    asts.sort(key=lambda Q: dist(P, Q))

sorted_lines = (asteroid_lines[angle] for angle in sorted(asteroid_lines))
destroyed_asteroids = [
    asteroid
    for line in zip_longest(*sorted_lines)
    for asteroid in line
    if asteroid is not None
]
destroyed = destroyed_asteroids[199]

print('Part 1:', best_location, nasteroids)
print('Part 2:', destroyed.x * 100 + destroyed.y)
