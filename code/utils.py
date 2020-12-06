import os


def get_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def get_input_dir() -> str:
    return os.path.realpath(os.path.join(get_dir(), "..\input"))


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
