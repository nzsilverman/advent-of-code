from itertools import islice
def part_1(filename):
    score = 0
    with open(filename, 'r') as f:
        for line in f:
            items = [item for item in line.strip()]
            middle = int(len(items)/2)
            first = items[:middle]
            second = items[middle:]
            for item in second:
                if item in first:
                    value = 0
                    if item.isupper():
                        value += 26
                    value += ord(item.lower()) - 96
                    score += value
                    break
    print(f"score: {score}")

def part_2(filename):
    score = 0
    with open(filename, 'r') as f:
        while True:
            next_3_lines = list(islice(f, 3))
            if not next_3_lines:
                break
            sets = []
            for line in next_3_lines:
                s = set([item for item in line.strip()])
                sets.append(s)
            union_val = list(sets[0].intersection(sets[1], sets[2]))[0]
            value = 0
            if union_val.isupper():
                value += 26
            value += ord(union_val.lower()) - 96
            score += value
    print(f"score: {score}")



def main():
    print("Part 1")
    part_1('input.txt')
    print("Part 2")
    part_2('input.txt')


if __name__ == '__main__':
    main()
