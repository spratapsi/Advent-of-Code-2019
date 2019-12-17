from itertools import cycle, repeat
from functools import partial
from math import prod, gcd

times = partial(repeat, None)

def lcm(a, b):
    return a * b // gcd(a, b)

def pattern(n, base=(0, 1, 0, -1)):
    p = cycle(k for k in base for _ in times(n))
    next(p)
    return p

def FFT(signal, k):
    return abs(sum(map(prod, zip(signal, pattern(k+1))))) % 10

with open('day16.in') as file:
    signal = [int(n) for n in next(file).strip()]

n = len(signal)

# Part 1

for _ in times(100):
    signal = [FFT(signal, k) for k in range(n)]

part_1 = ''.join(str(k) for k in signal[:8])

# Part 2

offset = int(''.join(str(k) for k in signal[:7]))

print('Part 1:', part_1)