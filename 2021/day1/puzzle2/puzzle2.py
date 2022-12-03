""" Advent of Code 2021. Day 1. Puzzle 2. 
    
    Puzzle:
        Given a list of numbers, determine how many windows increased from the previous window.
        A window for this puzzle is a three measurement sliding window.
        The first window does not get a measurement because nothing is before it.

    Nathan Silverman <nzsilverman@gmail.com>
"""

def count_increases(lines):
    """ Count how many entries increased from the previous entry. 

        The first entry gets passed over since no entry was before it.
    """

    increasing = 0
    for idx, val in enumerate(lines):
        if idx == 0: # Ignore first line since not increasing or decreasing
            continue
        if lines[idx - 1] < val:
            increasing += 1

    return increasing

def generate_window(lines, num):
    """ Return a list that are the sum for the windows for the lines.
        
        Args:
            lines:  lines to group into windows
            num:    Number of items in a window
    """
    windows = []
    for idx, val in enumerate(lines):
        # Only create windows when a complete window can be generated
        if (idx + num) <= len(lines):
            window_sum = 0
            for i in range(num):
                window_sum += lines[idx + i]
            windows.append(window_sum)
        else:
            print(f"Skipping creating a window for:\n\tidx: {idx}, num: {num}, len(lines): {len(lines)}")
    return windows

def read_in_lines(filename):
    """ Read in and return lines as integers from a file. """

    with open(filename, 'r') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    return lines
    
def main():
    print("Advent of Code 2021, Day 1, Puzzle 2")
    lines = read_in_lines('puzzle2.in')
    windows = generate_window(lines, 3)
    increases = count_increases(windows)
    print("\nIncreases: {}".format(increases))

if __name__ == '__main__':
    main()
