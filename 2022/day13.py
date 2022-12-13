from collections import deque
import ast
from itertools import islice

def readInput(filename):
    with open(filename, 'r') as f:
        pairs = []
        while True:
            next_3_lines = list(islice(f, 3))
            if not next_3_lines:
                break
            pair = []
            for line in next_3_lines[:2]:
                line = line.strip()
                parsed = ast.literal_eval(line)
                pair.append(parsed)
            pairs.append(pair)

def part1(pairs):
    for idx, pair in enumerate(pairs):
        left, right = pair

def main():
    lines = readInput('example.txt')
    # lines = readInput('input.txt')
    print("Part 1")
    print("Part 2")


if __name__ == '__main__':
    main()
