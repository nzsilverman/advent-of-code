import statistics
import math
import numpy as np
import copy

def read_input(filename):
    """ Return a numpy matrix. """
    input_list = []
    with open(filename, "r") as f:
        for line in f:
            input_list.append([int(x) for x in line.strip()])
    return np.array(input_list)

def increase_all_energy_level_by_one(input_matrix):
    for row_idx, row in enumerate(input_matrix):
        for col_idx, col in enumerate(row):
            input_matrix[row_idx][col_idx] += 1

def flash_octopuses(input_matrix):
    """ flash octopuses greater than 9. 

        When an octopus flashes, increase all the adjacent octopuses by 1 except ones that
        flashed. Detect if an octopus has already flashed by checking if the square is 0. 

        Returns number of octopuses flashed
    """
    where_is_greater_than_nine = np.asarray(np.where(input_matrix > 9)).T.tolist()
    flashed_count = 0
    for idx in where_is_greater_than_nine:
        row, col = idx
        input_matrix[row][col] = 0
        flashed_count += 1
        increase_adjacent(row, col, input_matrix)
    return flashed_count

def increase_adjacent(row, col, input_matrix):
    """ Increase the energy level of adjacent octopuses from the row, col where one flashed.

    Only increase the energy level if it is not set to zero.
    """
    row_plus_one = row + 1
    col_plus_one = col + 1
    row_minus_one = row - 1
    col_minus_one = col - 1
    combos = [(row_plus_one, col_plus_one), (row_plus_one, col_minus_one), (row_plus_one, col), (row, col_plus_one), (row, col_minus_one), (row_minus_one, col_minus_one), (row_minus_one, col_plus_one), (row_minus_one, col)]

    for combo in combos:
        try:
            x, y = combo
            if x < 0 or y < 0:
                raise Exception("Index less than 0")
            if input_matrix[x][y] != 0:
                input_matrix[x][y] += 1
        except Exception as e:
            print("Exception: {}".format(e))

def part1(filename):
    input_matrix = read_input(filename)
    flash_count = 0
    for i in range(100):
        increase_all_energy_level_by_one(input_matrix)
        while (True):
            new_flashes = flash_octopuses(input_matrix)
            flash_count += new_flashes
            if new_flashes == 0:
                break
        print("After step {}:".format(i))
        print(input_matrix)

    print("Flash count:")
    print(flash_count)
        
def part2(filename):
    input_matrix = read_input(filename)
    flash_count = 0
    i = 1
    while True:
        increase_all_energy_level_by_one(input_matrix)
        flashes_per_step = 0
        while (True):
            new_flashes = flash_octopuses(input_matrix)
            print(new_flashes)
            flash_count += new_flashes
            flashes_per_step += new_flashes
            if new_flashes == 0:
                break

        where_is_zero = np.asarray(np.where(input_matrix == 0)).T.tolist()
        if len(where_is_zero) == 100:
            print("100 flashed at cycle {}".format(i))
            print(input_matrix)
            return
        else:
            print("{} flashed at cycle {}".format(len(where_is_zero), i))
        i = i + 1

    print("Flash count:")
    print(flash_count)

def main():
    filename = 'input.txt'
    # filename = 'example.txt'
    # filename = 'one.txt'
    # filename = 'two.txt'

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
