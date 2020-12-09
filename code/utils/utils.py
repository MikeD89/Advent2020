import os
import time


def run(day, process, tests, part1, part2):
    data = load_data_by_day(day)
    processed = process(data)

    # Run
    tR = time_function(lambda: tests()) if tests is not None else None
    p1R = time_function(lambda: part1(processed))
    p2R = time_function(lambda: part2(processed))

    # Print
    print("----- Day %s -----" % day)
    if tR is not None:
        print("Tests  ({}) -> {}".format(tR[1], tR[0]))
    print("Part 1 ({}) -> {}".format(p1R[1], p1R[0]))
    print("Part 2 ({}) -> {}".format(p2R[1], p2R[0]))


def get_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def get_input_dir() -> str:
    return os.path.realpath(os.path.join(get_dir(), "..\input"))


def load_data_by_day(day):
    return load_data("day%s.txt" % day)


def load_data(data):
    path = os.path.realpath(os.path.join(get_input_dir(), data))
    with open(path, 'r') as file:
        return file.read().splitlines()


def convert_string_data_to_ints(data):
    return [int(numeric_string) for numeric_string in data]


def count_characters_in_string(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


def int_in_range(num, low, max):
    return num >= int(low) and num <= int(max)


def join_string_line_sets_to_map(data):
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


def join_string_line_sets_to_strings(data):
    curr = ""
    retVal = []

    # fun to bank line
    def bank(line):
        retVal.append(line)

    for line in data:
        curr += line + " "
        if not line:
            bank(curr)
            curr = ""

    # dont forget the last one
    bank(curr)

    return retVal


def time_function(f):
    before = time.time()
    ret = f()
    after = time.time()
    timeString = '{:.3f} ms'.format((after-before)*1000.0)
    return (ret, timeString)