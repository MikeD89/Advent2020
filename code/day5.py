import utils
import math

rows = 127
cols = 7
maxSeat = (rows * 8) + cols


def bsp(line, minChar, maxChar, l, u, indexLower, indexUpper):
    for i in range(indexLower, indexUpper):
        d = (u - l) / 2
        if line[i] == minChar:
            u = u - math.ceil(d)
        elif line[i] == maxChar:
            l = l + math.floor(d)
        else:
            assert False
    return u


def processRow(line):
    return bsp(line, "F", "B", 0, rows, 0, 7)


def processCol(line):
    return bsp(line, "L", "R", 0, cols, 7, 10)


def processSeat(line):
    row = processRow(line)
    col = processCol(line)
    return (row * 8) + col


def partOne(data):
    m = 0
    for line in data:
        s = processSeat(line)
        m = s if s > m else m
    return m


def partTwo(data):
    # Get all availible seats
    seats = set(range(0, maxSeat))
    for line in data:
        seats.remove(processSeat(line))

    # Find our seat
    for i in seats:
        if i-1 not in seats and i+1 not in seats:
            return i

    return "UNKNOWN"


def testCase(line, eRow, eCol, eSNum):
    assert processRow(line) == eRow
    assert processCol(line) == eCol
    assert processSeat(line) == eSNum


def test():
    testCase("FFFFFFFLLL", 0, 0, 0)
    testCase("BBBBBBBRRR", rows, cols, maxSeat)
    testCase("FBFBBFFRLR", 44, 5, 357)
    testCase("BFFFBBFRRR", 70, 7, 567)
    testCase("FFFBBBFRRR", 14, 7, 119)
    testCase("BBFFBBFRLL", 102, 4, 820)
    print("Tests Pass!")


if __name__ == "__main__":

    # Load Data
    data = utils.load_data("day5.txt")

    # Process it
    parsedData = []

    # Do puzzle
    print("---- Day 5 ----")
    test()
    print()
    print("Part 1: " + str(partOne(data)))
    print("Part 2: " + str(partTwo(data)))
