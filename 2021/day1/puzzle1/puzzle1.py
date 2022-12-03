""" Advent of Code 2021. Day 1. Puzzle 1. 
    
    Puzzle:
        Given a list of numbers, determine how many numbers increased from the previous number.
        The first number does not get a measurement because nothing is before it.

    Nathan Silverman <nzsilverman@gmail.com>
"""
def main():
    with open('puzzle1.in', 'r') as f:
        lines = [int(line.strip()) for line in f.readlines()]

    increasing = 0
    for idx, val in enumerate(lines):
        if idx == 0: # Ignore first line since not increasing or decreasing
            continue
        if lines[idx - 1] < val:
            increasing += 1
    print(f"Increasing lines: {increasing}")

if __name__ == '__main__':
    main()
