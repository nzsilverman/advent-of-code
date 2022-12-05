from itertools import islice

def part_1(filename):
    count = 0
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            first_elf, second_elf = line.split(',')
            # print(f"first_elf: {first_elf}")
            first_start, first_end = first_elf.split('-')
            first_start = int(first_start)
            first_end = int(first_end)
            second_start, second_end = second_elf.split('-')
            second_start = int(second_start)
            second_end = int(second_end)

            # Second fully contained in first
            if first_start <= second_start and first_end >= second_end:
                count += 1
            elif first_start >= second_start and first_end <= second_end:
                count += 1

    print(f"count: {count}")

def part_2(filename):
    count = 0
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
        for line in lines:
            first_elf, second_elf = line.split(',')
            # print(f"first_elf: {first_elf}")
            first_start, first_end = first_elf.split('-')
            first_start = int(first_start)
            first_end = int(first_end)
            second_start, second_end = second_elf.split('-')
            second_start = int(second_start)
            second_end = int(second_end)

            if first_start <= second_start and first_end >= second_start:
                count += 1
            elif second_start <= first_start and second_end >= first_start:
                count += 1

    print(f"count: {count}")


def main():
    print("Part 1")
    # part_1('input.txt')
    # part_1('example.txt')
    print("Part 2")
    part_2('input.txt')
    # part_2('example.txt')


if __name__ == '__main__':
    main()
