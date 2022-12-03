import copy
def main():
    with open("input.txt", "r") as f:
    # with open("simple.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

        binary_len = len(lines[0])
        total_nums = len(lines)
        oxygen = copy.deepcopy(lines)
        for i in range(binary_len):
            l = [int(digit[i]) for digit in oxygen]
            ones = sum(l)
            print("ones: {}".format(ones))
            if ones >= (len(oxygen) - ones):
                print("keeping ones") 
                oxygen = [line for line in oxygen if int(line[i]) == 1]
            else:
                print("keeping 0s") 
                oxygen = [line for line in oxygen if int(line[i]) == 0]

            if len(oxygen) == 1:
                break

            print(oxygen)


        c02 = copy.deepcopy(lines)
        for i in range(binary_len):
            l = [int(digit[i]) for digit in c02]
            ones = sum(l)
            if ones >= (len(c02) - ones):
                # 1s is most common
               c02 = [line for line in c02 if int(line[i]) == 0]
            else:
               c02 = [line for line in c02 if int(line[i]) == 1]

            if len(c02) == 1:
                break
            print(i)
            print(len(c02))

        oxygen = ''.join(oxygen)
        c02 = ''.join(c02)
        print(oxygen)

        o = int(oxygen, 2)
        c = int(c02, 2)

        print("oxygen: {}".format(int(oxygen, 2)))
        print("c02: {}".format(int(c02, 2)))
        print("multiplied: {}".format(o*c))

    



if __name__ == '__main__':
    main()
