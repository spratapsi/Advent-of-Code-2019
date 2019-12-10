from collections import Counter

def increasing(password: str) -> bool:
	return all(c <= c_ for c, c_ in zip(password, password[1:]))

def repeated_any(password: str) -> bool:
	return any(c == c_ for c, c_ in zip(password, password[1:]))

def repeated_two(password: str) -> bool:
    return 2 in Counter(password).values()

def passwords(lower: str, upper: str) -> 'Generator[str]':
	return (str(pwd) for pwd in range(lower, upper+1))

lower = 123257
upper = 647015

n1 = sum(increasing(pwd) and repeated_any(pwd) for pwd in passwords(lower, upper))
n2 = sum(increasing(pwd) and repeated_two(pwd) for pwd in passwords(lower, upper))

print('Part 1:', n1)
print('Part 2:', n2)