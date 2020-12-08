from utils import utils
from tests import day8_test as tests


class BootCode:
    def __init__(self):
        self.accumulator = 0
        self.address = 0
        self.lastAccumulator = self.accumulator
        self.lastAddress = self.address

    def run(self, program):
        ranLines = set()
        while True:
            if self.address in ranLines:
                return self.accumulator

            # Store the line and run it
            ranLines.add(self.address)
            self.next(program)

    def next(self, program):
        # Runs the next step
        self.stepTuple(program[self.address])

    def acc(self, val):
        # Accumulate the variable
        self.accumulator += val
        self.address += 1

    def jmp(self, val):
        # Jump the address elsewhere
        self.address += val

    def nop(self, val):
        # No-op does nothing
        self.address += 1

    def stepTuple(self, line):
        # Runs a tuple step
        self.step(line[0], line[1])

    def step(self, task, value):
        # Save state
        self.lastAddress = self.address
        self.lastAccumulator = self.accumulator

        # Runs a manual step
        {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }.get(task, lambda: "nothing")(value)

    def undo(self):
        # Undo state
        self.address = self.lastAddress
        self.accumulator = self.lastAccumulator


class BootCodeEOFVarient(BootCode):
    def run(self, program):
        ranLines = set()

        while True:
            if self.address in ranLines:
                return False

            if self.address > (len(program) - 1):
                return True

            # Store the line and run it
            ranLines.add(self.address)
            self.next(program)


def process(data):
    processed = []
    for line in data:
        split = line.split(" ")
        split[1] = int(split[1])
        processed.append(tuple(split))
    return processed


def partOne(data):
    return BootCode().run(data)


def partTwo(data):
    # We have to change one line
    for i in range(0, len(data)):

        # We can't "fix" accumulator errors
        inst = data[i][0]
        if inst != "nop" and inst != "jmp":
            continue

        # Modify the data
        newOp = "jmp" if inst == "nop" else "nop"
        data[i] = tuple([newOp, data[i][1]])

        # Test
        bc = BootCodeEOFVarient()
        success = bc.run(data)
        if success:
            return bc.accumulator

        # Reset the op
        data[i] = tuple([inst, data[i][1]])


if __name__ == "__main__":
    utils.run(8, process, tests.test, partOne, partTwo)
