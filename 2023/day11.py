import argparse
import itertools
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


def ArrContainsGalaxies(arr):
  if len(set(arr)) == 1 and arr[0] == '.':
    return False
  else:
    return True


def ExpandUniverse(matrix):
  expanded_rows = []
  for row in matrix:
    if not ArrContainsGalaxies(row):
      # Expand
      expanded_rows.append(row)
    expanded_rows.append(row)

  # Each row is actually a column
  expanded_cols = []
  for col_idx in range(len(expanded_rows[0])):
    col = []
    for row_idx in range(len(expanded_rows)):
      col.append(expanded_rows[row_idx][col_idx])

    if not ArrContainsGalaxies(col):
      expanded_cols.append(col)

    expanded_cols.append(col)

  # Convert rows into columns
  new_matrix = [[] for x in range(len(expanded_cols[0]))]
  for row in expanded_cols:
    assert len(row) == len(new_matrix)
    for idx, char in enumerate(row):
      new_matrix[idx].append(char)

  # Number each galaxy
  idx = 1
  for row_idx, row in enumerate(new_matrix):
    for col_idx, char in enumerate(row):
      if char == '#':
        new_matrix[row_idx][col_idx] = idx
        idx += 1

  return new_matrix


# @attrs.define(frozen=True)
@attrs.define()
class Node():
  row: int
  col: int


def GetNodeCoordinates(matrix):
  node_to_coords = {}
  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      if char != '.':
        node_to_coords[char] = Node(row=row_idx, col=col_idx)
  return node_to_coords


def InBounds(row_idx, col_idx, row_len, col_len):
  if row_idx < 0 or row_idx >= row_len:
    return False
  if col_idx < 0 or col_idx >= col_len:
    return False

  return True


def ShortestDistanceBetweenNodes(start_node, end_node, row_len, col_len):
  visited = set()

  queue = deque()
  queue.append((start_node, 0))

  while len(queue):
    s, dist = queue.popleft()

    if s == end_node:
      PrintDebug(f"Found end node!")
      return dist

    if (s.row, s.col) not in visited:
      visited.add((s.row, s.col))

    for permutation in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      test_node = Node(s.row + permutation[0], s.col + permutation[1])
      if InBounds(test_node.row, test_node.col, row_len, col_len):
        if (test_node.row, test_node.col) not in visited:
          queue.append((test_node, dist + 1))

  return -1


def GetCombinationsToShortestDistances(combinations, node_to_coords, row_len,
                                       col_len):
  combination_to_shortest_distance = {}
  for combination in combinations:
    shortest_distance = ShortestDistanceBetweenNodes(
      node_to_coords[combination[0]], node_to_coords[combination[1]], row_len,
      col_len)
    combination_to_shortest_distance[combination] = shortest_distance

  return combination_to_shortest_distance


def Part1(combination_to_shortest_distance):
  sum_shortest_distances = 0
  for combination in combination_to_shortest_distance:
    sum_shortest_distances += combination_to_shortest_distance[combination]

  print(f"Part 1 Answer: {sum_shortest_distances}")


def main():
  global DEBUG
  parser = argparse.ArgumentParser()
  parser.add_argument("input")
  parser.add_argument("--debug", action="store_true", default=False)
  args = parser.parse_args()
  DEBUG = args.debug

  data = open(args.input).read().strip()
  matrix = [[char for char in line] for line in data.split('\n')]

  PrintDebug("Original Universe")
  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      PrintDebug(char, end="")
    PrintDebug("")

  matrix = ExpandUniverse(matrix)
  PrintDebug("\nExpanded Universe")
  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      PrintDebug(char, end="")
    PrintDebug("")

  node_to_coords = GetNodeCoordinates(matrix)
  for key in node_to_coords.keys():
    PrintDebug(f"Node {key}: {node_to_coords[key]}")

  combinations = list(itertools.combinations(node_to_coords, 2))
  PrintDebug(f"Found {len(combinations)} unique combinations")

  combination_to_shortest_distance = GetCombinationsToShortestDistances(
    combinations, node_to_coords, len(matrix), len(matrix[0]))
  for key in combination_to_shortest_distance.keys():
    PrintDebug(
      f"Shortest distance between {key} is {combination_to_shortest_distance[key]}"
    )

  Part1(combination_to_shortest_distance)


if __name__ == '__main__':
  main()
