from itertools import permutations
from day7_intcode import IntCode

def simple_signal(intcode, phase_sequence):
    amplifiers = {X: IntCode(intcode) for X in 'ABCDE'}

    signal = 0
    for amplifier, phase in zip(amplifiers.values(), phase_sequence):
        amplifier.start()
        amplifier.input(phase, signal)
        signal = amplifier.output

    return signal

def feedback_signal(intcode, phase_sequence):
    amplifiers = {X: IntCode(intcode) for X in 'ABCDE'}

    for amplifier, phase in zip(amplifiers.values(), phase_sequence):
        amplifier.start()
        amplifier.input(phase)

    signal = 0
    while not amplifiers['E'].finished:
        for amplifier in amplifiers.values():
            amplifier.input(signal)
            signal = amplifier.output

    return signal

with open('day7.in', 'r') as file:
    intcode = [int(n) for n in next(file).strip().split(',')]

phase_sequences = permutations(range(5))
max_simple = max(simple_signal(intcode, ps) for ps in phase_sequences)

phase_sequences = permutations(range(5, 10))
max_feedback = max(feedback_signal(intcode, ps) for ps in phase_sequences)

print('Part 1:', max_simple)
print('Part 2:', max_feedback)