from utils import utils

day = 18

tD = """
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""
tA1 = 26 + 437 + 12240 + 13632
tA2 = 46 + 1445 + 669060 + 23340


class Calculator:
    def findFirstBrackets(self, line):
        # Find those brackets
        bracketStack = list()
        for i in range(len(line)):
            c = line[i]
            if c == "(":
                bracketStack.append(i)
            elif c == ")":
                j = bracketStack.pop()
                return (j, i)
        return None

    def findSum(self, line, charSet):
        found = False
        startingPointer = 0
        for i in range(len(line)):
            c = line[i]

            # Is this the end?
            if not c.isdigit() and found:
                return (startingPointer, i)

            # Is this the start?
            elif c in charSet and not found:
                found = True

            elif not c.isdigit():
                startingPointer = i + 1

        # if we found a digit, but reached the end, we still have maths to do
        return (startingPointer, len(line)) if found else None

    def solve(self, line, charset):
        sumRange = self.findSum(line, charset)
        while sumRange != None:
            result = eval(line[sumRange[0]:sumRange[1]])
            line = str(result).join([line[:sumRange[0]], line[sumRange[1]:]])
            sumRange = self.findSum(line, charset)

        return line

    def calculate(self, line, charset):
        line = line.strip().replace(" ", "")
        brackets = self.findFirstBrackets(line)
        while brackets != None:
            partialLine = line[brackets[0]+1:brackets[1]]
            partial = self.calc(partialLine)
            line = str(partial).join([line[:brackets[0]], line[brackets[1]+1:]])
            brackets = self.findFirstBrackets(line)

        return self.solve(line, charset)

    def calc(self, line):
        return int(self.calculate(line, "*+"))

    def sumData(self, data):
        return sum([int(self.calc(line)) for line in data])


class CalculatorMk2(Calculator):
    def calc(self, line):
        line = self.calculate(line, "+")
        line = self.calculate(line, "*")
        return line


def test():
    assert Calculator().sumData(utils.load_test_data(tD)) == tA1
    assert CalculatorMk2().sumData(utils.load_test_data(tD)) == tA2
    return "Pass!"


if __name__ == "__main__":
    def process_data(d): return d
    def partOne(d): return Calculator().sumData(d)
    def partTwo(d): return CalculatorMk2().sumData(d)

    utils.run(day, process_data, test, partOne, partTwo)
