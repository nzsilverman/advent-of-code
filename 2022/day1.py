def read_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

def part_1():
    with open('input.txt', 'r') as f:
        current_elf_sum = 0
        elves = []
        for line in f:
            if line == '\n':
                elves.append(current_elf_sum)
                current_elf_sum = 0
            else:
                current_elf_sum += int(line)

    print(max(elves))

    elves.sort(reverse=True)
    print(sum(elves[:3]))


def main():
    print("Day 1")
    part_1()


if __name__ == '__main__':
    main()
