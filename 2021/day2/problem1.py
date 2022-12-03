def main():
    with open('input.txt', 'r') as f:
        lines = [a.strip() for a in f.readlines()]

    depth = 0
    horizontal = 0

    for line in lines:
        command, val = line.split()
        val = int(val)
        if command == 'forward':
            horizontal += val
        elif command == 'down':
            depth += val
        elif command == 'up':
            depth -= val

    print("final depth: {}".format(depth))
    print("final horizontal: {}".format(horizontal))
    print("multiplied: {}".format(depth * horizontal))

if __name__ == '__main__':
    main()
