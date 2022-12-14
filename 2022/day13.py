from collections import deque
import ast
from itertools import islice

def readInput(filename):
    with open(filename, 'r') as f:
        pairs = []
        while True:
            next_3_lines = list(islice(f, 3))
            if not next_3_lines:
                break
            pair = []
            for line in next_3_lines[:2]:
                line = line.strip()
                parsed = ast.literal_eval(line)
                pair.append(parsed)
            pairs.append(pair)

    return pairs

def checkOrderCorrect(left, right):
    print(f"Compare left: {left} and right: {right}")
    res = True
    smallerFound = False
    if isinstance(left, list) and isinstance(right, list):
        # Check all elements
        for idx in range(len(left)):
            if idx >= len(right):
                if len(right):
                    if right[-1] == left[idx]:
                        res &= False
                    else:
                        res &= True
                else:
                    res &= False
                break

            print(f"\tCompare {left[idx]} vs {right[idx]}")

            if isinstance(left[idx], list) and isinstance(right[idx], list):
                ret, smallerFound = checkOrderCorrect(left[idx], right[idx])
                res &= ret
                if res == True: # todo this is broken
                    break
            elif isinstance(left[idx], list) and isinstance(right[idx], int):
                ret, smallerFound = checkOrderCorrect(left[idx], [right[idx]])
                res &= ret
            elif isinstance(left[idx], int) and isinstance(right[idx], list):
                ret, smallerFound = checkOrderCorrect([left[idx]], right[idx])
                res &= ret
            elif isinstance(left[idx], list) and isinstance(right[idx], int):
                ret, smallerFound = checkOrderCorrect(left[idx], [right[idx]])
                res &= ret
            elif left[idx] > right[idx]:
                res &= False
            elif left[idx] < right[idx]:
                smallerFound = True
            #     print("smaller found set")

            if res == False or smallerFound == True:
                break


    return res, smallerFound

def part1(pairs):
    correctOrder = []
    for idx, pair in enumerate(pairs):
        left, right = pair
        print(f"left: {left}, right: {right}")
        res, _ = checkOrderCorrect(left, right)
        print(f"result: {res}\n\n")
        if res == True:
            correctOrder.append(idx + 1)

    print(f"correct order indexes: {correctOrder}")
    print(f"Sum of correct order: {sum(correctOrder)}")

def main():
    # lines = readInput('example.txt')
    # lines = readInput('input.txt')
    # lines = readInput('inputKarl.txt')
    lines = readInput('problemChild.txt')
    # lines = readInput('smallerTest.txt')
    print("Part 1")
    part1(lines)
    print("Part 2")

    # for idx, pair in enumerate(lines):
    #     print(f"idx: {idx}\n")
    #     left, right = pair
    #     print(left)
    #     print(right)
    #     print("\n")

if __name__ == '__main__':
    main()
