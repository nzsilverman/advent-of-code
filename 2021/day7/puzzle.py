import statistics
import math
import numpy as np

def read_input(filename):
    crab_list = []
    with open(filename, "r") as f:
        for line in f:
            crab_list.extend([int(entry) for entry in line.strip().split(',')])
    return crab_list

def puzzle():
    # crab_list = read_input('example.txt')
    crab_list = read_input('input.txt')
    print("average: {}".format(sum(crab_list) / len(crab_list)))
    print("mode: {}".format(statistics.mode(crab_list)))
    pos_to_align_to = statistics.mode(crab_list)
    fuel_spent = 0
    for crab in crab_list:
        fuel_spent += abs(pos_to_align_to - crab)

    print("fuel spent: {}".format(fuel_spent))
    
def brute():
    """ A bad brute force solution to part 1. """
    crab_list = read_input('example.txt')
    # crab_list = read_input('input.txt')
    lowest_fuel_spent = sum(crab_list) # higher than possible?

    for crab in crab_list:
        fuel_spent = 0
        for inner_crab in crab_list:
            fuel_spent += abs(crab - inner_crab)
        if fuel_spent < lowest_fuel_spent:
            lowest_fuel_spent = fuel_spent

    print("lowest: {}".format(lowest_fuel_spent))

def brute2():
    """ A bad brute force solution to part 2. """
    # crab_list = read_input('example.txt')
    crab_list = read_input('input.txt')

    index_to_change = {}
    for crab in crab_list:
        for idx in range(len(crab_list)):
            fuel_spent = 0
            horizontal_change = abs(crab - idx)
            horizontal_change = sum([i for i in range(horizontal_change + 1)])
            print("horizontal change for crab {} to {} is {}".format(crab, idx, horizontal_change))
            fuel_spent += horizontal_change
            if idx in index_to_change:
                index_to_change[idx] += fuel_spent
            else:
                index_to_change[idx] = fuel_spent

    lowest = None
    for index in index_to_change:
        if lowest is not None:
            if index_to_change[index] < lowest:
                lowest = index_to_change[index]
        else:
            lowest = index_to_change[index]

    print("lowest: {}".format(lowest))

def part1():
    # crab_list = read_input('example.txt')
    crab_list = read_input('input.txt')

    median = np.median(crab_list)

    fuel = 0
    for crab in crab_list:
        fuel += abs(median - crab)

    print("fuel: {}".format(fuel))

def part2():
    # crab_list = read_input('example.txt')
    crab_list = read_input('input.txt')

    mean = (np.mean(crab_list))
    mean_floor = math.floor(mean)
    mean_ceil = math.ceil(mean)

    fuels = []
    for mean in [mean_floor, mean_ceil]:
        fuel = 0
        for crab in crab_list:
            fuel += sum([i for i in range(abs(crab-mean) + 1)])
        fuels.append(fuel)
    print("fuel: {}".format(min(fuels)))


def main():
    #  puzzle()
    # brute()
    # brute2()
    # part1()
    part2()

if __name__ == "__main__":
    main()
