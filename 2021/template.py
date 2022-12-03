import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    with open(filename, "r") as f:
        pass

def part1(filename):
    input_something = read_input(filename)
    
def part2(filename):
    input_something = read_input(filename)

def main(filename):
    print("**********************************")
    print("Part 1, input: {}".format(filename))
    part1(filename)
    print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <filename>")
        exit(-1)
    main(sys.argv[1])
