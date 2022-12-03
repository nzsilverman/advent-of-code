import statistics
import math
import numpy as np
import copy

def read_input(filename):
    """ Return a numpy matrix. """
    outer = []
    with open(filename, "r") as f:
        for row in f:
            inner = []
            for char in row.strip():
                inner.append(int(char))
            outer.append(inner)

    return np.array(outer)

def calculate_risk(positions, input_matrix):
    """ positions: list of list of positions, input_matrix == matrix read in. """
    sum_risk = 0
    for position in positions:
        x, y = position
        risk = 1 + input_matrix[x][y]
        sum_risk += risk
    return sum_risk


def puzzle(filename):
    input_matrix = read_input(filename)
    score_matrix = np.zeros(np.shape(input_matrix))
    for row_idx, row in enumerate(input_matrix):
        for col_idx, entry in enumerate(row):
            less_than_square = 0
            if row_idx == 0 and col_idx == 0:
                # Upper left corner
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            elif row_idx == 0 and col_idx == len(row) - 1:
                # Upper right corner
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            elif row_idx == len(input_matrix) - 1 and col_idx == 0:
                # Lower left corner
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
            elif row_idx == len(input_matrix) - 1 and col_idx == len(row) - 1:
                # Lower right corner
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
            elif row_idx == 0:
                # Top edge
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            elif row_idx == len(input_matrix) - 1:
                # Bottom edge
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
            elif col_idx == 0:
                # Left Edge
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            elif col_idx == len(row) - 1:
                # Right edge
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            else:
                # Middle square
                if input_matrix[row_idx][col_idx - 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx][col_idx + 1] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx - 1][col_idx] <= entry:
                    less_than_square += 1
                if input_matrix[row_idx + 1][col_idx] <= entry:
                    less_than_square += 1
            
            score_matrix[row_idx][col_idx] = less_than_square
    print(score_matrix)
    where_is_zero = np.asarray(np.where(score_matrix == 0)).T.tolist()

    risk = calculate_risk(where_is_zero, input_matrix)
    print("risk: {}".format(risk))

    
def get_adjacent_indices(i, j, m, n):
    """ matrix is size m x n (row x col) and index is <i, j> """
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def find_basin_size(basin_matrix, row_idx, col_idx):
    if row_idx >= len(basin_matrix) or row_idx < 0:
        return 0
    if col_idx >= len(basin_matrix[0]) or col_idx < 0:
        return 0
    if basin_matrix[row_idx][col_idx] == 0:
        return 0

    sum_adjacent = 0
    basin_matrix[row_idx][col_idx] = 0
    sum_adjacent += find_basin_size(basin_matrix, row_idx + 1, col_idx)
    sum_adjacent += find_basin_size(basin_matrix, row_idx - 1, col_idx)
    sum_adjacent += find_basin_size(basin_matrix, row_idx, col_idx + 1)
    sum_adjacent += find_basin_size(basin_matrix, row_idx, col_idx - 1)
    return 1 + sum_adjacent

def calculate_basins(filename):
    input_matrix = read_input(filename)
    where_is_nine = np.asarray(np.where(input_matrix == 9)).T.tolist()
    # 1 everywhere except where 9 is (those are zero)
    basin_matrix = np.ones(np.shape(input_matrix))
    for point in where_is_nine:
        x, y = point
        basin_matrix[x][y] = 0
    basin_sizes = []
    current_basin_size = 0
    for row_idx, row in enumerate(basin_matrix):
        for col_idx, entry in enumerate(row):
            basin_size = find_basin_size(basin_matrix, row_idx, col_idx)
            basin_sizes.append(basin_size)

    sorted_basin_sizes = sorted(basin_sizes, reverse=True)
    print("Top 3 multiplied: {}".format(sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2]))


def part2(filename):
    input_list = read_input(filename)

def test_calculate_basins():
    basin_test = np.array([[1,1,0], [1,0,1], [0, 1, 1]])
    print(basin_test)
    basin_size = find_basin_size(basin_test, 0, 0)
    print(basin_size)
    basin_size = find_basin_size(basin_test, 1, 0)
    print(basin_size)
    basin_size = find_basin_size(basin_test, 1, 2)
    print(basin_size)
    basin_size = find_basin_size(basin_test, 2, 1)
    print(basin_size)

def main():
    filename = 'input.txt'
    # filename = 'example.txt'

    # print("**********************************")
    # print("Part 1, input: {}".format(filename))
    # puzzle(filename)
    # print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    print("**********************************")
    calculate_basins(filename) 

    # test_calculate_basins()

if __name__ == "__main__":
    main()
