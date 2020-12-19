import os

import itertools
from os.path import join

from numpy.lib.arraysetops import isin
from utils import utils
from collections import defaultdict
from numpy import array
from itertools import chain
from functools import reduce

tD = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
tMatch = ["010111", "011101"]


class MatchChecker:
    def __init__(self, data):
        self.data = utils.join_string_line_sets_to_arrays(data)
        self.rules = self.parseRules(self.data[0])
        self.input = self.parseInput(self.data[1])
        self.cache = dict()

    def parseInput(_, IN):
        retVal = list()
        for i in IN:
            i = i.replace("a", "0")
            i = i.replace("b", "1")
            retVal.append(i)
        return retVal

    def parseRules(_, IN):
        retVal = defaultdict(int)
        for r in IN:
            split = r.split(":")
            index = split[0]
            rules = split[1]

            if "a" in rules:
                rules = "0"
            elif "b" in rules:
                rules = "1"
            else:
                rules = [[int(c) for c in s.strip().split()] for s in rules.split("|")]
            retVal[int(index)] = rules
        return retVal

    def fufilRule(self, index):
        # Is it cached?
        if index in self.cache:
            return self.cache[index]

        rule = self.rules[index]

        # If its a string, its data
        if isinstance(rule, str):
            return rule

        # Recurse!
        found = [self.fufilPart(p) for p in rule]

        allChars = True
        for a in found:
            if isinstance(a, list):
                allChars = False
        if not allChars:
            found = [item for sublist in found for item in sublist]

        # Squeeze it down
        if len(array(found, dtype=object).shape) > 1:
            found = [item for sublist in found for item in sublist]

        return found

    def fufilPart(self, part):
        result = [self.fufilRule(b) for b in part]
        if isinstance(result, str):
            return result

        resultShape = array(result, dtype=object).shape

        if len(resultShape) == 1:
            allChars = True
            for r in result:
                if not isinstance(r, str):
                    allChars = False

            if allChars:
                return ''.join(result)

        joined = list(itertools.product(*result))
        joined = [''.join(j) for j in joined]

        return joined

    def getValidInput(self, rule):
        parsedRule = self.fufilRule(rule)
        validInput = [i for i in self.input if i in parsedRule]
        return validInput


def test():
    testData = [line for line in tD.splitlines()][1:]
    vI = MatchChecker(testData).getValidInput(0)

    assert utils.compare_list_any_order(vI, tMatch)
    assert len(tMatch) == 2
    return "Pass!"


if __name__ == "__main__":
    day = os.path.basename(__file__)[3:5]

    def process_data(d): return d
    def partOne(d): return len(MatchChecker(d).getValidInput(0))
    def partTwo(d): return MatchChecker(d).findMatches(0)

    utils.run(day, process_data, test, partOne, None)
