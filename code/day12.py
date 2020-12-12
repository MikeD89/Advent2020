from utils import utils


class Navigator:
    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.facing = 90

    def run(self, program):
        for line in program:
            self.next(line)

    def next(self, line):
        # Runs the next step
        instr = line[0]
        num = line[1:]
        self.step(instr, int(num))

    def travel(self, value):
        if self.facing == 0:
            self.ns += value
        elif self.facing == 90:
            self.ew += value
        elif self.facing == 180:
            self.ns -= value
        elif self.facing == 270:
            self.ew -= value

    def step(self, instr, v):
        if instr == "N":
            self.ns += v
        elif instr == "S":
            self.ns -= v
        elif instr == "E":
            self.ew += v
        elif instr == "W":
            self.ew -= v
        elif instr == "L":
            self.facing = (self.facing - v) % 360
        elif instr == "R":
            self.facing = (self.facing + v) % 360
        elif instr == "F":
            self.travel(v)


def process(data):
    return data


def partOne(data):
    n = Navigator()
    n.run(data)
    return abs(n.ns) + abs(n.ew)


def partTwo(data):
    return None


if __name__ == "__main__":
    utils.run(12, process, None, partOne, partTwo)
