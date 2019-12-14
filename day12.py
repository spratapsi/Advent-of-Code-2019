from typing import NamedTuple
from itertools import combinations, count
from math import gcd
from functools import reduce
import re

def l1_norm(vector: list) -> int:
        return sum(abs(x) for x in vector)

def lcm(a: int, b: int) -> int:
    """Least common multiplier"""
    return a * b // gcd(a, b)

class Moon:
    def __init__(self, position):
        self.position = list(position)
        self.velocity = [0, 0, 0]

    def total_energy(self):
        kinetic = l1_norm(self.position)
        potential = l1_norm(self.velocity)
        return kinetic * potential


class MoonSystem(list):
    def apply_gravity(self, dim):
        for A, B in combinations(self, 2):
            a, b = A.position[dim], B.position[dim]
            if a < b:
                A.velocity[dim] += 1
                B.velocity[dim] -= 1
            elif a > b:
                A.velocity[dim] -= 1
                B.velocity[dim] += 1


    def apply_velocities(self, dim):
        for moon in self:
            moon.position[dim] += moon.velocity[dim]

    # Part 2

    def state(self, dim):
        pos = (moon.position[dim] for moon in self)
        vel = (moon.velocity[dim] for moon in self)
        return (*pos, *vel)

    def period_along_dimension(self, dim):
        initial_state = self.state(dim)
        for period in count(1):
            self.apply_gravity(dim)
            self.apply_velocities(dim)
            if self.state(dim) == initial_state:
                return period

    def period(self):
        periods = [system.period_along_dimension(dim) for dim in range(3)]
        return reduce(lcm, periods)


with open('day12.in') as file:
    positions = [
        [int(m) for m in re.findall(r'[xyz]=(-?\d+)', line)]
        for line in file
    ]

system = MoonSystem(Moon(position) for position in positions)

for t in range(1000):
    for dimension in range(3):
        system.apply_gravity(dimension)
        system.apply_velocities(dimension)

total_energy = sum(moon.total_energy() for moon in system)
period = system.period()

print('Part 1:', total_energy)
print('Part 2:', period)
