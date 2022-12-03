import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    with open(filename, "r") as f:
        line = f.read().strip()
    line = line.split()
    print(line)
    x1, x2 = [int(x) for x in line[2][2:-1].split('..')]
    y1, y2 = [int(x) for x in line[3][2:].split('..')]
    return (x1, x2, y1, y2)


def part1(filename):
    x1, x2, y1, y2 = read_input(filename)
    start_x, start_y = (0, 0)

    max_y = 0
    reach_end_set = set()
    reach_end_list = []
    for x in range(-1000, 1000):
        for y in range(-1000, 1000):
            print(x, y)
            y_pos = start_y
            x_pos = start_x
            y_cur = y # Current y velocity
            x_cur = x # Current x velocity
            reached_target = False
            local_max = 0
            while y_pos >= y1:
            # for i in range(500):
                y_pos = y_pos + y_cur
                x_pos = x_pos + x_cur

                if x_cur < 0:
                    x_cur = x_cur + 1
                elif x_cur > 0:
                    x_cur = x_cur -1
                elif x_cur == 0:
                    x_cur = 0

                y_cur -= 1

                local_max = max(y_pos, local_max)

                if x1 <= x_pos <= x2:
                    if y1 <= y_pos <= y2:
                        # In target
                        print("reached target with x: {} y: {}. x_pos: {} y_pos: {}".format(x, y, x_pos, y_pos))
                        reach_end_set.add((x, y))
                        reach_end_list.append((x, y))
                        reached_target = True
                        break
            if reached_target:
                print("local max: {}, max_y: {}".format(local_max, max_y))
                max_y = max(max_y, local_max)

    print("max y: {}".format(max_y))
    print("length of set: {}".format(len(reach_end_set)))
    print("length of list: {}".format(len(reach_end_list)))
    return reach_end_set
            
def compare_p2(my_set):
    correct = set()
    with open('correct_p2.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for line in lines:
            pairs = line.split()
            for pair in pairs:
                x, y = pair.split(',')
                correct.add((int(x),int(y)))

    print("correct - my_set: {}".format(correct - my_set))
    print("my_set - correct: {}".format(my_set - correct))

    
def part2(filename):
    my_set = part1(filename)
    # compare_p2(my_set)

def main():
    filename = 'input.txt'
    # filename = 'example.txt'

    # print("**********************************")
    # print("Part 1, input: {}".format(filename))
    # part1(filename)
    # print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
