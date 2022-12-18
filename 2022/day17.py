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

# Todo this is broken
def checkIfRockHitsAnything(tower, rock, x, y, direction):
    stopFound = False
    for colIdx in range(len(rock)):
        for rowIdx in range(len(rock[0])):
            print(f"colIdx: {colIdx}, rowIdx: {rowIdx}, y: {y}, x: {x}, len(tower): {len(tower)}")
            relativeY = y - (len(rock) - colIdx - 1)
            print(f"relativeY: {relativeY}")
            # if y <= len(tower):
            if direction == 'left':
                if rowIdx + x - 1 < 0:
                    stopFound = True
                    break

                if relativeY >= len(tower):
                    break
                # print(f"tower[y][rowIdx - x -1]: {tower[y][rowIdx - x - 1]}")
                # print(f"rock[colIdx][rowIdx]: {rock[colIdx][rowIdx]}")
                if tower[relativeY][rowIdx + x - 1] in ['-', '#'] and rock[colIdx][rowIdx] == '#':
                    stopFound = True
                    break
            elif direction == 'right':
                # if rowIdx + x + 1 < len(tower[0]) or y == len(tower):
                # print(f"colIdx: {colIdx}, rowIdx: {rowIdx}, y: {y}, x: {x}, len(tower[0]): {len(tower[0])}, len(rock[0]): {len(rock[0])}")
                if x + len(rock[0]) + 1 > len(tower[0]):
                    stopFound = True
                    break

                if relativeY >= len(tower):
                    break

                if tower[relativeY][rowIdx + x + 1] in ['-', '#'] and rock[colIdx][rowIdx] == '#':
                    stopFound = True
                    break
            elif direction == 'down':
                if relativeY > len(tower):
                    break

                if tower[relativeY-1][rowIdx + x] in ['-', '#'] and rock[colIdx][rowIdx] == '#':
                    print(f"tower line: ")
                    for line in tower[relativeY-1:relativeY]:
                        print(line)
                    print(f"rock[colIdx]")
                    print(rock[colIdx])
                    print(f"Downward stop found: tower[relativeY-1][rowIdx+x]: {tower[relativeY-1][rowIdx+x]}, rock[colIdx][rowIdx]: {rock[colIdx][rowIdx]}")

                    stopFound = True
                    break

        if stopFound:
            break

    return stopFound

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
            # stopFound = False
            # for colIdx in range(len(rock)):
            #     for rowIdx in range(len(rock[0])):
            #         print(f"colIdx: {colIdx}, rowIdx: {rowIdx}, y: {y}, x: {x}, len(tower): {len(tower)}")
            #         if y <= len(tower):
            #             if tower[y-1][rowIdx + x] in ['-', '#'] and rock[colIdx][rowIdx] == '#':
            #                 stopFound = True
            #                 break

            #     if stopFound:
            #         break
            stopFound = checkIfRockHitsAnything(tower, rock, x, y, "down")


            if not stopFound:
                print("Moving down")
                y -= 1
            else:
                print("End found")
                for row in reversed(rock):
                    tmp = ['.' for i in range(x)]
                    tmp.extend(row)
                    tmp.extend(['.' for i in range(towerWidth - len(row) - x)])
                    tower.append(tmp)
                break

        print(f"After rock {rockNum} fell, tower looks like:")
        for line in reversed(tower):
            print(line)

        if rockNum > 2:
            break

    print(f"Height of fallen rocks: {len(tower) - 1}")




part1()
