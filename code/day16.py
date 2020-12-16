import collections
from utils import utils
import math

tD = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

tD2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


def process(data):
    # COMMENT FOR TESTING
    # data = tD.strip().splitlines()
    #data = tD2.strip().splitlines()
    #

    data = utils.join_string_line_sets_to_arrays(data)

    rules = [[utils.splitrange(r) for r in d.split(": ")[1].split(" or ")] for d in data[0]]
    yourTicket = data[1][1].split(",")
    nearbyTickets = [[int(n) for n in d.split(",")] for d in data[2][1:]]

    return (rules, yourTicket, nearbyTickets)


def validateRule(rule, number):
    return bool(number in rule[0]) ^ bool(number in rule[1])


def validateNumber(rules, number):
    for rule in rules:
        if validateRule(rule, number):
            return True
    return False


def validateTicket(rules, ticket):
    for number in ticket:
        if not validateNumber(rules, number):
            return False
    return True


def getValidTickets(data):
    (rules, _, nearbyTickets) = data
    return [t for t in nearbyTickets if validateTicket(rules, t)]


def partOne(data):
    (rules, _, nearbyTickets) = data
    invalidNums = list()

    for ticket in nearbyTickets:
        for number in ticket:
            validNumber = validateNumber(rules, number)

            if not validNumber:
                invalidNums.append(number)

    return sum(invalidNums)


def findRule(i, rules, nearbyTickets):
    validRules = []
    for ruleI in range(len(rules)):
        rule = rules[ruleI]

        # Does this rule match the whole column?
        validRule = True
        for ticket in nearbyTickets:
            number = ticket[i]
            if not validateRule(rule, number):
                validRule = False
                break

        if validRule:
            validRules.append(ruleI)
    return validRules


def greedyRemove(data: list):
    retVal = collections.defaultdict(int)
    i = 0
    while len(retVal) != len(data):
        # If we find the single entry
        if len(data[i]) == 1:
            d = data[i][0]
            retVal[i] = d
            for v in data:
                if d in v:
                    v.remove(d)

        i = (i+1) % len(data)
    return retVal


def partTwo(data):
    (rules, yourTicket, nearbyTickets) = data
    nearbyTickets = getValidTickets(data)
    rulesOrder = [findRule(i, rules, nearbyTickets) for i in range(len(yourTicket))]
    rulesOrder = greedyRemove(rulesOrder)
    departure = [int(yourTicket[list(rulesOrder.keys())[list(rulesOrder.values()).index(i)]]) for i in range(6)]
    return math.prod(departure)


if __name__ == "__main__":
    utils.run(16, process, None, partOne, partTwo)
