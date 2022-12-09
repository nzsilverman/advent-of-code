class Loc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def readInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def simulateStep(hLoc, tLoc, direction, moveHead=False):
    if moveHead:
        # Update hLoc
        if direction == 'U':
            hLoc.y += 1
        elif direction == 'D':
            hLoc.y -= 1
        elif direction == 'R':
            hLoc.x += 1
        elif direction == 'L':
            hLoc.x -= 1


    # Update tLoc
    if (hLoc.x != tLoc.x) and (hLoc.y != tLoc.y): # H moved diagonally
        signX = 1 if (hLoc.x > tLoc.x) else -1
        signY = 1 if (hLoc.y > tLoc.y) else -1
        distance = 1 if abs(hLoc.x - tLoc.x) >=2 or abs(hLoc.y - tLoc.y) >= 2 else 0
        tLoc.x += signX * distance
        tLoc.y += signY * distance
    else: # H moved within a row or column
        if (hLoc.x - tLoc.x) >= 2:
            tLoc.x += 1
        elif (tLoc.x - hLoc.x) >= 2:
            tLoc.x -= 1
        elif (hLoc.y - tLoc.y) >= 2:
            tLoc.y += 1
        elif (tLoc.y - hLoc.y) >= 2:
            tLoc.y -= 1



def part1(lines):
    hLoc = Loc(0,0)
    tLoc = Loc(0,0)
    tVisitedLocs = set()
    tVisitedLocs.add((tLoc.x, tLoc.y))

    for line in lines:
        direction, steps = line.split()
        for step in range(int(steps)):
            simulateStep(hLoc, tLoc, direction, moveHead=True)
            tVisitedLocs.add((tLoc.x, tLoc.y))

    print(f"Size of tVisitedLocs set: {len(tVisitedLocs)}")

def part2(lines):
    knotLocs = [Loc(0,0) for x in range(10)]
    tVisitedLocs = set()
    tVisitedLocs.add((knotLocs[9].x, knotLocs[9].y))

    for line in lines:
        direction, steps = line.split()
        for step in range(int(steps)):
            for i in range(1,len(knotLocs)):
                head = knotLocs[i-1]
                tail = knotLocs[i]
                simulateStep(head, tail, direction, i==1)
                if i == 9:
                    tVisitedLocs.add((tail.x, tail.y))
    print(f"Size of tVisitedLocs set: {len(tVisitedLocs)}")



def main():
    lines = readInput('input.txt')
    print("Part 1")
    part1(lines)
    print("Part 2")
    part2(lines)


if __name__ == '__main__':
    main()
