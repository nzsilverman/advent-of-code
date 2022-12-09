def readInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    return lines

def main():
    lines = readInput('example.txt')
    # lines = readInput('input.txt')
    print("Part 1")
    print("Part 2")


if __name__ == '__main__':
    main()
