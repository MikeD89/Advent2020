import utils


def processItem(line):
    tree = '#'
    retVal = []
    line = line.strip()

    for x in line:
        retVal.append(x == tree)
    return retVal


def calcSlope(data, xStep, yStep):
    count = 0
    x = 0
    for y in range(0, len(data), yStep):
        row = data[y]
        width = len(row)
        if data[y][x % width]:
            count += 1
        x += xStep

    return count


def partOne(data):
    return calcSlope(data, 3, 1)


def partTwo(data):
    return \
        calcSlope(data, 1, 1) * \
        calcSlope(data, 3, 1) * \
        calcSlope(data, 5, 1) * \
        calcSlope(data, 7, 1) * \
        calcSlope(data, 1, 2)


if __name__ == "__main__":
    # Load Data
    data = utils.load_data("day3.txt")

    # Process it
    parsedData = []
    for line in data:
        parsedData.append(processItem(line))

    # Do puzzle
    print("---- Day 3 ----")
    print("Part 1: " + str(partOne(parsedData)))
    print("Part 2: " + str(partTwo(parsedData)))
