def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

        binary_len = len(lines[0])
        total_nums = len(lines)
        print(total_nums)
        gamma = []
        for i in range(binary_len):
            l = [int(digit[i]) for digit in lines]
            ones = sum(l)
            if ones > (total_nums - ones):
                gamma.append('1')
            else:
                gamma.append('0')

        gamma = ''.join(gamma)
        epsilon = ['1' if l == '0' else '0' for l in gamma]
        epsilon = ''.join(epsilon)
        print("gamma: {}".format(gamma))
        print("epsilon: {}".format(epsilon))
        gamma_base10= (int(gamma, 2))
        epsilon_base10= (int(epsilon, 2))

        print("gamma base 10: {}".format(gamma_base10))
        print("epsilon base 10: {}".format(epsilon_base10))
        print("gamma * epsilon: {}".format(gamma_base10 * epsilon_base10))


        # epsilon_base2 = bin(~gamma_base10)
        # print("gamma base 10: {}".format(gamma_base10))
        # print("gamma base 2: {}".format(bin(gamma_base10)))
        # print("epsilon base 2: {}".format(epsilon_base2))

    



if __name__ == '__main__':
    main()
