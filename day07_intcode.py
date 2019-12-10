from collections import namedtuple
from enum import Enum, auto

Operation = namedtuple('Operation', ['function', 'nparams'])

class IntCode(list):
    """IntCode Computer.
    Important: the functions take only pointers as arguments.
    This simplifies the approach for storing results."""

    def __init__(self, intcode):
        super().__init__(intcode)
        self.ptr = 0
        self.output = None
        self.finished = False
        self._process = self._start_process()

    def start(self):
        """self._process is a subroutine that needs to be started."""
        next(self._process)

    def input(self, *values):
        for value in values:
            self._process.send(value)

    def _next(self, mode='1'):
        """Get next pointer and increment"""
        value = self.ptr
        self.ptr += 1
        return value if mode == '1' else self[value]

    def _start_process(self):
        """Main coroutine"""
        while (instruction := self[self._next()]) != 99:
            modes_reversed, opcode = divmod(instruction, 100)
            operation, nparams = self.operations[opcode]

            modes = str(modes_reversed).zfill(nparams)[::-1]
            param_pointers = (self._next(mode) for mode in modes)

            if operation is IntCode.inp:
                inp = yield
                operation(self, inp, *param_pointers)
            elif operation is IntCode.out:
                self.output = operation(self, *param_pointers)
            else:
                operation(self, *param_pointers)

        self.finished = True
        yield

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