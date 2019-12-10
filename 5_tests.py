from day5 import IntCode

intcode = [3,9,8,9,10,9,4,9,99,-1,8]
input = 5
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = [3,9,8,9,10,9,4,9,99,-1,8]
input = 8
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = [3,9,7,9,10,9,4,9,99,-1,8]
input = 5
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = [3,9,7,9,10,9,4,9,99,-1,8]
input = 10
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1108,-1,8,3,4,3,99
input = 5
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1108,-1,8,3,4,3,99
input = 8
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1107,-1,8,3,4,3,99
input = 5
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1107,-1,8,3,4,3,99
input = 8
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9
input = 0
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9
input = 2
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1105,-1,9,1101,0,0,12,4,12,99,1
input = 0
expected = 0
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,3,1105,-1,9,1101,0,0,12,4,12,99,1
input = -1
expected = 1
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
input = 5
expected = 999
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
input = 8
expected = 1000
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)

intcode = 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
input = 10
expected = 1001
actual = IntCode(intcode).compute(input=input)
print('Expected, actual =', expected, actual)