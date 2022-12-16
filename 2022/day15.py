import sys
from collections import deque
# from matplotlib.patches import Polygon
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import shapely.geometry as sg
from shapely.plotting import plot_polygon


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

def part2():
    if infile == 'input.txt':
        xMin, xMax = 0, 4000000
        yMin, yMax = 0, 4000000
    else:
        xMin, xMax = 0, 20
        yMin, yMax = 0, 20

    polygons = []
    backgroundRect = sg.Polygon([[xMin, yMin], [xMin, yMax], [xMax, yMax], [xMax, yMin]])

    fig, ax = plt.subplots()
    for sensor, beacon in zip(sensors, beacons):
        sx, sy = sensor
        bx, by = beacon
        dist = manhattanDistance(sx, sy, bx, by)
        print(f"drawing sensor centered at ({sx}, {sy}) and with distance: {dist}")
        points = np.array([(sx + dist,sy),(sx,sy+dist),(sx - dist,sy),(sx,sy-dist)])
        p = mpl.patches.Polygon(points, fc="white", ec="black")
        polygons.append(sg.Polygon(points))
        ax.add_patch(p)

    mergedPolygon = sg.Polygon()
    for polygon in polygons:
        mergedPolygon = mergedPolygon.union(polygon)

    differenceRect = backgroundRect - mergedPolygon
    differentPoint = differenceRect.centroid
    tuningFrequency = differentPoint.x * 4000000 + differentPoint.y
    print(f"tuningFrequency: {tuningFrequency}")

    plot_polygon(differenceRect, ax=ax)

    ax.set_xlim([xMin,xMax])
    ax.set_ylim([yMin,yMax])
    plt.show()


part1()
part2()
