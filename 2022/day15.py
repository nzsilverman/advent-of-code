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

print(f"maxX: {maxX}, maxY: {maxY}")

# matrix = [['.' for x in range(maxX + 10)] for x in range(maxY + 10)]

# for sensor in sensors:
#     x, y = sensor
#     matrix[y][x] = 'S'

# for beacon in beacons:
#     x, y = beacon
#     matrix[y][x] = 'B'

# def printMatrix():
#     for line in matrix:
#         print(line)

def manhattanDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# def addInvalidLocations(sensor, beacon):
#     global matrix
#     sx, sy = sensor
#     bx, by = beacon
#     dist = manhattanDistance(sx, sy, bx, by)
#     print(f"distance: {dist}")

#     for rowIdx, row in enumerate(matrix):
#         for colIdx, val in enumerate(row):
#             if manhattanDistance(colIdx, rowIdx, sx, sy) <= dist:
#                 if matrix[rowIdx][colIdx] == '.':
#                     matrix[rowIdx][colIdx] = "#"

invalidLocations = set()

# def addInvalidLocations(sensor, beacon):
#     sx, sy = sensor
#     bx, by = beacon
#     dist = manhattanDistance(sx, sy, bx, by)
#     for a in range(dist + 1):
#         b = abs(dist - a) + 1
#         for i in range(b):
#             x1 = sx + a
#             y1 = sy + b
#             x2 = sx - a
#             y2 = sy - b
#             invalidLocations.add((x1, y1))
#             invalidLocations.add((x2, y2))


# for sensor, beacon in zip(sensors, beacons):
#     print(f"sensor: {sensor}, beacon: {beacon}")
#     addInvalidLocations(sensor, beacon)

# invalidLocations = set()

# for i in range(minX-100000, maxX+100000):
#     x, y = i, row
#     for sensor, beacon in zip(sensors, beacons):
#         sx, sy = sensor
#         bx, by = beacon
#         dist = manhattanDistance(sx, sy, bx, by)
#         if manhattanDistance(sx, sy, x, y) <= dist:
#             if (x,y) not in beacons and (x,y) not in sensors:
#                 invalidLocations.add((x, y))

for x in range(minX, maxX + 1):
    for sensor, beacon in zip(sensors, beacons):
        print(f"sensor: {sensor}, beacon: {beacon}")
        sx, sy = sensor
        bx, by = beacon
        dist = manhattanDistance(sx, sy, bx, by)
        pointToSensor = manhattanDistance(x, row, sx, sy)
        if pointToSensor <= dist and (x, row) not in beacons and (x, row) not in sensors:
            invalidLocations.add((x, row))



count = 0
for item in invalidLocations:
    x,y = item
    if y == row:
        print(item)
        count += 1

print(f"Count: {count}")

