from utils import utils
import math
import string

s = "shiny gold"


def process_data(data):
    processed = dict()
    for line in data:
        line = line.replace(" bags", "").replace(" bag", "")
        split = line.split(" contain ")

        if "no other." in split[1]:
            processed[split[0]] = []
            continue

        bags = split[1][:-1].split(", ")

        processed[split[0]] = list(map(lambda a: tuple(a.split(" ", 1)), bags))
    return processed


def find_bag(data, bag, search):
    for (_, t) in bag:
        if t == search:
            return True

        if find_bag(data, data[t], search):
            return True

    return False


def partOne(data):
    return sum(1 for (_, x) in data.items() if find_bag(data, x, s))


def count_bag(data, bag):
    if not bag:
        return 1

    counts = [count_bag(data, data[b]) * int(c) for c, b in bag]
    return sum(counts) + 1


def partTwo(data):
    return count_bag(data, data[s]) - 1


if __name__ == "__main__":
    day = 7

    # Load Data
    data = utils.load_data("day%s.txt" % day)
    processed = process_data(data)

    # Do puzzle
    print("---- Day %s ----" % day)
    print("Part 1: " + str(partOne(processed)))
    print("Part 2: " + str(partTwo(processed)))
