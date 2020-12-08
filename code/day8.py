from utils import utils
from tests import day8_test as d8t


class BootCode:
    def __init__(self):
        self.accumulator = 0
        self.pointer = 0
        self.lastAccumulator = self.accumulator
        self.lastPointer = self.pointer

    def run(self, program):
        ranLines = set()
        while True:
            if self.pointer in ranLines:
                return self.accumulator

            # Store the line and run it
            ranLines.add(self.pointer)
            self.next(program)

    def next(self, program):
        # Runs the next step
        self.stepTuple(program[self.pointer])

    def acc(self, val):
        # Accumulate the variable
        self.accumulator += val
        self.pointer += 1

    def jmp(self, val):
        # Jump the pointer elsewhere
        self.pointer += val

    def nop(self, val):
        # No-op does nothing
        self.pointer += 1

    def stepTuple(self, line):
        # Runs a tuple step
        self.step(line[0], line[1])

    def step(self, task, value):
        # Save state
        self.lastPointer = self.pointer
        self.lastAccumulator = self.accumulator

        # Runs a manual step
        {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }.get(task, lambda: "nothing")(value)

    def undo(self):
        # Undo state
        self.pointer = self.lastPointer
        self.accumulator = self.lastAccumulator


class BootCodeEOFVarient(BootCode):
    def run(self, program):
        ranLines = set()

        while True:
            if self.pointer in ranLines:
                return False

            if self.pointer > (len(program) - 1):
                return True

            # Store the line and run it
            ranLines.add(self.pointer)
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
        modData = data.copy()
        newOp = "jmp" if inst == "nop" else "nop"
        modData[i] = tuple([newOp, data[i][1]])

        # Test
        bc = BootCodeEOFVarient()
        success = bc.run(modData)
        if success:
            return bc.accumulator


if __name__ == "__main__":
    utils.run(8, process, d8t.test, partOne, partTwo)
