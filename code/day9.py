from utils import utils
import itertools
from tests import day8_test as tests


def process(data):
    processed = []
    for line in data:
        processed.append(int(line))
    return processed


def calculateSums(v, n):
    return {sum(item) for item in itertools.product(*[v]*n)}


def partOne(data):
    values = []

    for line in data:

        # Preamble
        if len(values) < 25:
            values.append(line)
            continue

        sums = calculateSums(values, 2)
        if line not in sums:
            return line

        values.pop(0)
        values.append(line)

    return "Unknown"


def partTwo(data, invalidNumber):

    for i in range(1, 100):
        values = []

        for line in data:
            # Exit early clause
            if line > invalidNumber:
                break

            # Preamble
            if len(values) < i:
                values.append(line)
                continue

            total = sum(values)

            # Exit early clause
            if total > invalidNumber:
                break

            if total == invalidNumber:
                return str(min(values) + max(values))

            values.pop(0)
            values.append(line)
    return "N/A"


if __name__ == "__main__":
    data = utils.load_data_by_day(9)
    processed = process(data)

    # Run
    p1R = utils.time_function(lambda: partOne(processed))
    p2R = utils.time_function(lambda: partTwo(processed, p1R[0]))

    # Print
    print("----- Day %s -----" % 9)
    print("Part 1 ({}) -> {}".format(p1R[1], p1R[0]))
    print("Part 2 ({}) -> {}".format(p2R[1], p2R[0]))
