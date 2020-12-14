from utils import utils
import collections

tD = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

tD2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


class Accumulator:
    def __init__(self):
        self.bitDepthString = '{:036b}'
        self.maskPrefix = "mask = "
        self.mask = ""
        self.memory = collections.defaultdict(int)

    def setMask(self, value):
        self.mask = value

    def andMemoryMask(self, value):
        return [value]

    def andValueMask(self, value):
        binary = self.bitDepthString.format(int(value))
        rVal = list(binary)
        for i in range(len(self.mask)):
            rVal[i] = binary[i]
            if self.mask[i] != "X":
                rVal[i] = self.mask[i]
        return int("".join(rVal), 2)

    def setMemory(self, value: str):
        s = value.split(" = ")
        i = s[0].replace("mem[", "").replace("]", "")

        memoryMasked = self.andMemoryMask(i)
        valueMasked = self.andValueMask(s[1])
        for m in memoryMasked:
            self.memory[m] = valueMasked

    def runLine(self, line: str):
        if line.startswith(self.maskPrefix):
            self.setMask(line.replace(self.maskPrefix, ""))
        else:
            self.setMemory(line)

    def sum(self):
        return sum(self.memory.values())


class AccumulatorVersionTwo(Accumulator):
    def _recurseReplace(self, lst, string, index) -> list:
        # Get out clause
        if "X" not in string:
            lst.append(string)
            return

        # Recurse down
        for i in range(index, len(string)):
            c = string[i]
            if c == "X":
                self._doReplace(lst, string, i, "0")
                self._doReplace(lst, string, i, "1")

    def _doReplace(self, lst, string, index, value) -> list:
        thisString = list(string)
        thisString[index] = value
        thisString = "".join(thisString)

        return self._recurseReplace(lst, thisString, index+1)

    def andMemoryMask(self, value):
        binary = self.bitDepthString.format(int(value))
        modValue = list(binary)

        # Handle the 0's and 1's - this is easy
        for i in range(len(self.mask)):
            m = self.mask[i]
            v = modValue[i]
            if m == "0":
                modValue[i] = v
            else:
                modValue[i] = m
        modValue = "".join(modValue)

        # Now we branch!
        rVal = list()
        self._recurseReplace(rVal, modValue, 0)
        return rVal

    def andValueMask(self, value):
        return int(value)


def process(data):
    # data = tD.strip().splitlines()
    return data


def partOne(data):
    a = Accumulator()
    for line in data:
        a.runLine(line)
    return a.sum()


def partTwo(data):
    #data = tD2.strip().splitlines()
    a = AccumulatorVersionTwo()
    for line in data:
        a.runLine(line)
    return a.sum()


if __name__ == "__main__":
    utils.run(14, process, None, partOne, partTwo)
