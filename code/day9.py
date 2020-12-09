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


def partTwo(data):
    invalidNumber = partOne(data)

    for i in range(1, 100):
        values = []

        for line in data:
            # Preamble
            if len(values) < i:
                values.append(line)
                continue

            # Exit early clause
            if line > invalidNumber:
                break

            total = sum(values)
            if total == invalidNumber:
                return min(values) + max(values)

            values.pop(0)
            values.append(line)
    return "N/A"


if __name__ == "__main__":
    utils.run(9, process, None, partOne, partTwo)
