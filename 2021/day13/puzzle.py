import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    """ Return a tuple of the grid and the folds.

        The grid is a numpy array of a 1 where the `#` symbol is. Everything else is a 0 where the `.` is  
        
        The folds is a list of tuples containing an axis and a value
    """
        
    with open(filename, "r") as f:
        highest_x = 0
        highest_y = 0

        points = []
        folds = [] # Ordered list of folds as tuples of (<x or y>, value)
        read_in_folds = False
        for line in f:
            if line == '\n':
                read_in_folds = True
                continue

            if not read_in_folds:
                x, y = [int(val) for val in line.strip().split(',')]
                highest_x = max(x, highest_x)
                highest_y = max(y, highest_y)
                points.append((x,y))
            else:
                # Read in folds
                axis, val = line.strip().split()[2].split('=')
                folds.append((axis, int(val)))

        # x is the column and y is the rows in the problem... confusing, right?
        points_matrix = np.zeros((highest_y+1, highest_x+1))
        for point in points:
            x, y = point
            points_matrix[y][x] = 1

    return points_matrix, folds

def fold_up(matrix1, matrix2):
    """ Fold matrix2 up onto matrix1. """
    matrix2 = np.flip(matrix2, 0) # Flip the matrix up
    
    m1_rows, m1_cols = np.shape(matrix1)
    m2_rows, m2_cols = np.shape(matrix2)

    smaller_matrix = None
    larger_matrix = None
    offset = abs(m1_rows - m2_rows)
    if m1_rows < m2_rows:
        smaller_matrix = matrix1
        larger_matrix = matrix2
    else:
        smaller_matrix = matrix2
        larger_matrix = matrix1

    for row_idx, row in enumerate(larger_matrix):
        for col_idx, col in enumerate(row):
            if row_idx >= offset:
                if smaller_matrix[row_idx - offset][col_idx] == 1:
                    larger_matrix[row_idx][col_idx] = 1

    return copy.deepcopy(larger_matrix) # TODO do we need to copy this?

def fold_left(matrix1, matrix2):
    """ Fold matrix2 left onto matrix1. """
    matrix2 = np.flip(matrix2, 1) # Flip the matrix up
    
    m1_rows, m1_cols = np.shape(matrix1)
    m2_rows, m2_cols = np.shape(matrix2)

    smaller_matrix = None
    larger_matrix = None
    offset = abs(m1_cols - m2_cols)
    if m1_cols < m2_cols:
        smaller_matrix = matrix1
        larger_matrix = matrix2
    else:
        smaller_matrix = matrix2
        larger_matrix = matrix1

    for row_idx, row in enumerate(larger_matrix):
        for col_idx, col in enumerate(row):
            if col_idx >= offset:
                if smaller_matrix[row_idx][col_idx - offset] == 1:
                    larger_matrix[row_idx][col_idx] = 1

    return copy.deepcopy(larger_matrix) # TODO do we need to copy this?

def split_matrix(matrix, fold):
    """ Return a tuple of the two matrices found from splitting matrix by fold.
        fold is a tuple of (axis, val)
    """
    axis, val = fold

    # print("Attempting to use fold {} on matrix: ".format(fold))
    # print(matrix)
    
    if axis == 'x':
        m1 = matrix[:, :val]
        m2 = matrix[:, val+1:]
    else:
        m1 = matrix[:val, :]
        m2 = matrix[val+1:, :]

    return (m1, m2)
            
def part1(filename):
    points_matrix, folds = read_input(filename)

    working_matrix = copy.deepcopy(points_matrix)
    for fold in folds:
        m1, m2 = split_matrix(working_matrix, fold)
        axis, val = fold
        if axis == 'x':
            working_matrix = fold_left(m1, m2)
        else:
            working_matrix = fold_up(m1, m2)
        break # Only apply one fold for part 1

    print(working_matrix.sum())
    
def part2(filename):
    points_matrix, folds = read_input(filename)

    working_matrix = copy.deepcopy(points_matrix)
    for fold in folds:
        m1, m2 = split_matrix(working_matrix, fold)
        axis, val = fold
        if axis == 'x':
            working_matrix = fold_left(m1, m2)
        else:
            working_matrix = fold_up(m1, m2)

    for line in working_matrix:
        for char in line:
            # out = '#' if char else ' '
            out = '*' if char else ' '
            print(out, end="")
        print("")

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
