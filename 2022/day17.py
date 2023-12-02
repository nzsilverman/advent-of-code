import sys
from collections import deque
import copy

infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
jetPattern = open(infile).read().strip()

rocks = []
one = [["#", "#", "#", "#"]]

two = [[".", "#", "."],
       ["#", "#", "#"],
       [".", "#", "."]]

three = [[".", ".", "#"],
         [".", ".", "#"],
         ["#", "#", "#"]]

four =  [["#"],
         ["#"],
         ["#"],
         ["#"]]

five =  [["#", "#"],
         ["#", "#"]]

rocks.extend([one, two, three, four, five])

# rockLeftX is the location of the left side of the rock
# rockBottomY is the location of the bottom of the rock
def checkIfRockHitsAnything(tower, rock, rockLeftX, rockBottomY, direction):
    # for colIdx in range(len(rock)-1, -1, -1):
    for colIdx in range(len(rock)):
        towerY = rockBottomY + (len(rock) - colIdx - 1)

        for rowIdx in range(len(rock[0])):
            towerX = rockLeftX + rowIdx
            if direction == 'left':
                if towerX - 1 < 0:
                    return True

                if towerY < len(tower) and tower[towerY][towerX-1] == '#' and rock[colIdx][rowIdx] == '#':
                    return True
            elif direction == 'right':
                if towerX + 1 >= len(tower[0]):
                    return True

                if towerY < len(tower) and tower[towerY][towerX+1] == '#' and rock[colIdx][rowIdx] == '#':
                    return True
            elif direction == 'down':
                if towerY <= len(tower):
                    if tower[towerY-1][towerX] in ['-', '#'] and rock[colIdx][rowIdx] == '#':
                        return True
    return False

# Return a list of depths representing the distance below the top of the tower
def getFloorDepths(tower):
    depths = []
    for rowIdx in range(len(tower[0])):
        y = len(tower) - 1
        while True:
            if tower[y][rowIdx] in ['-', '#']:
                depths.append(len(tower) - 1 - y)
                break
            y -= 1
    return (depths[0], depths[1], depths[2], depths[3], depths[4], depths[5], depths[6])

def simulateRocks(numRocksToFall, findJetPatternCyclesBeforeRepeat=False, towerIn=None):
    towerWidth = 7
    tower = [['-' for x in range(towerWidth)]] if towerIn == None else towerIn
    jetIdx = 0
    depthsPerPatternCycle = []
    depthToRockNum = {}

    for rockNum in range(numRocksToFall):
        if rockNum % 100000:
            print(f"{rockNum} rocks have fallen")
        rock = rocks[rockNum % len(rocks)]
        x = 2 # Where is left side of rock
        y = len(tower) + 3

        while True:
            if findJetPatternCyclesBeforeRepeat and jetIdx % len(jetPattern) == 0:
                depths = getFloorDepths(tower)
                # print(f"depths: {depths}")

                if depths in depthsPerPatternCycle:
                    # print(f"depths already in depthsPerPatternCycle!!")
                    # print(f"depthsPerPatternCycle: {depthsPerPatternCycle}")
                    # print(f"depths: {depths}")
                    return depthToRockNum[depths], rockNum - depthToRockNum[depths]
                else:
                    depthsPerPatternCycle.append(depths)
                    depthToRockNum[depths] = rockNum


            jetDir = jetPattern[jetIdx % len(jetPattern)]
            jetIdx += 1
            # Shift left/ right
            if jetDir == '<' and not checkIfRockHitsAnything(tower, rock, x, y, "left"):
                # print("Moving left")
                x -= 1
            # elif jetDir == '<':
            #     print("Skipping moving left")
            elif jetDir == '>' and not checkIfRockHitsAnything(tower, rock, x, y, "right"):
                # print("Moving right")
                x += 1
            # else:
            #     print("Skipping moving right")

            # Move down if possible, else come to rest
            rockHitsSomething = checkIfRockHitsAnything(tower, rock, x, y, "down")

            if not rockHitsSomething:
                # print("Moving down")
                y -= 1
            else:
                # print("End found")
                for rowIdx, row in enumerate(reversed(rock)):
                    if (y+rowIdx) < len(tower):
                        for idx in range(len(row)):
                            if row[idx] == '#':
                                tower[y+rowIdx][idx + x] = '#'
                    else:
                        tmp = ['.' for i in range(x)]
                        tmp.extend(row)
                        tmp.extend(['.' for i in range(towerWidth - len(row) - x)])
                        tower.append(tmp)
                break

        # print(f"After rock {rockNum} fell, tower looks like:")
        # for line in reversed(tower):
        #     print(line)

        # if rockNum > 2:
        #     break

    print(f"Height of fallen rocks: {len(tower) - 1}")
    return len(tower) - 1, tower




# part 1
# simulateRocks(2022)

# part 2
numToSimulate = 1_000_000_000_000
simulateRocks(numToSimulate)

# numInitialRocks, numRepeatingRocks = simulateRocks(numToSimulate, True)
# print(f"numInitialRocks: {numInitialRocks}")
# print(f"numRepeatingRocks: {numRepeatingRocks}")

# initialRocksHeight, initialTower = simulateRocks(numInitialRocks)
# repeatingRocksHeight, repeatingRocksTower = simulateRocks(numRepeatingRocks, False, copy.deepcopy(initialTower))
# repeatingRocksHeight = repeatingRocksHeight - initialRocksHeight

# remainder = (numToSimulate-numInitialRocks) % numRepeatingRocks
# remainderRocksHeight, _ = simulateRocks(remainder, False, copy.deepcopy(repeatingRocksTower))
# remainderRocksHeight = remainderRocksHeight - repeatingRocksHeight
# print(f"remainder: {remainder}")
# print(f"initialRocksHeight: {initialRocksHeight}")
# print(f"repeatingRocksHeight: {repeatingRocksHeight}")
# print(f"remainderRocksHeight: {remainderRocksHeight}")
# print(f"Part 2 answer: {initialRocksHeight + remainderRocksHeight + repeatingRocksHeight*int((numToSimulate-numInitialRocks) / numRepeatingRocks)}")
