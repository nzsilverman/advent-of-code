import statistics
import math
import numpy as np
import copy

def read_input(filename):
    """ Return a list of tuples where each tuple is a signal and then segments list. """
    input_list = []
    with open(filename, "r") as f:
        for line in f:
            signals_segments = line.strip().split('|')
            signals_segments_tuple = (sorted(signals_segments[0].split(), key=len), signals_segments[1].split())
            input_list.append(signals_segments_tuple)
    return input_list

def part1():
    # input_list = read_input('example.txt')
    input_list = read_input('input.txt')
    count = 0
    for entry in input_list:
        signals, segments = entry
        for segment in segments:
            if len(segment) in [2, 4, 3, 7]:
                count += 1
    print("count: {}".format(count))
        

def part2_bad():
    # input_list = read_input('example.txt')
    input_list = read_input('one_line_example.txt')
    # input_list = read_input('input.txt')

    # Map the signal to the segment. Start with a complete list
    mapping_template = {
        "a" :   ['a','b','c','d','e','f','g'],
        "b" :   ['a','b','c','d','e','f','g'],
        "c" :   ['a','b','c','d','e','f','g'],
        "d" :   ['a','b','c','d','e','f','g'],
        "e" :   ['a','b','c','d','e','f','g'],
        "f" :   ['a','b','c','d','e','f','g'],
        "g" :   ['a','b','c','d','e','f','g'],
    }

    # Signal length to valid letters in the segment
    len_to_valid_letters = {
            2   :   ['c', 'f'],
            3   :   ['a', 'c', 'f'],
            4   :   ['b', 'c', 'd', 'f'],
            5   :   ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            6   :   ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            7   :   ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    }

    for entry in input_list:
        mapping = copy.deepcopy(mapping_template)
        signals, segments = entry
        print("signals: {}".format(signals))
        for signal in signals:
            valid_letters = len_to_valid_letters[len(signal)]
            print("signal: {}".format(signal))
            print("valid letters: {}".format(valid_letters))
            for letter in signal:
                print("letter: {}".format(letter))
                letters_to_remove = []
                for mappped_letter in mapping[letter]:
                    if mappped_letter not in valid_letters:
                        letters_to_remove.append(mappped_letter)

                for letter_to_remove in letters_to_remove:
                    print("removing {} for mapping letter: {}".format(letter_to_remove, letter))
                    mapping[letter].remove(letter_to_remove)

                print("mapping[{}]: {}".format(letter, mapping[letter]))

        all_mappings_found = False
        while (not all_mappings_found): 
            equal_sets = []
            for letter in mapping:
                for second_letter in mapping:
                    if letter != second_letter and set(mapping[letter]) == set(mapping[second_letter]):
                        equal_sets.append(mapping[letter])

            print("Equal sets: {}".format(equal_sets))
            for equal_set in equal_sets:
                if len(equal_set) == equal_sets.count(equal_set):
                    print("equal set satisfied: {}".format(equal_set))
                    # These sets have enough variables to satisfy the equation, remove these from all other sets
                    letters_to_remove_from_all = []
                    for letter in mapping:
                        if set(mapping[letter]) != set(equal_set):
                            for equal_sets_letter in equal_set:
                                print("Removing {} from mapping[{}]".format(equal_sets_letter, letter))
                                if equal_sets_letter in mapping[letter]:
                                    mapping[letter].remove(equal_sets_letter)

                            if len(mapping[letter]) == 1:
                                # A match between signal to segment has been found
                                letters_to_remove_from_all.append(mapping[letter][0])

                    print("letters to remove from all: {}".format(letters_to_remove_from_all))
                    for letter in mapping:
                        for letter_to_remove in letters_to_remove_from_all:
                            print("trying to remove letter: {}".format(letter_to_remove))
                            if len(mapping[letter]) != 1:
                                if letter_to_remove in mapping[letter]:
                                    mapping[letter].remove(letter_to_remove)

                    if len(equal_set) == 2:
                        # Special case
                        pass

            print("mappings: {}".format(mapping))

            all_mappings_found = True
            for letter in mapping:
                if len(mapping[letter]) > 1:
                    all_mappings_found = False
             

    print(mapping)
    # for key in mapping:
    #     if len(mapping[key]) 
    #     

def check_if_a_in_b(a, b):
    """ check if the characters in a are all present in b. """
    for character in a:
        if character not in b:
            return False
    return True

def check_if_keys_match(a, b):
    """ check if the characters in a are all present in b and vice versa. """
    for character in a:
        if character not in b:
            return False

    for character in b:
        if character not in a:
            return False

    return True

def part2():
    # input_list = read_input('example.txt')
    # input_list = read_input('one_line_example.txt')
    input_list = read_input('input.txt')
    
    # map a segment number to a signal
    mapping_template = {
        0   :   '',
        1   :   '',
        2   :   '',
        3   :   '',
        4   :   '',
        5   :   '',
        6   :   '',
        7   :   '',
        8   :   '',
        9   :   '',
    }


    answer = 0
    for entry in input_list:
        mapping = copy.deepcopy(mapping_template)
        signals, segments = entry

        # Put in mappings of known size
        for signal in signals:
            if len(signal) in [2, 4, 3, 7]:
                if len(signal) == 2:
                    mapping[1] = signal
                elif len(signal) == 4:
                    mapping[4] = signal
                elif len(signal) == 3:
                    mapping[7] = signal
                elif len(signal) == 7:
                    mapping[8] = signal

        # Find mapping 3
        for signal in signals:
            if len(signal) == 5:
                if check_if_a_in_b(mapping[1],signal):
                    mapping[3] = signal
                    break

        # Find mapping 5 and 2
        for signal in signals:
            if len(signal) == 5 and signal != mapping[3]:
                diff = set(signal).symmetric_difference(set(mapping[8]))
                all_in_4 = True

                for item in diff:
                    if not check_if_a_in_b(item, mapping[4]):
                        all_in_4 = False
                if all_in_4: 
                    mapping[2] = signal
                else:
                    mapping[5] = signal

        # Find mapping for 0
        for signal in signals:
            if len(signal) == 6:
                diff_5_2 = set(mapping[5]).symmetric_difference(set(mapping[2]))
                diff_5_2_str = ''.join([x for x in diff_5_2])
                diff = set(signal).symmetric_difference(set(mapping[8]))
                diff_string = ''.join([x for x in diff])
                if not check_if_a_in_b(diff_string, diff_5_2_str):
                    mapping[0] = signal

        # Find mapping for 6 and 9
        for signal in signals:
            if (len(signal) == 6 and signal != mapping[0]):
                diff = set(signal).symmetric_difference(set(mapping[8]))
                diff_string = ''.join([x for x in diff])
                if check_if_a_in_b(diff_string, mapping[4]):
                    mapping[6] = signal
                else:
                    mapping[9] = signal

        # Printing for help
        # for signal in signals:
        #     for key in mapping:
        #         if check_if_keys_match(mapping[key], signal):
        #             print('{}: {}'.format(signal, key))

        output = []
        for segment in segments:
            for key in mapping:
                if check_if_keys_match(mapping[key], segment):
                    output.append(key)
        output_str = [str(x) for x in output]
        output_int = int(''.join(output_str))
        answer += output_int
        print("{}: {}".format(segments, output_int))

    print("answer: {}".format(answer))



def main():
    # part1()
    part2()

if __name__ == "__main__":
    main()
