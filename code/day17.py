from utils import utils
import numpy as np
from scipy.signal import convolve

day = 17

tD = """
.#.
..#
###
"""

active = '#'
inactive = '.'


class DimentionalConway:
    # The game of seats
    def __init__(self, data, dimensions):
        self.dimensions = dimensions

        # Load the data into numpy
        def parse(x): return x == active
        self.data = np.array([list(d) for d in data])
        self.data = parse(self.data).astype(int)

        # already 2d, expand to N dimensions
        for _ in range(dimensions - 2):
            self.data = np.expand_dims(self.data, 0)

        # create a kernel based on N dimensions - make us have no weight
        self.kernel = np.ones((3, )*dimensions, dtype=int)
        self.kernel[(1, )*dimensions] = 0

    def cycle(self):
        # Add room for our data to grow
        self.data = np.pad(self.data, pad_width=1, mode='constant', constant_values=False)

        # Convolve our kernal
        neighbors = convolve(self.data, self.kernel, mode='same')

        # Work our which to set active and inactive before changing the data
        neighbour_check = np.logical_or(neighbors < 2, neighbors > 3)
        active = np.logical_and(self.data == 0, neighbors == 3)
        inactive = np.logical_and(self.data == 1, neighbour_check)

        # Set up data!
        self.data[active] = 1
        self.data[inactive] = 0

    def count(self):
        return np.sum(self.data)

    def iterate(self, times):
        for _ in range(times):
            self.cycle()
        return self.count()


def process_data(data):
    # data = utils.load_test_data(tD)
    return data


def partOne(data):
    game = DimentionalConway(data, 3)
    game.iterate(6)
    return game.count()


def partTwo(data):
    game = DimentionalConway(data, 4)
    game.iterate(6)
    return game.count()


if __name__ == "__main__":
    utils.run(day, process_data, None, partOne, partTwo)
