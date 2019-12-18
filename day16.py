from itertools import accumulate

with open('day16.in') as file:
    original_signal = [int(n) for n in next(file).strip()]

def srange(start, end, length, step):
    """Yield endpoints for slices:
    --> (start, start + length), (start + step, start + step + length), ...
    """
    inf, sup = start, start + length
    while sup <= end:
        yield (inf, sup)
        inf, sup = inf + step, sup + step
    if inf < end:
        yield (inf, min(sup, end))

def sum_signal(acc, k, end, offset=0):
    k_ = offset + k
    pstart = k - 1
    nstart = pstart + 2 * k_
    pos = sum(acc[s] - acc[i] for i, s in srange(pstart, end, k_, 4*k_))
    neg = sum(acc[s] - acc[i] for i, s in srange(nstart, end, k_, 4*k_))
    return pos - neg

def FFT(signal, offset=0):
    end = len(signal)
    acc = [0, *accumulate(signal)]
    signal = [
        abs(sum_signal(acc, k, end, offset)) % 10
        for k in range(1, end + 1)
    ]
    return signal

# Part 1

signal = original_signal
for phase in range(100):
    signal = FFT(signal)

message1 = ''.join(str(x) for x in signal[:8])

# Part 2

offset = int(''.join(str(x) for x in original_signal[:7]))
signal = (original_signal * 10_000)[offset:]  # We don't to compute the whole FFT

for phase in range(100):
    print(phase)
    signal = FFT(signal, offset=offset)

message2 = ''.join(str(x) for x in signal[:8])

print('Part 1:', message1)
print('Part 2:', message2)
