from utils import utils
from math import prod


def parse(i):
    if i == "x":
        return None
    return int(i)


def process(data):
    #data = ["939", "7,13,x,x,59,x,31,19"]
    return data


def partOne(data):
    times = data[1].split(",")
    times = [parse(t) for t in times]
    times = [t for t in times if t]

    earliest = int(data[0])

    curr = 0
    while True:
        curr += 1
        if curr < earliest:
            continue
        for t in times:
            if curr % t == 0:
                wait = curr - earliest
                return t * wait


def crt(n, a):
    # Based on: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
    t = 0
    p = prod(n)
    for n_i, a_i in zip(n, a):
        t += a_i * pow(p // n_i, -1, n_i) * (p // n_i)
    return t % p


def partTwo(data):
    times = [parse(d) for d in data[1].split(",")]
    times = [(t, t-i) for i, t in enumerate(times) if t]
    return crt([t[0] for t in times], [t[1] for t in times])


if __name__ == "__main__":
    utils.run(13, process, None, partOne, partTwo)
