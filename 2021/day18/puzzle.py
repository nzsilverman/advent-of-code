import statistics
import math
import numpy as np
import copy
import sys

# THIS IS SOME OF THE WORST CODE I HAVE EVER WRITTEN. READER BEWARE


def read_input(filename):
    with open(filename, "r") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

def add_two_snail_numbers(num1, num2):
    """ add num2 to num1 """
    if num1 == '':
        return copy.deepcopy(num2)
    else:
        new_num = '[' + num1 + ',' + num2 + ']'
    return new_num

# def explode(number, idx):
#     """ Explode the snailfish number at a certain idx. 
#         idx must be to the start [ of the pair to explode
# 
#         Returns the exploded string
#     """
#     print("Explosion at idx: {}".format(idx))
#     print("number[{}]: {}".format(idx, number[idx]))
#     print("number[idx-5:idx+5]: {}".format(number[idx-5:idx+5]))
# 
#     # Idx points to [ in a [left,right] sequence
#     left_is_double_digit = False
#     if number[idx+2] == ',':
#         left = number[idx + 1]  # left is single digit
#     else:
#         left = number[idx+1:idx+3]
#         left_is_double_digit = True
# 
#     right_is_double_digit = False
#     left_offset = 0 if not left_is_double_digit else 1 # Extra left digits added
#     if number[idx+left_offset+4] == ']':
#         right = number[idx+left_offset+3] # right is single digit
#     else:
#         right = number[idx+left_offset+3:idx+left_offset+5]
# 
#     print("left: {}, right: {}".format(left, right))
# 
# 
#     left_num_idx = None
#     for i, char in enumerate(number[:idx]):
#             if char not in ['[', ']', ',']:
#                 left_num_idx = i
# 
#     right_num_idx = None
#     right_offset = 4 if not right_is_double_digit else 5 # offset to reach right bracket
#     for i, char in enumerate(number[idx+right_offset:]): 
#         if char not in ['[', ']', ',']:
#             right_num_idx = i + (idx + right_offset)
#             break
# 
# 
# 
#     # Update neighbor values if they exist
#     if left_num_idx:
#         val = str(int(number[left_num_idx]) + int(left))
#         number = number[:left_num_idx] + val + number[left_num_idx + 1:]
# 
#         # If this is a two digit number, the right index needs to be adjusted
#         if int(val) >= 10:
#             right_num_idx += 1
#             idx += 1
# 
#     if right_num_idx:
#         val = str(int(number[right_num_idx]) + int(right))
#         number = number[:right_num_idx] + val + number[right_num_idx + 1:]
# 
#     # Explode the current to zero
#     number = number[:idx] + '0' + number[idx + right_offset + left_offset + 1:]
# 
#     # print(f"left: {left}, right: {right}, left_num_idx: {left_num_idx}, right_num_idx: {right_num_idx}")
# 
#     # print("After explosion: {}".format(number))
#     return number

# def explode(number, idx):
#     """ Explode the snailfish number at a certain idx. 
#         idx must be to the [ of the pair to explode
# 
#         Returns the exploded string
#     """
#     print("Explosion at idx: {}".format(idx))
#     print("number[{}]: {}".format(idx, number[idx]))
#     print("number[idx-5:idx+5]: {}".format(number[idx-5:idx+5]))
# 
# 
#     right_bracket_idx = None
#     for i, char in enumerate(number[idx:]):
#         if char == ']':
#             right_bracket_idx = idx + i
#             break
# 
#     print("idx: {} right_bracket_idx: {}".format(idx, right_bracket_idx))
#     explode_list = number[idx+1:right_bracket_idx]
#     print("Explode list: {}".format(explode_list))
#     try:
#         left, right = [int(x) for x in explode_list.split(',')]
#         print(f'left: {left}, right: {right}')
#     except Exception as e:
#         for i in range(len(number)):
#             print("{}: {} \t".format(i, number[i]), end="")
#         print()
#         raise(e)
# 
#     left_num_idx = None
#     for i, char in enumerate(number[:idx]):
#             if char not in ['[', ']', ',']:
#                 left_num_idx = i
# 
#     right_num_idx = None
#     for i, char in enumerate(number[right_bracket_idx:]): 
#         if char not in ['[', ']', ',']:
#             right_num_idx = i + right_bracket_idx 
#             break
# 
#     # TODO I do not handle updating the left and right neighbors properly when those neighbores are double digits
#     # Update neighbor values if they exist
#     if left_num_idx:
#         val = str(int(number[left_num_idx]) + left)
#         if int(val) >= 10:
#             left = math.floor(int(val) / 2)
#             right = math.ceil(int(val) / 2)
#             number = number[:left_num_idx] + f'[{left},{right}]' + number[left_num_idx + 1:]
# 
#             # Update indices
#             # There was 1 digit, now there are 5 [x,y]. A difference of 4 from idx
#             if right_num_idx:
#                 right_num_idx += 4 
#             idx += 4
#             right_bracket_idx += 4
#         else:
#             number = number[:left_num_idx] + val + number[left_num_idx + 1:]
# 
#     if right_num_idx:
#         print('right_num_index: {}'.format(right_num_idx))
#         print('number[right_num_index]: {}'.format(number[right_num_idx]))
#         val = str(int(number[right_num_idx]) + right)
# 
#         if int(val) >= 10:
#             left = math.floor(int(val) / 2)
#             right = math.ceil(int(val) / 2)
#             number = number[:right_num_idx] + f'[{left},{right}]' + number[right_num_idx + 1:]
#         else:
#             number = number[:right_num_idx] + val + number[right_num_idx + 1:]
# 
#     # Explode the current to zero
#     number = number[:idx] + '0' + number[right_bracket_idx + 1:]
# 
#     # print("After explosion: {}".format(number))
# 
#     return number

def explode(number):
    """ Explode the first place possible in the number.

    Returns either a new, exploded number or None if no explosions.
    """
    bracket_count = 0
    for left_bracket_idx, char in enumerate(number):
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1

        if bracket_count > 4:
            pair_found = False
            chars_found = []
            for i, x in enumerate(number[left_bracket_idx + 1:]):
               chars_found.append(x)
               if x == ']':
                if '[' not in chars_found:
                    pair_found = True
                    break
            if not pair_found:
                continue
            # if number[left_bracket_idx+1] == '[':
            #     # Pair to explode is nested, must keep iterating
            #    continue
            # if number[left_bracket_idx+3] in ['[', ']', ',']:
            #     # Case such as: [[[[[0,[7,7]],1],2],3],4] where the [7,7] must explode before the [0, [7,7]]
            #     continue
            else:
                # Found the pair to explode. left_bracket_idx points to the [ bracket starting the pair

                for i, x in enumerate(number[left_bracket_idx+1:]):
                    if x == ']':
                        right_bracket_idx = i + left_bracket_idx + 1
                        break
                    elif x == ',':
                        comma_idx = i + left_bracket_idx + 1

                explode_left_num = int(''.join(number[left_bracket_idx+1:comma_idx]))
                explode_right_num = int(''.join(number[comma_idx+1:right_bracket_idx]))

                print("explode left num: {}, explode right num: {}".format(explode_left_num, explode_right_num))

                print("left bracket idx: {}\tcomma idx: {}\tright_bracket_idx: {}".format(left_bracket_idx, comma_idx, right_bracket_idx))

                left_num_start_idx = None # The start of the left number
                left_num_end_idx = None # The last digit in the left number
                print("number[:left_bracket_idx]")
                print(number[:left_bracket_idx])
                for i, x in enumerate(reversed(number[:left_bracket_idx])):
                        if x not in ['[', ']', ','] and not left_num_end_idx:
                            left_num_end_idx = left_bracket_idx - i - 1
                        elif left_num_end_idx:
                            if x == ',' or x == '[':
                                left_num_start_idx = left_bracket_idx - i 
                                break

                right_num_start_idx = None # The first digit of the right number
                right_num_end_idx = None # The last digit of the right number
                for i, x in enumerate(number[right_bracket_idx+1:]): 
                    if x not in ['[', ']', ','] and not right_num_start_idx:
                        right_num_start_idx = i + right_bracket_idx + 1
                        print("first right char found: {}".format(x))
                        print("right num start index: {}".format(right_num_start_idx))
                    elif right_num_start_idx:
                        if x == ',' or x == ']':
                            right_num_end_idx = i + right_bracket_idx 
                            break

                explosion = ''
                print("left num start idx: {} left num end idx: {}".format(left_num_start_idx, left_num_end_idx))
                if left_num_start_idx:
                    left_num = int(''.join(number[left_num_start_idx:left_num_end_idx + 1]))
                    print("Left Neighbor: {}".format(left_num))
                    left_plus_left = explode_left_num + left_num
                    explosion = number[:left_num_start_idx] + str(left_plus_left) + number[left_num_end_idx + 1:left_bracket_idx]
                else:
                    print("explosion after going to left bracket idx: {}".format(explosion))
                    explosion = number[:left_bracket_idx]

                # Add in the zero
                explosion = explosion + '0' 


                print("right num start idx: {} right num end idx: {}".format(right_num_start_idx, right_num_end_idx))
                if right_num_start_idx:
                    print("number[right_num_start_idx:right_num_end_idx + 1]:\t{}".format(number[right_num_start_idx:right_num_end_idx + 1]))
                    right_num = int(''.join(number[right_num_start_idx:right_num_end_idx + 1]))
                    print("Right Neighbor: {}".format(right_num))
                    right_plus_right = explode_right_num + right_num 
                    print("explosion before adding right: {}".format(explosion))
                    explosion += number[right_bracket_idx + 1:right_num_start_idx] + str(right_plus_right) + number[right_num_end_idx + 1:]
                    print("explosion after adding right: {}".format(explosion))
                else:
                    explosion += number[right_bracket_idx + 1:]
            
                print("Original number: {}".format(number))
                print("Explosion complete: {}".format(explosion))

                return explosion

    # Nothing got exploded
    return None


# def split(number, idx):
#     """ Split the snailfish number at a certain idx.
#         idx must be the idx of a char that is >= 10
#     """
#     print("Splitting at idx: {}".format(idx))
#     complete_number = number[idx]
#     end_idx_offset = 0
#     for c in number[idx+1:]:
#         if c not in ['[', ']', ',']:
#             complete_number += c
#             end_idx_offset += 1
#         else:
#             break
#     left = math.floor(int(complete_number) / 2)
#     right = math.ceil(int(complete_number) / 2)
#     number = number[:idx] + f'[{left},{right}]' + number[idx + end_idx_offset + 1:]
#     # print("After split: {}".format(number))
#     return number

def split(number):
    """ Split the snailfish number at the first possible spot. Return the split snailfish.
        If no splits neccessary, return none
    """
    for idx, char in enumerate(number):
        if char not in ['[', ']', ',']:
            complete_number = number[idx]
            end_idx_offset = 0
            for c in number[idx+1:]:
                if c not in ['[', ']', ',']:
                    complete_number += c
                    end_idx_offset += 1
                else:
                    break
            print("Complete number: {}".format(complete_number))
            if int(complete_number) >= 10:
                print("Splitting at idx: {}".format(idx))
                left = math.floor(int(complete_number) / 2)
                right = math.ceil(int(complete_number) / 2)
                number = number[:idx] + f'[{left},{right}]' + number[idx + end_idx_offset + 1:]
                print("After split: {}".format(number))
                return number
    # No splits
    return None

# def snailfish_reduce(number):
#     """ Reduce the snailfish number passed in and return the new number. """
# 
#     bracket_count = 0
#     for idx, char in enumerate(number):
#         if char == '[':
#             bracket_count += 1
#         elif char == ']':
#             bracket_count -= 1
# 
#         if bracket_count > 4:
#             if number[idx+1] == '[':
#                 # Pair to explode is nested, must keep iterating
#                 continue
#             if number[idx+3] in ['[', ']', ',']:
#                 # Case such as: [[[[[0,[7,7]],1],2],3],4] where the [7,7] must explode before the [0, [7,7]]
#                 continue
#             return explode(number, idx)
#         # elif char not in ['[', ']', ',']:
#         #     complete_number = ''
#         #     for c in number[idx:]:
#         #         if c not in ['[', ']', ',']:
#         #             complete_number += c
#         #         else:
#         #             break
#         #     if int(complete_number) >= 10:
#         #         return split(number, idx)
# 
#     # No reductions neccessary
#     print("No reductions neccessary for number: {}".format(number))
#     return None

def explode_as_much_as_possible(number):
    """ Explode as much as possible and return a new number. """
    prev = number
    while number != None:
        prev = copy.deepcopy(number)
        number = explode(number)

    return prev

def calculate_magnitude_for_pair(num1, num2):
    return 3*int(num1) + 2*int(num2)

def calculate_magnitude(number):
    num_list = [char for char in number]

def split_number_at_first_comma (number):
    """ Split the number at the first comma that divides the left half from the right half,
    removing the leading [ and ending ]. """

    # No splitting necessary
    if len(number) == 1:
        return number

    assert number[0] == '['
    assert number[-1] == ']'

    # Trim the leading and trailing [ ]
    number = number[1:-1]

    # If there are no more nested left right pairs, return the numbers
    if len(number) == 3:
        if number[1] == ',':
            if number[0] not in ['[', ']', ','] and number[2] not in ['[', ']', ',']:
                return number[0], number[2]

    # Otherwise, find the first split
    bracket_count = 0
    comma_idx = None
    for idx, char in enumerate(number):
        if char == '[':
            bracket_count += 1
        elif char == ']':
            bracket_count -= 1
        
        if bracket_count == 0:
            print("bracket count = 0 at idx: {}".format(idx))
            print("number[idx] = {}".format(number[idx]))
            print("number: {}".format(number))
            if char == ',':
                comma_idx = idx
                break

    print("comma idx: {}".format(comma_idx))
    assert comma_idx != None

    left = number[:comma_idx]
    right = number[comma_idx + 1:]
    print("left, right : {}, {}".format(left, right))
    
    return left, right

def calculate_magnitude_recursive (left, right):
    """ Calculate the magnitude recursively for a left and right side. """

    if len(left) == 1 and len(right) == 1:
        return calculate_magnitude_for_pair(int(left), int(right))

    if len(left) == 1:
        left_num = int(left)
    else:
        left_left, left_right = split_number_at_first_comma(left)
        left_num = calculate_magnitude_recursive(left_left, left_right)

    if len(right) == 1:
        right_num = int(right)
    else:
        right_left, right_right = split_number_at_first_comma(right)
        right_num = calculate_magnitude_recursive(right_left, right_right)

    return calculate_magnitude_for_pair(left_num, right_num)


def part1(filename):
    snailfish_numbers = read_input(filename)

    output = ''
    for number in snailfish_numbers:
        print("before add two snail numbers: {}".format(output))
        output = add_two_snail_numbers(output, number)
        print("After add two snail numbers: {}".format(output))

        # new = copy.deepcopy(output)
        # # while True:
        # for i in range(2):
        #     new = explode(new)
        #     print(new)
        #     if new is not None:
        #         output = new
        #     else:
        #         break
        # output = explode(output)
        # output = explode(output)
        output = explode_as_much_as_possible(output)

        print("Done exploding as much as possible, onto splitting and exploding")
        while True:
            split_num = split(output)
            if split_num is None:
                print("No splits necessary")
                break
            else:
                output = split_num
                output = explode_as_much_as_possible(output)

        # not_done_reducing = True
        # while not_done_reducing:
        #     reduced = snailfish_reduce(output)
        #     print("reduced: {}".format(reduced))
        #     if reduced is not None:
        #         output = reduced
        #     else:
        #         not_done_reducing = False
        print("****************************")
        print("After addition: {}".format(output))
        print("****************************")

    print("final reduced output:")
    print(output)

    left, right = split_number_at_first_comma(output)
    print("left: {}".format(left))
    print("right: {}".format(right))
    mag = calculate_magnitude_recursive(left, right)
    print("magnitude: {}".format(mag))

    
def part2(filename):
    snailfish_numbers = read_input(filename)

    mags = []
    for num1 in snailfish_numbers:
        for num2 in snailfish_numbers:
            print("num1 {}".format(num1))
            print("num2 {}".format(num2))
            if num1 != num2:
                output = add_two_snail_numbers(num1, num2)
                output = explode_as_much_as_possible(output)
                while True:
                    split_num = split(output)
                    if split_num is None:
                        break
                    else:
                        output = split_num
                        output = explode_as_much_as_possible(output)

                print("After addition: {}".format(output))
                left, right = split_number_at_first_comma(output)
                mag = calculate_magnitude_recursive(left, right)
                mags.append(mag)
    
    print("Magnitudes: {}".format(sorted(mags)))
    print("highest: {}".format(sorted(mags)[-1]))

def main():
    filename = 'input.txt'
    # filename = 'example.txt'
    # filename = 'example2.txt'
    # filename = '1to4.txt'
    # filename = '1to5.txt'
    # filename = '1to6.txt'
    # filename = 'reduce_example.txt'
    # filename = 'two_digits.txt'
    # filename = 'two_digits_2.txt'

    # print("**********************************")
    # print("Part 1, input: {}".format(filename))
    # part1(filename)
    # print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
