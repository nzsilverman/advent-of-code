from collections import deque
from itertools import islice
import math

class Monkey():
    def __init__(self):
        self.number = None
        self.items = deque()
        self.updateFunc = None
        self.left = None
        self.right = None
        self.operator = None
        self.testFunc = None
        self.modulus = None
        self.trueMonkey = None
        self.falseMonkey = None
        self.numItemsInspected = 0

    def __str__(self):
        string = f"\nMonkey {self.number}\n"
        string += f"\titems: {self.items}\n"
        string += f"\ttrueMonkey: {self.trueMonkey}\n"
        string += f"\tfalseMonkey: {self.falseMonkey}\n"
        string += f"\tleft: {self.left}\n"
        string += f"\tright: {self.right}\n"
        string += f"\toperator: {self.operator}\n"
        string += f"\tmodulus: {self.modulus}\n"
        string += f"\tnumItemsInspected: {self.numItemsInspected}\n"
        return string

def readInput(filename):
    monkeys = {}
    with open(filename, 'r') as f:
        while True:
            monkeyLines = list(islice(f, 7))
            monkeyLines = [x.strip() for x in monkeyLines]
            if not monkeyLines:
                break

            number = int(monkeyLines[0][:-1].split()[1])
            items = deque([int(x) for x in monkeyLines[1].split('Starting items: ')[1].split(', ')])
            left, operator, right = monkeyLines[2].split('Operation: new = ')[1].split()
            if operator == '+':
                updateFunc = lambda old: (old if str(left)=='old' else int(left)) + (old if str(right)=='old' else int(right))
            elif operator == '*':
                updateFunc = lambda old: (old if str(left)=='old' else int(left)) * (old if str(right)=='old' else int(right))


            modulus = int(monkeyLines[3].split('Test: divisible by ')[1])
            testFunc = lambda x: x % modulus == 0
            trueMonkey = int(monkeyLines[4].split('If true: throw to monkey ')[1])
            falseMonkey = int(monkeyLines[5].split('If false: throw to monkey ')[1])

            monkey = Monkey()
            monkey.number = number
            monkey.items = items
            monkey.updateFunc = updateFunc
            monkey.testFunc = testFunc
            monkey.trueMonkey = trueMonkey
            monkey.falseMonkey = falseMonkey
            monkey.left = left
            monkey.right = right
            monkey.operator = operator
            monkey.modulus = modulus

            monkeys[number] = monkey
            dbgPrint(f"monkey number: {number}")
            x = 79
            y = monkey.updateFunc(x)
            dbgPrint(y)
            dbgPrint(monkey.updateFunc(x))
            dbgPrint(monkeys[number].updateFunc(x))

    return monkeys

def update(old, left, right, operator):
    left = old if str(left)=='old' else int(left)
    right = old if str(right)=='old' else int(right)
    if operator == '+':
        return left + right
    elif operator == '*':
        return left * right

VERBOSE=False
def dbgPrint(string):
    global VERBOSE
    if VERBOSE:
        dbgPrint(string)


def simulateRound(monkeys, part1):
    for i in range(len(monkeys)):
        # dbgPrint(f"Monkey {i}:")
        monkey = monkeys[i]
        for item in monkey.items:
            # dbgPrint(f"\tMonkey inspects an item with a worry level of {item}.")
            # new = monkey.updateFunc(item) # Todo why does lambda not work?
            monkey.numItemsInspected += 1
            new = update(item, monkey.left, monkey.right, monkey.operator)
            # dbgPrint(f"\t\tWorry level is updated to {new}")
            if part1:
                new = int(math.floor(new / 3))
            # dbgPrint(f"\t\tWorry level is divided by 3 to be: {new}")

            # if monkey.testFunc(new):
            if new % monkey.modulus == 0:
                # dbgPrint(f"\t\tItem is divisible, being thrown to monkey {monkey.trueMonkey}")
                monkeys[monkey.trueMonkey].items.append(new)
            else:
                # dbgPrint(f"\t\tItem is not divisible, being thrown to monkey {monkey.falseMonkey}")
                monkeys[monkey.falseMonkey].items.append(new)
        monkey.items = deque()

def part1(monkeys):
    for i in range(20):
        simulateRound(monkeys, True)

    numInspected = []
    for key in monkeys.keys():
        dbgPrint(monkeys[key])
        numInspected.append(monkeys[key].numItemsInspected)

    numInspected.sort(reverse=True)

    print(f"Part 1 answer: Monkey Business Score: {numInspected[0] * numInspected[1]}")

def optimizedSimulation(monkeys, commonDenom):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for item in monkey.items:
            monkey.numItemsInspected += 1
            new = update(item, monkey.left, monkey.right, monkey.operator)
            new = new % commonDenom

            if new % monkey.modulus == 0:
                monkeys[monkey.trueMonkey].items.append(new)
            else:
                monkeys[monkey.falseMonkey].items.append(new)
        monkey.items = deque()

def part2(monkeys):
    commonDenom = 1
    for monkey in monkeys.values():
        commonDenom = int((commonDenom * monkey.modulus) / math.gcd(commonDenom, monkey.modulus))
    for i in range(10000):
    # for i in range(20):
        print(f"Round: {i}")
        optimizedSimulation(monkeys, commonDenom)

    numInspected = []
    for key in monkeys.keys():
        dbgPrint(monkeys[key])
        numInspected.append(monkeys[key].numItemsInspected)

    numInspected.sort(reverse=True)
    print(numInspected)

    print(f"Part 2 answer: Monkey Business Score: {numInspected[0] * numInspected[1]}")

def main():
    # monkeys = readInput('example.txt')
    monkeys = readInput('input.txt')
    # part1(monkeys)
    part2(monkeys)




if __name__ == '__main__':
    main()
