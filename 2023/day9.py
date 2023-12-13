import sys
from collections import deque


def PrintRed(skk, end="\n"):
  PrintDebug("\033[91m{}\033[00m".format(skk), end=end)


def PrintGreen(skk, end="\n"):
  PrintDebug("\033[92m{}\033[00m".format(skk), end=end)


def PrintYellow(skk, end="\n"):
  PrintDebug("\033[93m{}\033[00m".format(skk), end=end)


def PrintLightPurple(skk, end="\n"):
  PrintDebug("\033[94m{}\033[00m".format(skk), end=end)


DEBUG = 1


def PrintDebug(skk, end="\n"):
  if DEBUG:
    print(skk, end=end)


def CalculateHistoryPart1(report):

  history = [report]

  current = report
  while True:
    row = []
    for a, b in zip(current[1:], current[:-1]):
      row.append(a - b)
    history.append(row)
    current = row

    if sum(row) == 0:
      break

  PrintDebug(f"History:")
  for row in history:
    PrintDebug(row)

  next_value = 0
  for row in reversed(history):
    PrintDebug(f"Row: {row}")
    next_value += row[-1]

  return next_value


def Part1(lines):
  reports = []
  for line in lines:
    report = [int(x) for x in line.split()]
    reports.append(report)

  sum_history = 0
  for report in reports:
    sum_history += CalculateHistoryPart1(report)

  print(f"Part 1: {sum_history}")


def CalculateHistoryPart2(report):

  history = [report]

  current = report
  while True:
    row = []
    for a, b in zip(current[1:], current[:-1]):
      row.append(a - b)
    history.append(row)
    current = row

    if sum(row) == 0:
      break

  PrintDebug(f"History:")
  for row in history:
    PrintDebug(row)

  vals = [0]
  for idx, row in enumerate(reversed(history[:-1])):
    diff = row[0] - vals[-1]
    PrintDebug(f"Row: {row}, diff: {diff}")
    vals.append(diff)

  return vals[-1]


def Part2(lines):
  reports = []
  for line in lines:
    report = [int(x) for x in line.split()]
    reports.append(report)

  sum_history = 0
  for report in reports:
    sum_history += CalculateHistoryPart2(report)

  print(f"Part 2: {sum_history}")


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  # Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
