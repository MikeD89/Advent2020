import os
import time
from itertools import chain, combinations


def run(day, process, tests, part1, part2):
    data = load_data_by_day(day)
    processed = process(data)

    # Run
    tR = time_function(lambda: tests()) if tests is not None else None
    p1R = time_function(lambda: part1(processed)) if part1 is not None else None
    p2R = time_function(lambda: part2(processed)) if part2 is not None else None

    # Print
    print("----- Day %s -----" % day)
    if tR is not None:
        print("T  - {} -> {}".format(tR[1], tR[0]))
    if p1R is not None:
        print("P1 - {} -> {}".format(p1R[1], p1R[0]))
    if p2R is not None:
        print("P2 - {} -> {}".format(p2R[1], p2R[0]))


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


def join_string_line_sets_to_arrays(data):
    curr = []
    retVal = []

    # fun to bank line
    def bank(line):
        retVal.append(line)

    for line in data:
        if line:
            curr.append(line)
        if not line:
            bank(curr)
            curr = []

    # dont forget the last one
    bank(curr)

    return retVal


def time_function(f):
    before = time.time()
    ret = f()
    after = time.time()

    formatType = "ms"
    ms = (after-before)*1000.0
    if ms > 1000:
        formatType = "s"
        ms /= 1000

    timeString = '{:.0f} {}'.format(ms, formatType)
    return (ret, timeString)


def splitrange(hyphenString):
    x = [int(x) for x in hyphenString.split('-')]
    return range(x[0], x[-1]+1)


def load_test_data(tD):
    return tD.strip().splitlines()


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)))


def compare_list_any_order(l1, l2):
    return set(l1) == set(l2)
