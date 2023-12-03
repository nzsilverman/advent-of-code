import sys
from collections import deque

def PrintRed(skk, end="\n"): PrintDebug("\033[91m{}\033[00m".format(skk), end=end)
def PrintGreen(skk, end="\n"): PrintDebug("\033[92m{}\033[00m".format(skk), end=end)
def PrintYellow(skk, end="\n"): PrintDebug("\033[93m{}\033[00m".format(skk), end=end)
def PrintLightPurple(skk, end="\n"): PrintDebug("\033[94m{}\033[00m".format(skk), end=end)

DEBUG=0
def PrintDebug(skk="", end="\n"):
    if DEBUG:
        print(skk, end=end)

def CharIsSymbol(char):
    return char != '.' and not char.isnumeric()

def PrintMatrix(matrix, char_indices):
    for y_idx, line in enumerate(matrix):
        for x_idx, char in enumerate(line):
            if (x_idx, y_idx) in char_indices:
                PrintGreen(char, end="\t")
            else:
                PrintDebug(char, end="\t")
        PrintDebug()

def FindSymbolIndices(matrix):
    indices = []
    for y_idx, line in enumerate(matrix):
        for x_idx, char in enumerate(line):
            if CharIsSymbol(char):
                indices.append((x_idx, y_idx))

    return indices

def FindSymbolIndicesPart2(matrix):
    indices = []
    for y_idx, line in enumerate(matrix):
        for x_idx, char in enumerate(line):
            if char == "*":
                indices.append((x_idx, y_idx))

    return indices

def InBounds(x, y, xSize, ySize):
    if x < 0 or x > xSize-1:
        return False

    if y < 0 or y > ySize-1:
        return False

    return True


def FindEntireNumber(matrix, x_start, y_start):
    x_first = x_start
    x_end = x_start

    xSize = len(matrix[0])
    ySize = len(matrix)

    while InBounds(x_first-1, y_start, xSize, ySize) and matrix[y_start][x_first-1].isnumeric():
        x_first-=1

    while InBounds(x_end+1, y_start, xSize, ySize) and matrix[y_start][x_end+1].isnumeric():
        x_end+=1

    return (x_first, x_end, y_start)

def NumberNotationToNumber(matrix, x_first, x_end, y):
    return int(''.join(matrix[y])[x_first:x_end+1])

def GetAdjacentIndices(matrix, x, y):
    xSize = len(matrix[0])
    ySize = len(matrix)

    adjacent = []

    if InBounds(x - 1, y, xSize, ySize):
        adjacent.append((x-1, y))
    if InBounds(x + 1, y, xSize, ySize):
        adjacent.append((x+1, y))
    if InBounds(x, y-1, xSize, ySize):
        adjacent.append((x, y-1))
    if InBounds(x, y+1, xSize, ySize):
        adjacent.append((x, y+1))
    if InBounds(x - 1, y-1, xSize, ySize):
        adjacent.append((x-1, y-1))
    if InBounds(x - 1, y+1, xSize, ySize):
        adjacent.append((x-1, y+1))
    if InBounds(x + 1, y-1, xSize, ySize):
        adjacent.append((x+1, y-1))
    if InBounds(x + 1, y+1, xSize, ySize):
        adjacent.append((x+1, y+1))

    return adjacent

def Part1(matrix):
    symbol_indices = FindSymbolIndices(matrix)

    adjacent_nums_set = set()
    for x_idx, y_idx in symbol_indices:
        adjacent = GetAdjacentIndices(matrix, x_idx, y_idx)
        PrintMatrix(matrix, adjacent)

        for x_adj, y_adj in adjacent:
            if matrix[y_adj][x_adj].isnumeric():
                num_found = FindEntireNumber(matrix, x_adj, y_adj)
                adjacent_nums_set.add(num_found)


    engine_sum = 0
    for paramaterized_num in adjacent_nums_set:
        engine_sum += NumberNotationToNumber(matrix, paramaterized_num[0], paramaterized_num[1], paramaterized_num[2])

    print(f"Part 1 answer: {engine_sum}")

def Part2(matrix):
    answer = 0
    symbol_indices = FindSymbolIndicesPart2(matrix)

    for x_idx, y_idx in symbol_indices:
        adjacent = GetAdjacentIndices(matrix, x_idx, y_idx)

        adjacent_nums_set = set()
        for x_adj, y_adj in adjacent:
            if matrix[y_adj][x_adj].isnumeric():
                num_found = FindEntireNumber(matrix, x_adj, y_adj)
                adjacent_nums_set.add(num_found)

        if len(adjacent_nums_set) == 2:
            nums = []
            for item in adjacent_nums_set:
                num = NumberNotationToNumber(matrix, item[0], item[1], item[2])
                nums.append(num)

            assert len(nums) == 2
            gear_ratio = nums[0] * nums[1]
            answer += gear_ratio



    print(f"Part 2 answer: {answer}")


def main():
    infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    data = open(infile).read().strip()
    lines = [line for line in data.split('\n')]
    matrix = []

    for line in lines:
        char_list = [char for char in line]
        matrix.append(char_list)

    # Part1(matrix)
    Part2(matrix)


if __name__ == '__main__':
    main()
