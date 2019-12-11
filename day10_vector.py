from collections import defaultdict
from itertools import combinations, zip_longest
from math import gcd, hypot
from typing import NamedTuple

with open('day10.in', 'r') as file:
    asteroid_map = [line.strip() for line in file]

class Vector(NamedTuple):
    x: int
    y: int

    def direction(self):
        g = gcd(self.x, self.y)
        return Vector(self.x // g, self.y // g)

    def sign_tangent(self):
        x, y = self.x, self.y
        sign = -1 if x > 0 else 1 if x < 0 else -1 if y > 0 else -1
        tangent = float('inf') if x == 0 else y / x
        return (sign, tangent)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(P, Q):
        return Vector(P.x - Q.x, P.y - Q.y)

# Part 1

asteroids = [
    Vector(x, y)
    for y, line in enumerate(asteroid_map)
    for x, character in enumerate(line)
    if character == '#'
]

asteroid_lines = {P: defaultdict(list) for P in asteroids}
for P, Q in combinations(asteroids, 2):
    PQ = (Q - P).direction()
    QP = -PQ
    asteroid_lines[P][PQ].append(Q)
    asteroid_lines[Q][QP].append(P)

station_location = max(asteroid_lines, key=lambda P: len(asteroid_lines[P]))
nasteroids = len(asteroid_lines[station_location])


# Part 2

lines = asteroid_lines[station_location]

for line in lines.values():
    line.sort(key=lambda P: hypot(*P))

sorted_lines = (lines[tg] for tg in sorted(lines, key=Vector.sign_tangent))
destroyed_asteroids = [
    asteroid
    for line in zip_longest(*sorted_lines)
    for asteroid in line
    if asteroid is not None
]
destroyed = destroyed_asteroids[199]

print('Part 1:', station_location, nasteroids)
print('Part 2:', destroyed.x * 100 + destroyed.y)
