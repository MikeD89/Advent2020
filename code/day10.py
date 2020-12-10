import collections
from utils import utils


def process(data):
    processed = []
    for x in data:
        processed.append(int(x))
    return sorted(processed) + [max(processed) + 3]


def partOne(data):
    oneJolt = 0
    threeJolt = 0
    curr = 0

    for x in data:
        diff = x - curr
        oneJolt += 1 if diff == 1 else 0
        threeJolt += 1 if diff == 3 else 0
        curr = x

    # Final appliance
    return oneJolt * threeJolt


def partTwo(data):
    cache = collections.defaultdict(int)

    cache[0] = 1
    for n in data:
        cache[n] = cache[n-1] + cache[n-2] + cache[n-3]

    return cache[max(data)]


def test():
    data1 = sorted([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19])
    data2 = sorted([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49])
    assert partTwo(data1) == 8
    assert partTwo(data2) == 19208
    print("Pass")
    return "Pass!"


if __name__ == "__main__":
    utils.run(10, process, test, partOne, partTwo)
