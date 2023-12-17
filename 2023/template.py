import argparse
import math
import sys

from collections import defaultdict
from collections import deque

import attrs

DEBUG = 0


def PrintRed(skk, end="\n"):
  PrintDebug("\033[91m{}\033[00m".format(skk), end=end)


def PrintGreen(skk, end="\n"):
  PrintDebug("\033[92m{}\033[00m".format(skk), end=end)


def PrintYellow(skk, end="\n"):
  PrintDebug("\033[93m{}\033[00m".format(skk), end=end)


def PrintLightPurple(skk, end="\n"):
  PrintDebug("\033[94m{}\033[00m".format(skk), end=end)


def PrintDebug(skk, end="\n"):
  if DEBUG:
    print(skk, end=end)


def main():
  global DEBUG
  parser = argparse.ArgumentParser()
  parser.add_argument("input")
  parser.add_argument("--debug", action="store_true", default=False)
  args = parser.parse_args()
  DEBUG = args.debug

  data = open(args.input).read().strip()
  lines = [line for line in data.split('\n')]

  for line in lines:
    PrintDebug(line)


if __name__ == '__main__':
  main()
