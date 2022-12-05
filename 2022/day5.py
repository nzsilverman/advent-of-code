from collections import defaultdict, deque

def charIsUppercaseLetter(char):
    return 65 <= ord(char) <= 90

def part_1(filename):
    stacks = defaultdict(deque) # map char idx to stack
    instructions = deque()
    stack_num_to_idx = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            if '[' in line: # Parsing stacks
                for idx,char in enumerate(line):
                    if charIsUppercaseLetter(char):
                        print(f"char: {char}, idx: {idx}")
                        stacks[idx].appendleft(char)
            elif 'move' in line: # parsing instructions
                itersString, moveString = line.split(' from ')
                iters = int(itersString.split()[1])
                fromStack, toStack = [stack_num_to_idx[int(x)] for x in moveString.split(' to ')]
                move = (iters, fromStack, toStack)
                instructions.append(move)
            elif '1' in line: # parsing indexes
                for idx, char in enumerate(line):
                    if char != ' ' and char != '\n':
                        stack_num_to_idx[int(char)] = idx
        print(stacks)
        for iters, fromStack, toStack in instructions:
            for i in range(iters):
                stacks[toStack].append(stacks[fromStack].pop())

        print(stacks)

        print("Answer:")
        for i in range(len(stack_num_to_idx)):
            print(stacks[stack_num_to_idx[i+1]][-1], end="")

def part_2(filename):
    stacks = defaultdict(deque) # map char idx to stack
    instructions = deque()
    stack_num_to_idx = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            if '[' in line: # Parsing stacks
                for idx,char in enumerate(line):
                    if charIsUppercaseLetter(char):
                        print(f"char: {char}, idx: {idx}")
                        stacks[idx].appendleft(char)
            elif 'move' in line: # parsing instructions
                itersString, moveString = line.split(' from ')
                iters = int(itersString.split()[1])
                fromStack, toStack = [stack_num_to_idx[int(x)] for x in moveString.split(' to ')]
                move = (iters, fromStack, toStack)
                instructions.append(move)
            elif '1' in line: # parsing indexes
                for idx, char in enumerate(line):
                    if char != ' ' and char != '\n':
                        stack_num_to_idx[int(char)] = idx
        print(stacks)
        for iters, fromStack, toStack in instructions:
            crates = deque()
            for i in range(iters):
                crates.appendleft(stacks[fromStack].pop())
            for crate in crates:
                stacks[toStack].append(crate)

        print(stacks)

        print("Answer:")
        for i in range(len(stack_num_to_idx)):
            print(stacks[stack_num_to_idx[i+1]][-1], end="")



def main():
    # print("Part 1")
    # part_1('input.txt')
    # part_1('example.txt')
    print("Part 2")
    part_2('input.txt')
    # part_2('example.txt')


if __name__ == '__main__':
    main()
