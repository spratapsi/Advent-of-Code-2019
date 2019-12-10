from collections import defaultdict

with open('day6.in', 'r') as file:
    pairs = [tuple(x.strip() for x in line.split(')')) for line in file]

children = defaultdict(list)
parent = {}

for a, b in pairs:
    children[a].append(b)
    parent[b] = a

def levels(planet, n=0):
    """Depth-first-search traversal, reporting level"""
    yield (planet, n)
    for s in children[planet]:
        yield from levels(s, n+1)

def path(obj):
    """Path from obj to 'COM'"""
    yield obj
    if obj == 'COM':
        return
    yield from path(parent[obj])

# Part 1
checksum = sum(level for planet, level in levels('COM'))

# Part 2
path_you = set(path('YOU'))
path_san = set(path('SAN'))
path_common = path_you & path_san
njumps = (len(path_you) - 1) + (len(path_san) - 1) - 2 * len(path_common)


print('Part 1:', checksum)
print('Part 2:', njumps)