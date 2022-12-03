import statistics
import math
import numpy as np
import copy
import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import scipy
import heapq

def read_input(filename):
    outer_list = []
    with open(filename, "r") as f:
        for row in f:
            inner_list = []
            for char in row.strip():
                inner_list.append(int(char))
            outer_list.append(inner_list)
    
    return outer_list

def generate_directed_weighted_graph(input_list):
    num_rows = len(input_list)
    num_cols = len(input_list[0])
    graph = np.zeros((num_rows * num_cols, num_rows*num_cols))
    idx_to_vertice = np.zeros((num_rows, num_cols), dtype=int)
    
    nums = [x for x in range(num_rows*num_cols)]
    idx = 0
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            idx_to_vertice[row_idx][col_idx] = nums[idx]
            idx += 1

    for row_idx, row in enumerate(input_list):
        for col_idx, col in enumerate(row):
            current_vertice = idx_to_vertice[row_idx][col_idx]
            vertices_to_add = []
            if col_idx > 0:
                # left exists
                left_vertice = idx_to_vertice[row_idx][col_idx-1]
                vertices_to_add.append((left_vertice, input_list[row_idx][col_idx-1]))
            
            if col_idx < len(row)-1:
                # Right exists
                right_vertice = idx_to_vertice[row_idx][col_idx+1]
                vertices_to_add.append((right_vertice, input_list[row_idx][col_idx+1]))

            if row_idx > 0:
                # Top exists
                top_vertice = idx_to_vertice[row_idx-1][col_idx]
                vertices_to_add.append((top_vertice, input_list[row_idx-1][col_idx]))

            if row_idx < len(input_list)-1:
                # Bottom exists
                bottom_vertice = idx_to_vertice[row_idx+1][col_idx]
                vertices_to_add.append((bottom_vertice, input_list[row_idx+1][col_idx]))

            for vertice, weight in vertices_to_add:
                # print("Current vertice: {}\tVertice: {}\tWeight: {}".format(current_vertice, vertice, weight))
                graph[current_vertice][vertice] = weight


    # where_is_zero = np.asarray(np.where(graph == 0)).T.tolist()
    # for point in where_is_zero:
    #     x, y = point
    #     graph[x][y] = sys.maxsize

    return graph

def part1(filename):
    input_list = read_input(filename)
    # input_list = [[1,2,3],[4,5,6],[7,8,9]]
    graph = generate_directed_weighted_graph(input_list)
    print("Done generating directed graph")
    dist_matrix = shortest_path(graph, directed=True, indices=0)
    print(dist_matrix)
    num_rows, num_cols = np.shape(graph)
    print("Distance between node 0 and {}".format(num_cols-1))
    print(dist_matrix[num_cols-1])


def square_to_new_val(original, row_offset, col_offset):
    # Apply row offset
    val = (original + row_offset) % 9 
    val = 9 if val == 0 else val

    # Apply col offset
    val = (val + col_offset) % 9
    val = 9 if val == 0 else val

    return val

def generate_5x_list(input_list):
    new_array = np.zeros((5*len(input_list), 5*len(input_list[0])), dtype=int)
    for i in range(5):
        for j in range(5):
            for row_idx, row in enumerate(input_list):
                for col_idx, val in enumerate(row):
                    new_val = square_to_new_val(val, i, j)
                    new_row_idx = row_idx + i * len(input_list)
                    new_col_idx = col_idx + j * len(input_list[0])
                    new_array[new_row_idx][new_col_idx] = new_val
    return new_array

class Node:
    def __init__ (self, position=None, parent=None):
        self.position = position
        self.parent = parent

        self.g = sys.maxsize
        self.h = sys.maxsize
        self.f = sys.maxsize

    def __eq__(self, other):
        return self.position == other.position

def manhattan_distance(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)

def heuristic(position1, position2):
    """ Return the h value from position1 (x,y) to position2 (x,y).
        
        Args:
            position1   Tuple of x,y
            position2   Tuple of x,y
    """
    x1, y1 = position1
    x2, y2 = position2
    return manhattan_distance(x1, x2, y1, y2)

def a_star(nodes, graph, start, end):
    """ Perform A star algorithm. 
        
        Args:
            nodes   a list of Nodes to traverse
            graph   puzzle input list where each coordinate(x,y) has the weight to get there from its neighbors
            start   coordinate tuple (x,y) in graph of where to start
            end     coordinate tuple (x,y) in graph of where to end
    """

    open_list = nodes
    closed_list = []
    closed_set = set() # Set to check if a position is in the closed list

    # Initialize start node to have an f value of 0
    for idx, node in enumerate(open_list):
        if node == start:
            open_list[idx].h = 0
            open_list[idx].g = 0
            open_list[idx].f = 0

    while open_list:
        current = open_list[0]
        current_idx = 0
        for idx, val in enumerate(open_list):
            if val.f < current.f:
                current = val
                current_idx = idx
        open_list.pop(current_idx)
        closed_list.append(current)
        closed_set.add(current.position)

        if current == end:
            # End found
            return closed_list

        # A list of tuples of the neighbor position and the cost to move from the current to the neighbor
        neighbors = []
        # print("current.position")
        # print(current.position)
        cur_x, cur_y = current.position
        if cur_y > 0:
            # left exists
            left_vertice = (cur_x, cur_y-1)
            neighbors.append((left_vertice, graph[cur_x][cur_y-1]))
        
        if cur_y < len(graph[0])-1:
            # Right exists
            right_vertice = (cur_x, cur_y+1)
            neighbors.append((right_vertice, graph[cur_x][cur_y+1]))

        if cur_x > 0:
            # Top exists
            top_vertice = (cur_x-1, cur_y)
            neighbors.append((top_vertice, graph[cur_x-1][cur_y]))

        if cur_x < len(graph)-1:
            # Bottom exists
            bottom_vertice = (cur_x+1, cur_y)
            neighbors.append((bottom_vertice, graph[cur_x+1][cur_y]))

        for neighbor in neighbors:
            neighbor_pos, neighbor_cost = neighbor
            if neighbor_pos in closed_set:
                # Skip this neighbor
                continue
            
            for idx, open_val in enumerate(open_list):
                if open_val.position == neighbor_pos:
                    if (neighbor_cost + current.g) < open_val.g:
                        open_list[idx].parent = current.position
                        open_list[idx].g = neighbor_cost + current.g
                        open_list[idx].h = heuristic(open_val.position, end.position) + neighbor_cost
                        open_list[idx].f = open_list[idx].g + open_list[idx].h

    return closed_list

def generate_nodes_for_all_indices(graph):
    nodes = []
    for row_idx, row in enumerate(graph):
        for col_idx, val in enumerate(row):
            nodes.append(Node((row_idx, col_idx)))

    return nodes
    
def part2(filename):
    input_list = read_input(filename)
    input_list = generate_5x_list(input_list)
    print("len(input_list): {} len(input_list[0]): {}".format(len(input_list), len(input_list[0])))
    graph = generate_directed_weighted_graph(input_list)
    print("Done generating directed graph")
    print("Graph shape: {}".format(np.shape(graph)))
    # dist_matrix = shortest_path(graph, directed=True, indices=0)
    dist_matrix = scipy.sparse.csgraph.dijkstra(graph, directed=True, indices=0)
    num_rows, num_cols = np.shape(graph)
    print("Distance between node 0 and {}".format(num_cols-1))
    print(dist_matrix[num_cols-1])

def part2_a_star(filename):
    input_list = read_input(filename)
    input_list = generate_5x_list(input_list)
    nodes = generate_nodes_for_all_indices(input_list)
    end_idx_x = len(input_list) - 1
    end_idx_y = len(input_list[0]) - 1
    a_star_closed_list = a_star(nodes, input_list, Node((0,0)), Node((end_idx_x, end_idx_y)))
    print("A star cost: {}".format(a_star_closed_list[-1].g))

def part2_dijkstra(filename):
    input_list = read_input(filename)
    input_list = generate_5x_list(input_list)
    N = len(input_list) 
    M = len(input_list[0])

    visited = set()
    # Store elements in the priority queue as tuples of (cost to get here, row idx, col idx)
    # Initialize the pq to (0,0,0)
    pq = [(0,0,0)]
    heapq.heapify(pq)
    # Map of (row_idx, col_idx) -> shortest path to get there
    count = {}

    while len(pq) > 0:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if (cur_row, cur_col) in visited:
            # A shorter path to htis node has already been found
            continue

        # This is the shortest path to this node
        visited.add((cur_row, cur_col))
        count[(cur_row, cur_col)] = cur_cost

        if cur_row == N-1 and cur_col == M-1:
            break

        # Update the cost of neighbors
        for r, c in [[0,1], [0,-1], [1,0], [-1,0]]:
            row = cur_row + r
            col = cur_col + c

            if not (0 <= row < N and 0 <= col < M):
                # Out of bounds
                continue

            heapq.heappush(pq, (cur_cost + input_list[row][col], row, col))
        

    print("Dijsktra cost: {}".format(count[(N-1, M-1)]))

def part2_better_a_star(filename):
    input_list = read_input(filename)
    input_list = generate_5x_list(input_list)
    N = len(input_list) 
    M = len(input_list[0])

    visited = set()
    # Store elements in the priority queue as tuples of (f, g, h, row idx, col idx)
    # Initialize the pq to (0,0,0)
    pq = [(0,0,0,0,0)]
    heapq.heapify(pq)
    # Map of (row_idx, col_idx) -> shortest path to get there
    count = {}

    while len(pq) > 0:
        f, g, h, cur_row, cur_col = heapq.heappop(pq)
        if (cur_row, cur_col) in visited:
            # A shorter path to htis node has already been found
            continue

        # This is the shortest path to this node
        visited.add((cur_row, cur_col))
        count[(cur_row, cur_col)] = g

        if cur_row == N-1 and cur_col == M-1:
            break

        # Update the cost of neighbors
        for r, c in [[0,1], [0,-1], [1,0], [-1,0]]:
            row = cur_row + r
            col = cur_col + c

            if not (0 <= row < N and 0 <= col < M):
                # Out of bounds
                continue

            new_g = g + input_list[row][col]
            new_h = manhattan_distance(row, N-1, col, M-1)
            new_f = new_g + new_h
            heapq.heappush(pq, (new_f, new_g, new_h, row, col))
        

    print("A Star cost: {}".format(count[(N-1, M-1)]))

def main():
    filename = 'input.txt'
    # filename = 'example.txt'

    # print("**********************************")
    # print("Part 1, input: {}".format(filename))
    # part1(filename)
    # print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    # part2(filename)
    # part2_a_star(filename)
    # part2_dijkstra(filename)
    part2_better_a_star(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
