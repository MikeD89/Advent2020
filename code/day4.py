import utils
import re

validEyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def processData(data):
    curr = ""
    retVal = []

    # fun to bank line
    def bank(line):
        # bank
        keyValue = line.strip().split(" ")
        d = dict(s.split(":") for s in keyValue)
        retVal.append(d)

    for line in data:
        curr += line + " "
        if not line:
            bank(curr)
            curr = ""

    # dont forget the last one
    bank(curr)

    return retVal


def checkNum(item, digits, min, max):
    return item.isnumeric() and \
        len(item) == digits and \
        int(item) >= min and \
        int(item) <= max


def isMeasurement(item: str):
    if item.endswith("cm") and item[:-2].isnumeric():
        return checkNum(item[:-2], 3, 150, 193)
    elif item.endswith("in") and item[:-2].isnumeric():
        return checkNum(item[:-2], 2, 59, 76)
    return False


def isColour(item: str):
    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', item)


def isFromArray(item: str, validValues):
    return item in validValues


def checkId(item: str):
    return len(item) == 9 and item.isnumeric()


def isValid(item):
    valid = "byr" in item and checkNum(item["byr"], 4, 1920, 2002) and \
        "iyr" in item and checkNum(item["iyr"], 4, 2010, 2020) and \
        "eyr" in item and checkNum(item["eyr"], 4, 2020, 2030) and \
        "hgt" in item and isMeasurement(item["hgt"]) and \
        "hcl" in item and isColour(item["hcl"]) and \
        "ecl" in item and isFromArray(item["ecl"], validEyes) and \
        "pid" in item and checkId(item["pid"])

    return valid


def partOne(data):
    return sum(1 for x in data if isValid(x))


if __name__ == "__main__":
    # Load Data
    data = utils.load_data("day4.txt")
    parsedData = processData(data)

    # Do puzzle
    print("---- Day 4 ----")

    # Part 1 no longer works, as the workings of the "isValid" method were improved
    print("Part 2: " + str(partOne(parsedData)))
