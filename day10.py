from collections import defaultdict
from itertools import combinations, zip_longest
from cmath import pi, phase

with open('day10.in', 'r') as file:
    asteroid_map = [line.strip() for line in file]

def angle(z):
    theta = phase(z)
    theta += 2 * pi if theta < -pi / 2 else 0
    return round(theta, 13)

# Part 1

asteroids = [
    (x + 1j * y)
    for y, line in enumerate(asteroid_map)
    for x, character in enumerate(line)
    if character == '#'
]

asteroid_lines = {P: defaultdict(list) for P in asteroids}
for P, Q in combinations(asteroids, 2):
    z = Q - P
    theta, theta_ = angle(z), angle(-z)
    asteroid_lines[P][theta].append(Q)
    asteroid_lines[Q][theta_].append(P)

station_location = max(asteroid_lines, key=lambda P: len(asteroid_lines[P]))
nasteroids = len(asteroid_lines[station_location])


# Part 2

lines = asteroid_lines[station_location]

for line in lines.values():
    line.sort(key=abs)

sorted_lines = (lines[angle] for angle in sorted(lines))
destroyed_asteroids = [
    asteroid
    for line in zip_longest(*sorted_lines)
    for asteroid in line
    if asteroid is not None
]
destroyed = destroyed_asteroids[199]

print('Part 1:', station_location, nasteroids)
print('Part 2:', destroyed.real * 100 + destroyed.imag)