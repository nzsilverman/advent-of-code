import numpy as np
import copy

class Point:
    """ A custom point class that is hashable. """
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def pretty_print(self):
        return f'<x: {self.x}, y: {self.y}>'
    def __repr__(self):
        return self.pretty_print()
    def __str__(self):
        return self.pretty_print()
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

def read_input(filename):
    """ Read input and return a list of lists where the inner list is a list of Points. """

    with open(filename, "r") as f:
        lines = [line.split('->') for line in f.readlines()]
        stripped_lines = []
        for line in lines:
            coords = [coord.strip() for coord in line]
            coords_as_points = []
            for point in coords:
                x, y = point.split(',')
                coords_as_points.append(Point(x, y))
            stripped_lines.append(coords_as_points)
            
    return stripped_lines

def enumerate_points_on_line_segment(p1, p2, skip_diagonals):
    """ Enumerate and return all points on the line segment that are integers.
        
        Args:
            p1           A Point for one end of the line segment
            p2           A Point for one end of the line segment

        Returns:
            A list of points that are on the line segment
    """
    if skip_diagonals:
        if (p2.y - p1.y) != 0 and (p2.x - p1.x) != 0:
            return []

    points_on_line = []
    next_point = copy.deepcopy(p1)
    while (next_point != p2):
        points_on_line.append(copy.deepcopy(next_point))
        next_point.x += np.sign(p2.x - p1.x)
        next_point.y += np.sign(p2.y - p1.y)
    points_on_line.append(copy.deepcopy(next_point))

    return points_on_line
        

def puzzle(skip_diagonals):
    """ Solve the puzzle, optionally skipping the diagonals. """

    line_segments = read_input('input.txt')
    # line_segments = read_input('example.txt')
    
    point_map = {}
    for line_segment in line_segments:
        p1, p2 = line_segment
        points_on_line = enumerate_points_on_line_segment(p1, p2, skip_diagonals)

        for point in points_on_line:
            if point in point_map:
                point_map[point] += 1
            else:
                point_map[point] = 1

    count = 0
    for key in point_map:
        if point_map[key] >= 2:
            count += 1

    print("Count: {}".format(count))
    
def main():
    print("Part 1")
    puzzle(True)
    print("Part 2")
    puzzle(False)

if __name__ == '__main__':
    main()
