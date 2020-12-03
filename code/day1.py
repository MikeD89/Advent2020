import utils

def partOne(data) :
    for n in data:
        partner = 2020 - n 
        if partner in data:
            return str(partner * n)

def partTwo(data) :
    for n in data:
        for i in data:
            partner = 2020 - n - i
            if partner in data:
                return str(partner * n * i)

if __name__ == "__main__":
    # Load Data
    data = utils.load_data("day1.txt")
    nums = utils.convert_string_data_to_ints(data)

    # Do puzzle
    print("---- Day 1 ----")
    print("Part 1: " + partOne(nums))
    print("Part 2: " + partTwo(nums))