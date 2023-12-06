import sys
import attrs
import math
import numpy
from collections import deque


def PrintRed(skk, end="\n"):
  PrintDebug("\033[91m{}\033[00m".format(skk), end=end)


def PrintGreen(skk, end="\n"):
  PrintDebug("\033[92m{}\033[00m".format(skk), end=end)


def PrintYellow(skk, end="\n"):
  PrintDebug("\033[93m{}\033[00m".format(skk), end=end)


def PrintLightPurple(skk, end="\n"):
  PrintDebug("\033[94m{}\033[00m".format(skk), end=end)


DEBUG = 0


def PrintDebug(skk, end="\n"):
  if DEBUG:
    print(skk, end=end)


@attrs.define
class Race():
  time: int
  record: int


def SolveQuadraticEquation(a, b, c):
  PrintDebug(f"a: {a}, b: {b}, c: {c}")
  sol1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
  sol2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
  return sol1, sol2


def FindNumWaysToWinRace(races):
  numWaysToWinRace = []
  for race in races:
    PrintDebug(race)
    sol1, sol2 = SolveQuadraticEquation(-1, race.time, -race.record)

    # If solutions are integers, the race is tied which doesn't count as a win
    if sol1.is_integer():
      sol1 += 1
    if sol2.is_integer():
      sol2 -= 1

    lowerBound = math.ceil(sol1)
    upperBound = math.floor(sol2)

    PrintDebug(f"Sol1: {sol1}, Sol2: {sol2}")
    PrintDebug(f"Lower Bound: {lowerBound}, Upper Bound: {upperBound}")
    numSolutions = upperBound - lowerBound + 1
    numWaysToWinRace.append(numSolutions)

  print(f"Num Ways to Win Race: {numpy.prod(numWaysToWinRace)}")


def Part1(lines):
  times = [int(x) for x in lines[0].split(':')[1].strip().split()]
  distances = [int(x) for x in lines[1].split(':')[1].strip().split()]

  races = []
  for time, record in zip(times, distances):
    races.append(Race(time=time, record=record))

  print("Part 1 answer")
  FindNumWaysToWinRace(races)


def Part2(lines):
  races = []
  times = [
    int(x) for x in lines[0].split(':')[1].strip().replace(" ", "").split()
  ]
  distances = [
    int(x) for x in lines[1].split(':')[1].strip().replace(" ", "").split()
  ]
  for time, record in zip(times, distances):
    races.append(Race(time=time, record=record))

  print("Part 2 answer")
  FindNumWaysToWinRace(races)


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
