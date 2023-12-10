import sys
from collections import deque
import math

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


@attrs.define
class Mapping():
  left: str
  right: str


def Part1(instructions, graph):
  node = 'AAA'

  steps = 0
  while node != 'ZZZ':
    instruction = instructions[steps % len(instructions)]
    if instruction == 'L':
      node = graph[node].left
    else:
      node = graph[node].right

    steps += 1

  print(f"Part 1: Number of steps to find ZZZ: {steps}")


def Part2(instructions, graph):
  node = 'AAA'

  starting_nodes = []
  for node in graph.keys():
    if node.endswith("A"):
      starting_nodes.append(node)

  PrintDebug(f"Starting nodes: {starting_nodes}")

  node_to_steps = {}
  for node in starting_nodes:
    tmp_node = node
    steps = 0
    while not tmp_node.endswith('Z'):
      instruction = instructions[steps % len(instructions)]
      if instruction == 'L':
        tmp_node = graph[tmp_node].left
      else:
        tmp_node = graph[tmp_node].right

      steps += 1

    node_to_steps[node] = steps

  divisors = []
  for node in node_to_steps:
    PrintDebug(
      f"Starting node {node} took {node_to_steps[node]} steps to end in Z")
    divisors.append(node_to_steps[node])

  print(
    f"Part 2: Number of steps to end only on nodes that end in Z: {math.lcm(*divisors)}"
  )


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  instructions = [x for x in lines[0]]
  PrintDebug(f"Instructions: {instructions}")
  graph = {}
  for line in lines[2:]:
    node, left_right = [x.strip() for x in line.split(' = ')]
    left_right = left_right.replace("(", "")
    left_right = left_right.replace(")", "")
    left, right = [x.strip() for x in left_right.split(",")]
    graph[node] = Mapping(left=left, right=right)
    PrintDebug(line)

  for key in graph.keys():
    PrintDebug(f"Node: {key}, mapping: {graph[key]}")

  Part1(instructions, graph)
  Part2(instructions, graph)


if __name__ == '__main__':
  main()
