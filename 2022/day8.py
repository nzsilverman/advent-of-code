import numpy as np

def readInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    matrix = []
    for line in lines:
        arr = []
        for char in line:
            arr.append(int(char))
        matrix.append(arr)

    return matrix

def printMatrix(matrix):
    print()
    for line in matrix:
        for char in line:
            print(round(char), end=" ")
        print()

    print()

def generateVisibleTable(matrix):
    width, height = len(matrix[0]), len(matrix)
    visibleTable = np.zeros((width, height))

    for row in range(width):
        for col in range(height):
            if row == 0 or row == height - 1: # Exterior Tree
                visibleTable[row][col] = 1
            elif col == 0 or col == width - 1: # Exterior Tree
                visibleTable[row][col] = 1
            else: # Interior Tree
                visibleLeft = True
                for i in range(row):
                    if matrix[i][col] >= matrix[row][col]:
                        visibleLeft = False

                visibleRight = True
                for i in range(row+1, width):
                    if matrix[i][col] >= matrix[row][col]:
                        visibleRight = False

                visibleTop = True
                for i in range(col):
                    if matrix[row][i] >= matrix[row][col]:
                        visibleTop = False

                visibleBottom = True
                for i in range(col+1, height):
                    if matrix[row][i] >= matrix[row][col]:
                        visibleBottom = False

                if visibleLeft or visibleRight or visibleTop or visibleBottom:
                    visibleTable[row][col] = 1




    return visibleTable

def generateScenicScores(matrix):
    width, height = len(matrix[0]), len(matrix)
    scenicTable = np.zeros((width, height))

    for row in range(width):
        for col in range(height):

            visibleLeft = 0
            for i in range(row-1, -1, -1):
                visibleLeft += 1
                if matrix[i][col] >= matrix[row][col]:
                    break

            visibleRight = 0
            for i in range(row+1, width):
                visibleRight += 1
                if matrix[i][col] >= matrix[row][col]:
                    break

            visibleTop = 0
            for i in range(col-1, -1, -1):
                visibleTop += 1
                if matrix[row][i] >= matrix[row][col]:
                    break

            visibleBottom = 0
            for i in range(col+1, height):
                visibleBottom += 1
                if matrix[row][i] >= matrix[row][col]:
                    break

            scenicScore = visibleLeft * visibleRight * visibleTop * visibleBottom
            scenicTable[row][col] = scenicScore




    return scenicTable


def main():
    matrix = readInput('example.txt')
    matrix = readInput('input.txt')
    printMatrix(matrix)
    visibleTable = generateVisibleTable(matrix)
    # printMatrix(visibleTable)
    print(f"Part 1: {visibleTable.sum()}")

    scenicTable = generateScenicScores(matrix)
    printMatrix(scenicTable)
    print(f"Part 2: {scenicTable.max()}")


if __name__ == '__main__':
    main()
