import sys
from collections import deque
import numpy as np

infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]

smallestX, smallestY = sys.maxsize, sys.maxsize
largestX, largestY = 0, 0

paths = []
for line in lines:
    path = []
    coords = line.split(' -> ')
    for coord in coords:
        x, y = coord.split(',')
        path.append((int(x), int(y)))
        smallestX = min(int(x), smallestX)
        smallestY = min(int(y), smallestY)
        largestX = max(int(x), largestX)
        largestY = max(int(y), largestY)
    paths.append(path)

# cave = np.zeroes((largestX, largestY))
# Cave must be indexed by [y][x]
cave = [['.' for x in range(largestX+1)] for y in range(largestY+1)]
sandStart = (500, 0)
cave[0][500] = '+'

def swap(left, right):
    tmp = left
    left = right
    right  = tmp
    return left, right

for path in paths:
    for pair in zip(path, path[1:]):
        start, end = pair
        if start[0] == end[0]: # Move along y axis
            a, b = start[1], end[1]
            if a > b:
                a, b = swap(a,b)
            for y in range(a, b+1):
                cave[y][start[0]] = '#'
        else: # Move along x axis
            a, b = start[0], end[0]
            if a > b:
                a, b = swap(a,b)
            for x in range(a, b+1):
                cave[start[1]][x] = '#'

def printRange(matrix, xMin, xMax, yMin, yMax):
    for line in matrix[yMin:yMax+1]:
        print(line[xMin:xMax+1])

offset = 5
print("Starting Cave:")
printRange(cave, smallestX-offset, largestX+offset, 0, largestY+offset)

# Update the sand in the cave or return False if it flowed into the abyss
def simulateSand(location):
    global cave

    x, y = location
    print(f"Starting with x: {x}, y: {y}")
    # if y <= len(cave)-1: # On/ Past the Botttom
    #     print(f"In the abyss! y: {y}, x: {x}")
    #     return False

    while y <= len(cave) - 2:
        print(f"While loop iteration. x: {x}, y: {y}")
        if cave[y+1][x] in ['#', 'o']:
            print("1")
            cave[y][x] = 'o'
            return True
        elif cave[y+1][x-1] in ['#', 'o']:
            print("2")
            cave[y][x-1] = 'o'
            return True
        elif cave[y+1][x+1] in ['#', 'o']:
            print("3")
            cave[y][x+1] = 'o'
            return True

        # Todo does this need to happen before setting?
        if cave[y+1][x] == '.':
            y += 1
            print(f"increasing y by 1 to: {y}")
        elif cave[y+1][x-1] == '.':
            y += 1
            x -= 1
        else:
            y += 1
            x += 1

    print(f"In the abyss! y: {y}, x: {x}")
    return False

print(cave[9][502])

i = 0
# while simulateSand(sandStart) != False:
# while True
for i in range(5):
    if simulateSand(sandStart) == False:
        break
    print(f"Cave at {i} iteration")
    printRange(cave, smallestX-offset, largestX+offset, 0, largestY+offset)
    i += 1


