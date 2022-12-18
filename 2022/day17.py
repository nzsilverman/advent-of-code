import sys
from collections import deque

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

def part1():
    numRocksToFall = 2022
    towerWidth = 7
    tower = [['-' for x in range(towerWidth)]]
    jetIdx = 0

    for rockNum in range(numRocksToFall):
        rock = rocks[rockNum % len(rocks)]
        x = 2 # Where is left side of rock
        y = len(tower) + 3

        while True:
            jetDir = jetPattern[jetIdx % len(jetPattern)]
            jetIdx += 1
            # Shift left/ right
            if jetDir == '<' and not checkIfRockHitsAnything(tower, rock, x, y, "left"):
                print("Moving left")
                x -= 1
            elif jetDir == '<':
                print("Skipping moving left")
            elif jetDir == '>' and not checkIfRockHitsAnything(tower, rock, x, y, "right"):
                print("Moving right")
                x += 1
            else:
                print("Skipping moving right")

            # Move down if possible, else come to rest
            rockHitsSomething = checkIfRockHitsAnything(tower, rock, x, y, "down")

            if not rockHitsSomething:
                print("Moving down")
                y -= 1
            else:
                print("End found")
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




part1()
