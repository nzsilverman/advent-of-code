import statistics
import math
import numpy as np
import copy
import sys


def convert_hex_string_to_binary_string(hex_string):
    hex_to_binary = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
    }
    binary_string = ""
    for char in hex_string:
        binary_string += hex_to_binary[char]

    return binary_string


def read_input(filename):
    with open(filename, "r") as f:
        line = f.read().strip()
    return line

def part1(filename):
    hex_string = read_input(filename)
    binary_string = convert_hex_string_to_binary_string(hex_string)
    # binary_string = "00111000000000000110111101000101001010010001001000000000"

    idx = 0
    version_sum = 0
    while idx < len(binary_string):
        try:
            # print("version: {}".format(binary_string[idx:idx+3]))
            version = int(binary_string[idx:idx+3], 2)
            version_sum += version
            type_id = int(binary_string[idx+3:idx+6], 2)
            # print("version: {} type id: {}".format(version, type_id))
            idx += 6 # Increment 3 for version and 3 for type id
            
            if type_id == 4:
                # Literal value
                binary_literal = ""
                while True:
                    group_id = binary_string[idx]
                    idx += 1
                    binary_literal += binary_string[idx:idx+4]
                    idx += 4
                    
                    if group_id == '0':
                        # Last chunk found
                        break

            else:
                # Operator packet
                length_type_id = binary_string[idx]
                idx += 1
                # print("Operator packet found, length type id == {}".format(length_type_id))
                if length_type_id == '0':
                    # Next 15 bits are a number that represents the total length in bits of the sub packets
                    subpackets_length = int(binary_string[idx:idx+15], 2)
                    idx += 15
                else:
                    # Next 11 bits are a number that represents the number of sub packets immediately contained
                    num_subpackets = int(binary_string[idx:idx+11], 2)
                    idx += 11
        except Exception as e:
            # print("Invalid access, assuming 0 padding being read.")
            break

    print("Version sum: {}".format(version_sum))
    return version_sum

def check_part1_version_sum():
    if (part1('12.txt') != 12):
        print("Error with 12.txt")
        exit(-1)

    if (part1('16.txt') != 16):
        print("Error with 16.txt")
        exit(-1)

    if (part1('23.txt') != 23):
        print("Error with 23.txt")
        exit(-1)

    if (part1('31.txt') != 31):
        print("Error with 31.txt")
        exit(-1)
    
def part2(filename):
    hex_string = read_input(filename)
    print(hex_string)
    binary_string = convert_hex_string_to_binary_string(hex_string)
    print(binary_string)

    id_to_operation = {
        0   :   "+",
        1   :   "*",
        2   :   "min",
        3   :   "max",
        5   :   "gt",
        6   :   "lt",
        7   :   "==",

    }

    out = []

    idx = 0
    version_sum = 0
    while idx < len(binary_string):
        try:
            # print("version: {}".format(binary_string[idx:idx+3]))
            version = int(binary_string[idx:idx+3], 2)
            version_sum += version
            type_id = int(binary_string[idx+3:idx+6], 2)
            print("version: {} type id: {}".format(version, type_id))
            idx += 6 # Increment 3 for version and 3 for type id

            if type_id != 4:
                out.append(id_to_operation[type_id])
            
            if type_id == 4:
                print("literal found")
                # Literal value
                binary_literal = ""
                while True:
                    group_id = binary_string[idx]
                    idx += 1
                    binary_literal += binary_string[idx:idx+4]
                    idx += 4
                    
                    if group_id == '0':
                        # Last chunk found
                        break
                    
                out.append(int(binary_literal, 2))

            else:
                print("operator found")
                # Operator packet
                length_type_id = binary_string[idx]
                idx += 1
                # print("Operator packet found, length type id == {}".format(length_type_id))
                if length_type_id == '0':
                    # Next 15 bits are a number that represents the total length in bits of the sub packets
                    subpackets_length = int(binary_string[idx:idx+15], 2)
                    idx += 15
                else:
                    # Next 11 bits are a number that represents the number of sub packets immediately contained
                    num_subpackets = int(binary_string[idx:idx+11], 2)
                    idx += 11
        except Exception as e:
            print("Invalid access, assuming 0 padding being read.")
            print("Excpetion: {}".format(e))
            break

    print(out)

    val = 0
    operands = []
    resolved = []
    for char in reversed(out):
        print(char)
        if char not in ('+', '*', 'min', 'max'):
            operands.append(char)
        else:
            print(operands)
            if char == 'max':
                x = max(operands)
            elif char == 'min':
                x = min(operands)
            elif char == '*':
                x = np.prod(operands)
            elif char == '+':
                x = sum(operands)
            else:
                print("char: {}".format(x))
                x = char

            operands = []
            resolved.append(x)

    for char in operands:
        resolved.append(char)

    print(resolved)

    # if char == 'gt':
    #     x = 1 if operands[1] > operands[0] else 0
    #     val += x
    #     operands.pop()
    #     operands.pop()
    # elif char == 'lt':
    #     x = 1 if operands[0] > operands[1] else 0
    #     val += x
    #     operands.pop()
    #     operands.pop()
    # elif char == '==':
    #     x = 1 if operands[0] == operands[1] else 0
    #     val += x
    #     operands.pop()
    #     operands.pop()

    print("val: {}".format(val))
    return val

def operate(type_id, subpackets):
    x = None
    if type_id == 0:
        # sum operation
        x = sum(subpackets)
    elif type_id == 1:
        x = np.prod(subpackets)
    elif type_id == 2:
        x = min(subpackets)
    elif type_id == 3:
        x = max(subpackets)
    elif type_id == 5:
        x = 1 if subpackets[0] > subpackets[1] else 0
    elif type_id == 6:
        x = 1 if subpackets[1] > subpackets[0] else 0
    elif type_id == 7:
        x = 1 if subpackets[0] == subpackets[1] else 0

    return x

def recursive_parse_packet(packet, start_idx, end_idx=-1):
    """ 
        Recursively parse packets starting at start_idx and ending at end_idx

        Return:
            Value, Next Index 
    """
    if start_idx == end_idx:
        return None, None

    # Discard the zeros at the end
    if start_idx > len(packet) - 4:
        return None, None


    idx = start_idx
    version = int(packet[idx:idx+3], 2)
    type_id = int(packet[idx+3:idx+6], 2)
    idx += 6 # Increment 3 for version and 3 for type id
    
    if type_id == 4:
        # Literal value
        binary_literal = ""
        while True:
            group_id = packet[idx]
            idx += 1
            binary_literal += packet[idx:idx+4]
            idx += 4
            
            if group_id == '0':
                # Last chunk found
                break
            
        binary_as_int = int(binary_literal, 2)
        return binary_as_int, idx

    else:
        # Operator packet
        length_type_id = packet[idx]
        idx += 1
        subpackets = []
        next_start = None

        if length_type_id == '0':
            # Next 15 bits are a number that represents the total length in bits of the sub packets
            subpackets_length = int(packet[idx:idx+15], 2)
            idx += 15
            end = idx + subpackets_length
            prev_index = None
            while idx != None:
                prev_index = idx
                x, idx = recursive_parse_packet(packet, idx, end)
                if x is not None:
                    subpackets.append(x)
            next_start = prev_index
        else:
            # Next 11 bits are a number that represents the number of sub packets immediately contained
            num_subpackets = int(packet[idx:idx+11], 2)
            idx += 11
            for i in range(num_subpackets):
                x, idx = recursive_parse_packet(packet, idx)
                if x is not None:
                    subpackets.append(x)
            next_start = idx

        return operate(type_id, subpackets), next_start



def part2_recursive(filename):
    hex_string = read_input(filename)
    binary_string = convert_hex_string_to_binary_string(hex_string)
    retval = recursive_parse_packet(binary_string, 0)[0]

    print("retval :{}".format(retval))


def main():
    filename = 'input.txt'
    # filename = '16.txt'
    # filename = '3.txt'
    # filename = '54.txt'
    # filename = '1.txt'
    # filename = '1.2.txt'
    # filename = '0.txt'

    # check_part1_version_sum()

    # print("**********************************")
    # print("Part 1, input: {}".format(filename))
    # part1(filename)
    # print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    # part2(filename)
    part2_recursive(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
