from collections import Counter

def next_larger(string):
    l = []
    prev = '1'
    s = iter(string)
    for c in s:
        if c >= prev:
            l.append(c)
            prev = c
        else:
            l.append(prev)
            l.extend(prev for _ in s)
    return l

def pwd_range(start, end):
    increment = {n: m for n, m in zip('12345678', '23456789')}
    digits = next_larger(start)
    length = len(digits)
    pos = -1
    while (pwd := ''.join(digits)) <= end:
        yield pwd

        try:
            while digits[pos] == '9':
                pos -= 1
        except IndexError:
            return

        last = digits[pos] = increment[digits[pos]]

        for pos in range(pos, 0):
            digits[pos] = last

def repeated_any(password: str) -> bool:
    return any(c == c_ for c, c_ in zip(password, password[1:]))

def repeated_two(password: str) -> bool:
    return 2 in Counter(password).values()

lower = '123217'
upper = '647015'

n1 = sum(repeated_any(pwd) for pwd in pwd_range(lower, upper))
n2 = sum(repeated_two(pwd) for pwd in pwd_range(lower, upper))

print('Part 1:', n1)
print('Part 2:', n2)