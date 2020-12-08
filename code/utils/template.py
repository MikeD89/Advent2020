from utils import utils
import math
import string


def process_data(data):
    processed = []
    for line in data:
        processed.append(line)
    return processed


def partOne(data):
    return 0


def partTwo(data):
    return 0


def testCase(line):
    assert True


def test():
    testCase("")
    return "Pass!"


if __name__ == "__main__":
    day = 1

    # Load Data
    data = utils.load_data("day%s.txt" % day)
    processed = process_data(data)

    # Do puzzle
    print("---- Day %s ----" % day)
    print("Tests:  " + test())
    print("Part 1: " + str(partOne(processed)))
    print("Part 2: " + str(partTwo(processed)))
