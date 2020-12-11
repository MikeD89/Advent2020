from day10 import test
from utils import utils
from tests import day11_test as tests
import copy

empty = 'L'
occupied = '#'
floor = '.'

##################################################################################


class GameOfSeats:
    # The game of seats
    def __init__(self, data):
        self.delta = 4
        self.seatPlan = []
        for line in data:
            self.seatPlan.append([GameOfSeats.parse(seat) for seat in line])

    ################################
    def parse(value):
        if value == floor:
            return None
        else:
            return value == occupied

    ################################
    def _checkAdjancy(self, i, j):
        adjacent = []
        for iD in range(i-1, i+2):
            for jD in range(j-1, j+2):
                if iD == i and jD == j:
                    continue

                if iD < 0 or jD < 0 or jD >= len(self.seatPlan[i]) or iD >= len(self.seatPlan):
                    continue

                adjacent.append(self.seatPlan[iD][jD])

        return sum([seat for seat in adjacent if seat])

    ################################
    def cycle(self):
        newSeats = copy.deepcopy(self.seatPlan)

        for i in range(len(self.seatPlan)):
            for j in range(len(self.seatPlan[i])):
                # Calculate values
                c = self.seatPlan[i][j]
                a = self._checkAdjancy(i, j)
                if c == None:
                    continue

                # Check state
                if c == True:
                    # Check for death
                    if a >= self.delta:
                        newSeats[i][j] = False
                elif c == False:
                    # Check for new life
                    if a == 0:
                        newSeats[i][j] = True

        # Has it settled?
        same = (self.seatPlan == newSeats)
        self.seatPlan = newSeats
        return same

    ################################
    def count(self):
        count = 0
        for row in self.seatPlan:
            count += sum([seat for seat in row if seat])
        return count

    ################################
    def converge(self):
        # Just stop potnetial infinite loops
        getOutOfJail = 5000
        while(True):
            if self.cycle():
                return
            getOutOfJail -= 1
            assert getOutOfJail > 0

    ################################
    def printData(self):
        print("-----------------------------")
        for i in range(len(self.seatPlan)):
            for j in range(len(self.seatPlan[i])):
                # Calculate values
                c = self.seatPlan[i][j]
                print(str(c).rjust(6, " ") + " " + str(self._checkAdjancy(i, j)), end=' ')
            print()
        print("-----------------------------")

##################################################################################


class GameOfSeatsPartTwo(GameOfSeats):
    # The game of seats
    def __init__(self, data):
        super().__init__(data)
        self.delta = 5

     ################################
    def _checkAdjancy(self, i, j):
        vectors = [[-1, -1], [-1, +0], [-1, +1],
                   [+0, -1],           [+0, +1],
                   [+1, -1], [+1, +0], [+1, +1]]
        adjacent = []
        for vector in vectors:
            iD = i
            jD = j
            done = False
            while (not done):
                iD += vector[0]
                jD += vector[1]

                # edge check
                if iD < 0 or jD < 0 or jD >= len(self.seatPlan[i]) or iD >= len(self.seatPlan):
                    done = True
                    continue

                # empty check
                tester = self.seatPlan[iD][jD]
                if tester == None:
                    continue

                adjacent.append(tester)
                done = True

        return sum([seat for seat in adjacent if seat])

##################################################################################


def process(data):
    return data


def partOne(data):
    game = GameOfSeats(data)
    game.converge()
    return game.count()


def partTwo(data):
    game = GameOfSeatsPartTwo(data)
    game.converge()
    return game.count()


if __name__ == "__main__":
    utils.run(11, process, tests.test, partOne, partTwo)
