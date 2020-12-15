import collections
from utils import utils
from tests import day8_test as tests


def calculate(iter, data):
    lastNum = -1
    lastSpoken = collections.defaultdict(lambda: -1)
    priorSpoken = collections.defaultdict(lambda: -1)

    for i in range(iter):
        thisNumber = lastNum
        if (i < len(data)):
            # First numbers
            thisNumber = data[i]
        elif priorSpoken[thisNumber] == -1 or lastSpoken[thisNumber] == -1:
            # Not spoken before, or only spoken once
            thisNumber = 0
        else:
            # has been spoken before
            thisNumber = lastSpoken[thisNumber] - priorSpoken[thisNumber]

        # Store this turn
        priorSpoken[thisNumber] = lastSpoken[thisNumber]
        lastSpoken[thisNumber] = i + 1
        lastNum = thisNumber
    return lastNum


def test():
    assert calculate(10, [0, 3, 6]) == 0
    assert calculate(2020, [0, 3, 6]) == 436
    assert calculate(2020, [1, 3, 2]) == 1
    assert calculate(2020, [1, 3, 2]) == 1
    assert calculate(2020, [2, 1, 3]) == 10
    assert calculate(2020, [1, 2, 3]) == 27
    assert calculate(2020, [2, 3, 1]) == 78
    assert calculate(2020, [3, 2, 1]) == 438
    assert calculate(2020, [3, 1, 2]) == 1836
    return "Tests Pass!"


def process(data):
    return [0, 13, 16, 17, 1, 10, 6]


def partOne(data):
    return calculate(2020, data)


def partTwo(data):
    # Lets just be lazy today
    return calculate(30000000, data)


if __name__ == "__main__":
    utils.run(15, process, test, partOne, partTwo)
