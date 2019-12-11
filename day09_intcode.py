from collections import defaultdict, namedtuple

Operation = namedtuple('Operation', ['function', 'nparams'])

class IntCode(defaultdict):
    """IntCode Computer.
    defaultdict allows to access non-initialized memory addresses.
    Important: the operations arguments must be pointers."""

    def __init__(self, intcode):
        super().__init__(int)
        self.update(enumerate(intcode))

        self.ptr = 0
        self.relative_base = 0
        self.outputs = []
        self.finished = False

    def start(self):
        """self._process is a subroutine that needs to be started."""
        self._process = self._main_process()
        next(self._process)

    def input(self, *values):
        for value in values:
            self._process.send(value)

    def _next_ptr(self, mode='1'):
        """Get next pointer and increment"""
        if mode == '0':
            pointer = self[self.ptr]
        elif mode == '1':
            pointer = self.ptr
        elif mode == '2':
            pointer = self[self.ptr] + self.relative_base

        self.ptr += 1
        return pointer

    @staticmethod
    def _split(instruction):
        """Split instruction code into operation and modes."""
        modes_reversed, opcode = divmod(instruction, 100)
        operation, nparams = IntCode.operations[opcode]
        modes = f'{modes_reversed:0{nparams}}'[::-1]
        return operation, modes

    def _main_process(self):
        """Main coroutine. Deals with input and output."""
        while (instruction := self[self._next_ptr()]) != 99:
            operation, modes = IntCode._split(instruction)
            param_pointers = (self._next_ptr(mode) for mode in modes)

            if operation is IntCode.inp:
                inp = yield
                operation(self, inp, *param_pointers)
            elif operation is IntCode.out:
                output = operation(self, *param_pointers)
                self.outputs.append(output)
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

    def rlb(self, increment):
        self.relative_base += self[increment]

    operations = {
        1: Operation(add, nparams=3),
        2: Operation(mul, nparams=3),
        3: Operation(inp, nparams=1),
        4: Operation(out, nparams=1),
        5: Operation(jit, nparams=2),
        6: Operation(jif, nparams=2),
        7: Operation(lst, nparams=3),
        8: Operation(eql, nparams=3),
        9: Operation(rlb, nparams=1)
    }
