from utils import utils
import day11


def partOneTest(data):
    games = [day11.GameOfSeats(game) for game in data[1:]]
    tester = day11.GameOfSeats(data[0])
    for game in games:
        assert not tester.cycle()
        assert tester.seatPlan == game.seatPlan

    assert tester.cycle()
    assert tester.count() == 37
    assert tester.seatPlan == games[-1].seatPlan


def partTwoTest(data):
    games = [day11.GameOfSeatsPartTwo(game) for game in data[1:]]
    tester = day11.GameOfSeatsPartTwo(data[0])

    for game in games:
        assert not tester.cycle()
        assert tester.seatPlan == game.seatPlan

    assert tester.cycle()
    assert tester.count() == 26
    assert tester.seatPlan == games[-1].seatPlan


def test():
    # Data
    p1 = utils.load_data("tests/day11_part1.txt")
    p2 = utils.load_data("tests/day11_part2.txt")

    partOneTest(utils.join_string_line_sets_to_arrays(p1))
    partTwoTest(utils.join_string_line_sets_to_arrays(p2))

    return "Pass!"
