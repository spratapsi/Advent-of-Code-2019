from collections import namedtuple

Operation = namedtuple('Operation', ['function', 'nparams'])

class IntCode(list):
    """IntCode Computer.
    Important: the functions take only pointers as arguments.
    This simplifies the approach for storing results."""
    def __init__(self, intcode):
        self.ptr = 0
        super().__init__(intcode)

    def next(self, mode='1'):
        """Get next pointer and increment"""
        value = self.ptr
        self.ptr += 1
        return value if mode == '1' else self[value]

    def compute(self, input):
        """Main function to apply computations"""
        self.inp(input, pos=self[1])
        self.ptr = 2

        while (instruction := self[self.next()]) != 99:
            modes_reversed, opcode = divmod(instruction, 100)
            operation, nparams = self.operations[opcode]

            modes = str(modes_reversed).zfill(nparams)[::-1]
            param_pointers = (self.next(mode) for mode in modes)

            output = operation(self, *param_pointers)

            if output is not None:
                return output


    # Operations

    def add(self, a, b, pos):
        self[pos] = self[a] + self[b]

    def mul(self, a, b, pos):
        self[pos] = self[a] * self[b]

    def inp(self, input, pos):
        self[pos] = int(input)

    def out(self, pos):
        return self[pos]

    def jit(self, flag, pos):
        if self[flag]:
            self.ptr = self[pos]

    def jif(self, flag, pos):
        if not self[flag]:
            self.ptr = self[pos]

    def lst(self, a, b, pos):
        self[pos] = int(self[a] < self[b])

    def eql(self, a, b, pos):
        self[pos] = int(self[a] == self[b])

    operations = {
        1: Operation(add, nparams=3),
        2: Operation(mul, nparams=3),
        3: Operation(inp, nparams=1),
        4: Operation(out, nparams=1),
        5: Operation(jit, nparams=2),
        6: Operation(jif, nparams=2),
        7: Operation(lst, nparams=3),
        8: Operation(eql, nparams=3),
    }



with open('day5.in') as input_file:
    intcode_ = [int(n) for n in input_file.read().split(',')]

intcode = IntCode(intcode_)
output = intcode.compute(input=5)
print(output)
