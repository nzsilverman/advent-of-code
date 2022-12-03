import copy
def read_input(filename):
    fish = []
    with open(filename, "r") as f:
        for line in f:
            fish_line = [int(fish) for fish in line.strip().split(',')]
            fish.extend(fish_line)
    return fish
            

def puzzle(days):
    fish_list = read_input('input.txt')
    # fish_list = read_input('example.txt')

    fish_list = grow_fish(days, fish_list)
    
    print("After {} days: {}".format(days, len(fish_list)))

def puzzle2(days):
    fish_list = read_input('input.txt')
    # fish_list = read_input('example.txt')

    fish_map = grow_fish_with_map(days, fish_list)

    count = 0
    for fish in fish_map:
        count += fish_map[fish]
    
    print("After {} days: {}".format(days, count))

def grow_fish(days, fish_list):
    """ Simulate growing fish. """
    for i in range(days):
        fish_to_append = 0
        for idx,fish in enumerate(fish_list):
            if fish == 0:
                fish_list[idx] = 6
                fish_to_append += 1
            else:
                fish_list[idx] -= 1

        for i in range(fish_to_append):
            fish_list.append(8)

    return fish_list

def grow_fish_with_map(days, fish_list):
    """ Simulate growing fish by recording how many fish are at each lifecycle stage. """
    fish_map = {
        0   :   0,
        1   :   0,
        2   :   0,
        3   :   0,
        4   :   0,
        5   :   0,
        6   :   0,
        7   :   0,
        8   :   0,
    }
    for fish in fish_list:
        fish_map[fish] += 1

    for day in range(days):
        new_fish_spawned = 0
        for i in range(8):
            if i == 0:
                new_fish_spawned = fish_map[0]

            fish_map[i] = fish_map[i+1]

        fish_map[8] = new_fish_spawned
        fish_map[6] += new_fish_spawned

    return fish_map
                

def main():
    print("part 1: ")
    puzzle(80)

    print("part 2: ")
    puzzle2(256)

if __name__ == '__main__':
    main()
