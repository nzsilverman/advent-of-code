from collections import deque
import sys

def readInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    matrix = []
    start = None
    end = None
    for row, line in enumerate(lines):
        vals = []
        for col, char in enumerate(line):
            if char == 'S':
                char = 'a'
                start = (row, col)
            elif char == 'E':
                char = 'z'
                end = (row, col)

            vals.append(ord(char) - 96)

        matrix.append(vals)

    return matrix, start, end

def readInputPt2(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]

    matrix = []
    start = []
    end = None
    for row, line in enumerate(lines):
        vals = []
        for col, char in enumerate(line):
            if char == 'S':
                char = 'a'
            elif char == 'E':
                char = 'z'
                end = (row, col)

            if char == 'a':
                start.append((row, col))

            vals.append(ord(char) - 96)

        matrix.append(vals)

    return matrix, start, end

# def bfs(matrix, loc, end, visited):
#     if loc == end:
#         return 1

#     row, col = loc
#     visited.add((row, col))

#     count = 0
#     for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         a = row + x
#         b = col + y
#         if a < 0 or a >= len(matrix):
#             continue
#         elif b < 0 or b >= len(matrix[0]):
#             continue
#         elif (a,b) in visited:
#             continue

#         if matrix[a][b] <= matrix[row][col] or (matrix[a][b] == (matrix[row][col] + 1)):
#             print(a,b)
#             return 1 + bfs(matrix, (a, b), end, visited)

def bfs(matrix, start, end):
    visited = set()
    visited.add(start)

    queue = deque()
    queue.append(start)

    prev = {}

    while queue:
        row, col = queue.popleft()

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            a = row + x
            b = col + y
            if a < 0 or a >= len(matrix):
                continue
            elif b < 0 or b >= len(matrix[0]):
                continue
            elif (a,b) in visited:
                continue

            if matrix[a][b] <= matrix[row][col] or (matrix[a][b] == (matrix[row][col] + 1)):
                queue.append((a, b))
                visited.add((a,b))
                prev[(a,b)] = (row, col)

    if end not in visited:
        return sys.maxsize

    location = end
    path = []
    while True:
        if location == start:
            break
        path.append(location)
        location = prev[location]

    path.reverse()

    return len(path)

def part2():
    # matrix, startList, end = readInputPt2('example.txt')
    matrix, startList, end = readInputPt2('input.txt')
    shortest = sys.maxsize
    for start in startList:
        print(f"finding path from {start} to {end}")
        shortest = min(bfs(matrix, start, end), shortest)

    print(f"shortest: {shortest}")


def main():
    # matrix, start, end = readInput('example.txt')
    matrix, start, end = readInput('input.txt')
    print(f"start: {start}, end: {end}")
    count = bfs(matrix, start, end)
    print("Part 1")
    print(f"count: {count}")

    print("Part 2")
    part2()


if __name__ == '__main__':
    main()
