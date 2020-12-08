from utils import utils
import string


def process_data(data):
    return utils.join_string_line_sets_to_strings(data)


def partOne(data):
    sum = 0
    for line in data:
        unique = set(line.replace(" ", ""))
        sum += len(unique)
    return sum


def partTwo(data):
    sum = 0
    for line in data:
        answers = line.split(" ")
        filtered_answers = [set(x) for x in answers if len(x) != 0]
        letters = set(string.ascii_lowercase)
        for x in filtered_answers:
            letters = letters.intersection(x)

        sum += len(letters)
    return sum


if __name__ == "__main__":
    day = 6

    # Load Data
    data = utils.load_data("day%s.txt" % day)
    processed = process_data(data)

    # Do puzzle
    print("---- Day %s ----" % day)
    print("Part 1: " + str(partOne(processed)))
    print("Part 2: " + str(partTwo(processed)))
