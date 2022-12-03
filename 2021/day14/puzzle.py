import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    with open(filename, "r") as f:
        polymer_map = {}
        polymer_template = ""
        read_in_rules = False
        for line in f:
            if line == '\n':
                read_in_rules = True
                continue

            if read_in_rules:
                pair, element = line.strip().split(' -> ')
                polymer_map[pair] = element
            else:
                polymer_template = line.strip()

    return polymer_template, polymer_map

            
def grow_polymer(polymer, polymer_map):
    new_polymer = ''
    for idx, char in enumerate(polymer[:-1]):
        new_polymer += char
        pair = polymer[idx:idx+2]
        if pair in polymer_map:
            new_polymer += polymer_map[pair]
    new_polymer += polymer[-1]

    return new_polymer

def part1(filename):
    polymer_template, polymer_map = read_input(filename)
    print(polymer_map)
    print(polymer_template)
    new_polymer = copy.deepcopy(polymer_template)
    for i in range(10):
        new_polymer = grow_polymer(new_polymer, polymer_map)
    
    element_map = {}
    for char in new_polymer:
        if char not in element_map:
            element_map[char] = 1
        else:
            element_map[char] += 1

    scores = []
    for key in element_map:
        scores.append(element_map[key])

    print(element_map['B'])
    scores = sorted(scores)
    print(scores)
    print("lowest: {} highest: {}".format(scores[0], scores[-1]))
    lowest = scores[0]
    highest = scores[-1]
    print("highest - lowest: {}".format(highest - lowest))
    
def part2(filename):
    polymer_template, polymer_map = read_input(filename)
    print(polymer_map)
    print(polymer_template)
    new_polymer = copy.deepcopy(polymer_template)
    for i in range(40):
        print("i: {}".format(i))
        new_polymer = grow_polymer(new_polymer, polymer_map)
    
    element_map = {}
    for char in new_polymer:
        if char not in element_map:
            element_map[char] = 1
        else:
            element_map[char] += 1

    scores = []
    for key in element_map:
        scores.append(element_map[key])

    print(element_map['B'])
    scores = sorted(scores)
    print(scores)
    print("lowest: {} highest: {}".format(scores[0], scores[-1]))
    lowest = scores[0]
    highest = scores[-1]
    print("highest - lowest: {}".format(highest - lowest))

def main():
    filename = 'input.txt'
    # filename = 'example.txt'

    print("**********************************")
    print("Part 1, input: {}".format(filename))
    part1(filename)
    print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
