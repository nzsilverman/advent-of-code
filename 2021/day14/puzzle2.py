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

def grow_recursive(polymer, polymer_map, depth):
    if depth == 0:
        return polymer
    else:
        new_polymer = grow_polymer(polymer, polymer_map)
    return grow_recursive(new_polymer, polymer_map, depth-1)

def grow_pair_recursively(pair, polymer_map, depth, results_map):
    # print("pair: {} depth: {}".format(pair, depth))
    if depth == 0:
        return
    if pair not in polymer_map:
        return
    
    new_char = polymer_map[pair]
    if new_char not in results_map:
        results_map[new_char] = 1
    else:
        results_map[new_char] += 1

    pair1 = pair[0] + new_char
    pair2 = new_char + pair[1]

    if pair1 in polymer_map:
        grow_pair_recursively(pair1, polymer_map, depth-1, results_map)
    if pair2 in polymer_map:
        grow_pair_recursively(pair2, polymer_map, depth-1, results_map)
     
def generate_pairs_mapping(polymer_map):
    """ Map a pair to all of its contributions after 1 round.

    Example:
        NN -> NC + CN -> (B, C)
    """
    pairs_to_additions = {}
    for key in polymer_map:
        pair1 = key[:1] + polymer_map[key]
        pair2 = polymer_map[key] + key[1:]
        pair1_result = polymer_map[pair1] if pair1 in polymer_map else None
        pair2_result = polymer_map[pair2] if pair2 in polymer_map else None
        pairs_to_additions[key] = (pair1_result, pair2_result)

    return pairs_to_additions

def generate_pairs_to_pairs_mapping(polymer_map):
    """ Map a pair to the pairs it will generate with its contribution.

    Example:
        NN -> NC + CN 
    """
    pairs_to_pairs = {}
    for key in polymer_map:
        pair1 = key[:1] + polymer_map[key]
        pair2 = polymer_map[key] + key[1:]
        pairs_to_pairs[key] = (pair1, pair2)

    return pairs_to_pairs

def count_pairs_recursively(pair, pairs_to_pairs, depth, pairs_to_count):
    if depth == 0:
        return 
    if pair not in pairs_to_pairs:
        return

    if pair not in pairs_to_count:
        pairs_to_count[pair] = 1
    else:
        pairs_to_count[pair] += 1

    pair1, pair2 = pairs_to_pairs[pair]
    count_pairs_recursively(pair1, pairs_to_pairs, depth - 1, pairs_to_count)
    count_pairs_recursively(pair2, pairs_to_pairs, depth - 1, pairs_to_count)

def part2(filename):
    polymer_template, polymer_map = read_input(filename)

    results_map = {}
    for char in polymer_template:
        if char not in results_map:
            results_map[char] = 1
        else:
            results_map[char] += 1

    pairs_to_count = {}
    pairs_to_pairs = generate_pairs_to_pairs_mapping(polymer_map)
    for key in polymer_map:
        pairs_to_count[key] = 0

    for idx, char in enumerate(polymer_template[:-1]):
        pair = polymer_template[idx:idx+2]
        pairs_to_count[pair] += 1

    # iterations = 1
    # iterations = 10
    iterations = 40
    for i in range(iterations):
        print("i: {}".format(i))
        # pairs_to_increment = []
        pair_to_increment = {}
        for pair in pairs_to_count:
            if pairs_to_count[pair] > 0:
                num_of_pair = pairs_to_count[pair]
                pairs_to_count[pair] = 0
                if polymer_map[pair] in results_map:
                    results_map[polymer_map[pair]] += num_of_pair
                else:
                    results_map[polymer_map[pair]] = num_of_pair

                pair1, pair2 = pairs_to_pairs[pair] 

                if pair1 in pair_to_increment:
                    pair_to_increment[pair1] += num_of_pair
                else:
                    pair_to_increment[pair1] = num_of_pair

                if pair2 in pair_to_increment:
                    pair_to_increment[pair2] += num_of_pair
                else:
                    pair_to_increment[pair2] = num_of_pair

                # for i in range(num_of_pair):
                #     pairs_to_increment.extend((pair1, pair2))

        # for pair in pairs_to_increment:
        #     if pair in pairs_to_count:
        #         pairs_to_count[pair] += 1
        #     else:
        #         pairs_to_count[pair] = 1
        # print(pair_to_increment)
        for key in pair_to_increment:
            pairs_to_count[key] += pair_to_increment[key]

    print("Results map: ")
    print(results_map)

    scores = []
    for key in results_map:
        scores.append(results_map[key])

    scores = sorted(scores)
    print(scores)
    print("lowest: {} highest: {}".format(scores[0], scores[-1]))
    lowest = scores[0]
    highest = scores[-1]
    print("highest - lowest: {}".format(highest - lowest))


def part2_bad(filename):
    polymer_template, polymer_map = read_input(filename)

    # pairs_to_additions = generate_pairs_mapping(polymer_map)
    # print(pairs_to_additions)

    results_map = {}
    for char in polymer_template:
        if char not in results_map:
            results_map[char] = 1
        else:
            results_map[char] += 1

    # iterations = 10
    # iterations = 2
    iterations = 1
    # iterations = 40

    pairs_to_count = {}
    pairs_to_pairs = generate_pairs_to_pairs_mapping(polymer_map)
    
    for key in polymer_map:
        pairs_to_count[key] = 0

    for idx, char in enumerate(polymer_template[:-1]):
        pair = polymer_template[idx:idx+2]
        # grow_pair_recursively(pair, polymer_map, iterations, results_map)
        # count_pairs_recursively(pair, pairs_to_pairs, iterations, pairs_to_count)
        pairs_to_count[pair] += 1


    for i in range(iterations):
        print(pairs_to_count)
        pairs_to_increment = []
        for pair in pairs_to_count:
            if pairs_to_count[pair] != 0:
                print("using pair: {}".format(pair))
                pair1, pair2 =  pairs_to_pairs[pair]
                
                old_char = polymer_map[pair]
                if old_char not in results_map:
                    results_map[old_char] = 0
                else:
                    results_map[old_char] -= pairs_to_count[pair]

                new_char1 = polymer_map[pair1]
                new_char2 = polymer_map[pair2]

                if new_char1 not in results_map:
                    results_map[new_char1] = pairs_to_count[pair]
                else:
                    results_map[new_char1] += pairs_to_count[pair]

                if new_char2 not in results_map:
                    results_map[new_char2] = pairs_to_count[pair]
                else:
                    results_map[new_char2] += pairs_to_count[pair]

                for i in range(pairs_to_count[pair]):
                    pairs_to_increment.append(pair1)
                    pairs_to_increment.append(pair2)

                pairs_to_count[pair] = 0

        for pair in pairs_to_increment:
            pairs_to_count[pair] +=1

        print("pairs to count after: ")
        print(pairs_to_count)


    # results_map = {}
    # for pair in pairs_to_count:
    #     char = polymer_map[pair]
    #     if char not in results_map:
    #         results_map[char] = pairs_to_count[pair]
    #     else:
    #         results_map[char] += pairs_to_count[pair]
            
    print(results_map)

    scores = []
    for key in results_map:
        scores.append(results_map[key])

    scores = sorted(scores)
    print(scores)
    print("lowest: {} highest: {}".format(scores[0], scores[-1]))
    lowest = scores[0]
    highest = scores[-1]
    print("highest - lowest: {}".format(highest - lowest))

def main():
    filename = 'input.txt'
    # filename = 'example.txt'

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
