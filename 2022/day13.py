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
    res = False
    mustBreak = False

    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) > 0:
            print("returning early here")
            res = True
            return res, True

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
                res, mustBreak = checkOrderCorrect(left[idx], right[idx])
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
                res, mustBreak = checkOrderCorrect(left[idx], [right[idx]])
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
                res, mustBreak = checkOrderCorrect([left[idx]], right[idx])
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
            #     print("smaller found set")


            if res == True:
                break

        # if len(left) < len(right) and res==True:
        #     return res


    return res, mustBreak

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
        res, _  = checkOrderCorrect(left, right)
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
