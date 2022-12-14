from collections import deque
import ast
from itertools import islice
from functools import cmp_to_key

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
    res = False
    mustBreak = False
    equal = False

    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            print("returning early here")
            res = True
            return res, True, equal

        if len(left) == 0 and len(right) == 0:
            res = True

        # if len(left) == 1 and len(right) == 1:
        #     if left[0] == right[0]:
        #         res = False
        #         mustBreak = True
        #         return res, mustBreak

        # Check all elements
        for idx in range(len(left)):
            print(f"idx: {idx}")
            if idx >= len(right):
                res = False
                mustBreak = True
                # print(f"hereee, res: {res}")
                # if len(right):
                #     if right[-1] == left[idx]:
                #         res = False
                #     else:
                #         res = True
                # else:
                #     res = False
                break

            print(f"\tCompare {left[idx]} vs {right[idx]}")
            # print(f"left: {left}, right: {right}")

            if isinstance(left[idx], list) and isinstance(right[idx], list):
                res, mustBreak, equal = checkOrderCorrect(left[idx], right[idx])
                # print("here1")
                # print(f"left: {left}, right: {right}, idx: {idx}")
                if mustBreak:
                    print("breaking 1")
                    break

                # print("returning here")
                # if len(left) < len(right) and res == True:
                #     print("breaking because len left is less")
                #     break
            elif isinstance(left[idx], list) and isinstance(right[idx], int):
                res, mustBreak, equal = checkOrderCorrect(left[idx], [right[idx]])
                # print("here2")
                if mustBreak:
                    print("breaking 2")
                    break

                # print("returning 2")
                # print(f"left: {left}, right: {right}")
                # if len(left) < len([right]) and res == True:
                #     print("here 2")
                #     break
            elif isinstance(left[idx], int) and isinstance(right[idx], list):
                res, mustBreak, equal = checkOrderCorrect([left[idx]], right[idx])
                # print("here3")
                if mustBreak:
                    # print("breaking 3")
                    break

                # if len([left]) < len(right) and res == True:
                #     break
            # elif isinstance(left[idx], list) and isinstance(right[idx], int):
            #     ret, smallerFound = checkOrderCorrect(left[idx], [right[idx]])
            #     res &= ret

            #     if len(left) < len([right]):
            #         break
            elif left[idx] > right[idx]:
                # print("here 4")
                res = False
                mustBreak = True
                break
            elif left[idx] < right[idx]:
                # print("here 5")
                res = True
            else: # equal
                print("here 6")
                if idx == len(left) - 1 and len(left) < len(right):
                    print("here 7")
                    res = True
                    equal = True
            #     print("smaller found set")


            if res == True:
                break

        # if len(left) < len(right) and res==True:
        #     return res


    return res, mustBreak, equal

# Return -1 if left < right
# Return 0 if left == right
# Return 1 if left > right
# This function mostly adapted from https://raw.githubusercontent.com/jonathanpaulson/AdventOfCode/master/2022/13.py
# This comparison function is necessary for part 2 because you need to know when they are equal
# to get the correct number
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            c = compare(left[i], right[i])
            if c == -1 or c == 1:
                return c
            i += 1
        if i == len(left) and i < len(right):
            return -1
        elif i == len(right) and i < len(left):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    else:
        return compare(left, [right])

def part2(pairs):
    packets = []
    for pair in pairs:
        left, right = pair
        packets.append(left)
        packets.append(right)
    packets.append([[2]])
    packets.append([[6]])

#     def compare(left, right):
#         res, _, equal = checkOrderCorrect(left, right)
#         if equal == True:
#             return 0
#         elif res:
#             return -1
#         else:
#             return 1

    sortedList = sorted(packets, key=cmp_to_key(compare))
    print(sortedList)

    ans = 1
    for idx,item in enumerate(sortedList):
        print(item)
        if item == [[2]] or item == [[6]]:
            ans *= (idx+1)

    print(f"Answer: {ans}")

def part1(pairs):
    # print(f"pair 50")
    # print(f"{pairs[49][0]}")
    # print(f"{pairs[49][1]}")
    # print(f"\npair 63")
    # print(f"{pairs[62][0]}")
    # print(f"{pairs[62][1]}")
    # return
    correctOrder = []
    for idx, pair in enumerate(pairs):
        left, right = pair
        print(f"left: {left}, right: {right}")
        res, _, _  = checkOrderCorrect(left, right)
        print(f"result: {res}\n\n")
        if res == True:
            correctOrder.append(idx + 1)

    print(f"correct order indexes: {correctOrder}")
    print(f"Sum of correct order: {sum(correctOrder)}")

def main():
    # lines = readInput('example.txt')
    lines = readInput('input.txt')
    # lines = readInput('inputKarl.txt')
    # lines = readInput('problemChild.txt')
    # lines = readInput('smallerTest.txt')
    print("Part 1")
    # part1(lines)
    print("Part 2")
    part2(lines)

    # for idx, pair in enumerate(lines):
    #     print(f"idx: {idx}\n")
    #     left, right = pair
    #     print(left)
    #     print(right)
    #     print("\n")

if __name__ == '__main__':
    main()
