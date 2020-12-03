import utils

def processItem(line) :
    delims = "- :"
    retVal = []
    for d in delims:
        split = line.split(d, 1)
        retVal.append(split[0])
        line = split[1]

    retVal.append(line.strip())
    return retVal

def partOne(data) :
    valid = 0
    for n in data:
        l, u, k, p = processItem(n)
        count = utils.count_characters_in_string(p, k)
        if utils.int_in_range(count, l, u):
            valid += 1

    return valid

def partTwo(data) :
    valid = 0
    for n in data:
        p1, p2, k, p = processItem(n)
        if (p[int(p1) - 1] is k) ^ (p[int(p2) - 1] is k):
            valid += 1

    return valid

if __name__ == "__main__":
    # Load Data
    data = utils.load_data("day2.txt")

    # Do puzzle
    print("---- Day 2 ----")
    print("Part 1: " + str(partOne(data)))
    print("Part 2: " + str(partTwo(data)))