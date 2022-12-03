import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    """ Return an undirected representation of adjacent edges in a dictionary. """
    edge_dict = {}
    with open(filename, "r") as f:
        for line in f:
            node1, node2 = line.strip().split('-') 
            # print(f"{node1},{node2}")
            if node1 not in edge_dict:
                edge_dict[node1] = []
            if node2 not in edge_dict:
                edge_dict[node2] = []

            edge_dict[node1].append(node2)
            edge_dict[node2].append(node1)

    return edge_dict


def find_all_paths_part1(current_node, current_path, complete_paths, edge_dict):
    current_path.append(current_node)

    if current_node == 'end':
        complete_paths.append(current_path)
        return

    for adjacent_node in edge_dict[current_node]:
        if (adjacent_node.islower() and adjacent_node in current_path):
            pass
        else:
            find_all_paths_part1(adjacent_node, copy.deepcopy(current_path), complete_paths, edge_dict)

def find_all_paths_part2(current_node, current_path, complete_paths, edge_dict, two_small_visited):
    current_path.append(current_node)

    if current_node == 'end':
        complete_paths.append(current_path)
        return

    for adjacent_node in edge_dict[current_node]:
        if (adjacent_node.islower() and adjacent_node in current_path):
            # pass
            if adjacent_node not in ['start', 'end']:
                if two_small_visited == False:
                    find_all_paths_part2(adjacent_node, copy.deepcopy(current_path), complete_paths, edge_dict, True)
        else:
            find_all_paths_part2(adjacent_node, copy.deepcopy(current_path), complete_paths, edge_dict, two_small_visited)


            
def part1(filename):
    edge_dict = read_input(filename)
    complete_paths = []
    find_all_paths_part1('start', [], complete_paths, edge_dict)
    print("complete paths: ")
    for path in complete_paths:
        print(path)
    print(len(complete_paths))

def part2(filename):
    edge_dict = read_input(filename)
    complete_paths = []
    path_set = set()
    find_all_paths_part2('start', [], complete_paths, edge_dict, False)
    print("complete paths: ")
    for path in complete_paths:
        print(path)
    print(len(complete_paths))

def main():
    filename = 'input.txt'
    # filename = '10.txt'
    # filename = '19.txt'

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
