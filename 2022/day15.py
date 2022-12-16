import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
row = int(sys.argv[2]) if len(sys.argv)>2 else 2000000
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]

sensors = []
beacons = []
maxX, maxY = 0, 0
minX, minY = sys.maxsize, sys.maxsize

for line in lines:
    s, b = line.split(': ')
    s = s.split(', ')
    sx = s[0].split('=')[1]
    sy = s[1].split('=')[1]
    b = b.split(', ')
    bx = b[0].split('=')[1]
    by = b[1].split('=')[1]
    sensors.append((int(sx), int(sy)))
    beacons.append((int(bx), int(by)))
    maxX = max(max(int(sx), maxX), int(bx))
    maxY = max(max(int(sy), maxY), int(by))
    minX = min(min(int(sx), minX), int(bx))
    minY = min(min(int(sy), minY), int(by))

def manhattanDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def part1():
    invalidLocations = set()
    for sensor, beacon in zip(sensors, beacons):
        print(f"sensor: {sensor}, beacon: {beacon}")
        sx, sy = sensor
        bx, by = beacon
        dist = manhattanDistance(sx, sy, bx, by)
        offset = 1_000_000
        for x in range(minX-offset, maxX + offset):
            pointToSensor = manhattanDistance(x, row, sx, sy)
            if pointToSensor <= dist and (x, row) not in beacons and (x, row) not in sensors:
                invalidLocations.add((x, row))

    print(f"Invalid locations in row {row}: {len(invalidLocations)}")

# part1()

# Works on example but is not optimized enough
# def part2():
#     if infile == 'input.txt':
#         xMin, xMax = 0, 4000000
#         yMin, yMax = 0, 4000000
#     else:
#         xMin, xMax = 0, 20
#         yMin, yMax = 0, 20

#     invalidLocations = set()
#     for x in range(xMin, xMax + 1):
#         for y in range(yMin, yMax + 1):
#             print(f"Investigating (x,y): ({x},{y})")
#             for sensor, beacon in zip(sensors, beacons):
#                 # print(f"sensor: {sensor}, beacon: {beacon}")
#                 sx, sy = sensor
#                 bx, by = beacon
#                 dist = manhattanDistance(sx, sy, bx, by)
#                 pointToSensor = manhattanDistance(x, y, sx, sy)
#                 if pointToSensor <= dist and (x, y) not in beacons and (x, y) not in sensors:
#                     invalidLocations.add((x, y))

#     for x in range(xMin, xMax + 1):
#         for y in range(yMin, yMax + 1):
#             if (x,y) not in invalidLocations and (x,y) not in beacons and (x,y) not in sensors:
#                 print(f"({x}, {y}) not in invalid locations set. Tuning frequency: {x*4000000 + y}")

def part2():
    if infile == 'input.txt':
        xMin, xMax = 0, 4000000
        yMin, yMax = 0, 4000000
    else:
        xMin, xMax = 0, 20
        yMin, yMax = 0, 20

    for x in range(xMin, xMax + 1):
        for y in range(yMin, yMax + 1):
            continue

part2()
