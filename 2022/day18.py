import sys
from collections import deque
import matplotlib.pyplot as plt
import math

infile = sys.argv[1] if len(sys.argv)>1 else '18.input'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]
xyzPairs = [x.split(',') for x in lines]
xyzPairs = [[int(x) for x in line] for line in xyzPairs]

def plot():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for line in xyzPairs:
        x,y,z = line
        ax.scatter(x, y, z)

    plt.show()
# plot()

def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2)* 1.0)
    return d

def part1():
    sidesExposed = 0
    for outer in xyzPairs:
        numNeighbors = 0
        x1, y1, z1 = outer
        for inner in xyzPairs:
            x2, y2, z2 = inner
            if outer == inner:
                continue

            if distance(x1, y1, z1, x2, y2, z2) == 1:
                numNeighbors += 1
        assert(numNeighbors <= 6)
        sidesExposed += (6 - numNeighbors)

    print(f"sidesExposed: {sidesExposed}")

# part1()


def part2():
    sidesExposed = 0
    pointToTwoAway = 0
    for outer in xyzPairs:
        numNeighbors = 0
        x1, y1, z1 = outer
        for inner in xyzPairs:
            x2, y2, z2 = inner
            if outer == inner:
                continue

            if distance(x1, y1, z1, x2, y2, z2) == 1:
                numNeighbors += 1
            elif distance(x1, y1, z1, x2, y2, z2) == 2:
                # Todo find a way to store this info
                continue
        assert(numNeighbors <= 6)
        sidesExposed += (6 - numNeighbors)

    print(f"sidesExposed: {sidesExposed}")
part2()
