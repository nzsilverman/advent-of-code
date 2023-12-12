import argparse
import math
import sys

from collections import defaultdict
from collections import deque

import attrs


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


def RowColToNodeNumber(row_idx, col_idx, length_row):
  """ Return a unique node number for every row/col idx pair in the graph. """
  return (col_idx + 1) + row_idx * length_row


def InBounds(row_idx, col_idx, matrix):
  if row_idx < 0 or row_idx >= len(matrix):
    return False
  if col_idx < 0 or col_idx >= len(matrix[0]):
    return False

  return True


def GetVisitedNodesInCycleRecursive(node, parent, adjacency_list, visited):
  visited.add(node)

  # TODO this wont work because of the neighbors finding the start node again
  # because its undirected ish?
  for neighbor in adjacency_list[node]:
    if neighbor == parent:
      continue

    if neighbor in visited:
      return (True, visited)
    else:
      if GetVisitedNodesInCycle(neighbor, node, adjacency_list, visited)[0]:
        return (True, visited)

  return (False, visited)


def GetVisitedNodesInCycle(start_node, adjacency_list):
  visited = set()
  PrintDebug(f"Start Node: {start_node}")

  stack = deque()
  stack.append(start_node)

  while len(stack):
    s = stack.pop()
    PrintDebug(f"s: {s}")

    if s not in visited:
      visited.add(s)

    for node in adjacency_list[s]:
      if node not in visited and node != s:
        PrintDebug(f"Adding node {node} to stack")
        stack.append(node)
      else:
        PrintYellow(f"Node ({node}) == s ({s})")

  return visited


def Part1(adjacency_list, start_node, matrix):
  visited = GetVisitedNodesInCycle(start_node, adjacency_list)

  furthest_length = math.ceil(len(visited) / 2)
  print(f"Part 1: Steps to get to farthest location: {furthest_length}")


def Part2(adjacency_list, start_node, matrix):
  visited = GetVisitedNodesInCycle(start_node, adjacency_list)
  PrintDebug(f"Visited: {visited}")

  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      node_number = RowColToNodeNumber(row_idx, col_idx, len(row))
      if node_number in visited:
        PrintYellow(char, end="")
      elif char == '.':
        PrintLightPurple(char, end="")
      else:
        PrintDebug(char, end="")
    PrintDebug("")


def main():
  global DEBUG
  parser = argparse.ArgumentParser()
  parser.add_argument("input")
  parser.add_argument("--debug", action="store_true", default=False)
  args = parser.parse_args()
  DEBUG = args.debug

  data = open(args.input).read().strip()
  matrix = [[char for char in line] for line in data.split('\n')]

  for line in matrix:
    for char in line:
      PrintDebug(char, end="")
    PrintDebug("")

  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      node_number = RowColToNodeNumber(row_idx, col_idx, len(row))
      PrintDebug(node_number, end="\t")
    PrintDebug("")

  start_node = None
  adjacency_list = defaultdict(set)

  for row_idx, row in enumerate(matrix):
    for col_idx, char in enumerate(row):
      node_number = RowColToNodeNumber(row_idx, col_idx, len(row))
      connected = deque()
      if char == '|':
        connected.append((row_idx - 1, col_idx))
        connected.append((row_idx + 1, col_idx))
      elif char == '-':
        connected.append((row_idx, col_idx - 1))
        connected.append((row_idx, col_idx + 1))
      elif char == 'L':
        connected.append((row_idx - 1, col_idx))
        connected.append((row_idx, col_idx + 1))
      elif char == 'J':
        connected.append((row_idx - 1, col_idx))
        connected.append((row_idx, col_idx - 1))
      elif char == '7':
        connected.append((row_idx + 1, col_idx))
        connected.append((row_idx, col_idx - 1))
      elif char == 'F':
        connected.append((row_idx + 1, col_idx))
        connected.append((row_idx, col_idx + 1))
      elif char == 'S':
        assert start_node is None
        start_node = node_number

      items_to_remove = []
      for item in connected:
        if not InBounds(item[0], item[1], matrix):
          items_to_remove.append(item)
      for item in items_to_remove:
        connected.remove(item)

      for item in connected:
        adjacency_list[node_number].add(
          RowColToNodeNumber(item[0], item[1], len(row)))

  start_node_connections = []
  for node_number in adjacency_list:
    if start_node in adjacency_list[node_number]:
      start_node_connections.append(node_number)
  assert len(start_node_connections) == 2
  adjacency_list[start_node].update(start_node_connections)

  PrintDebug("Adjacency List")
  for node_number in adjacency_list:
    PrintDebug(
      f"Node Number: {node_number}, set: {adjacency_list[node_number]}")

  # Part1(adjacency_list, start_node, matrix)
  Part2(adjacency_list, start_node, matrix)


if __name__ == '__main__':
  main()
