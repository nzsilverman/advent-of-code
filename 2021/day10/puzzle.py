import statistics
import math
import numpy as np
import copy

def read_input(filename):
    """ Return a numpy matrix. """
    with open(filename, "r") as f:
        input_list = [x.strip() for x in f.readlines()]
    return input_list

def part1(filename):
    first_illegal = {
        ')' :   0,
        ']' :   0,
        '}' :   0,
        '>' :   0,
    }
    input_list = read_input(filename)
    for line in input_list:
        stack = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                last = stack[-1]
                illegal_found = None
                if char == ')':
                    if last != '(':
                        illegal_found = char
                if char == ']':
                    if last != '[':
                        illegal_found = char
                if char == '}':
                    if last != '{':
                        illegal_found = char
                if char == '>':
                    if last != '<':
                        illegal_found = char
                if illegal_found:
                    first_illegal[illegal_found] += 1
                    break
                stack.pop()
    print(first_illegal)

    score_multiplier_map = {
        ')' :   3,
        ']' :   57,
        '}' :   1197,
        '>' :   25137,
    }
    score = 0
    for key in first_illegal:
        score += first_illegal[key] * score_multiplier_map[key]
    print('score: {}'.format(score))
        
def part2(filename):
    first_illegal = {
        ')' :   0,
        ']' :   0,
        '}' :   0,
        '>' :   0,
    }
    input_list = read_input(filename)
    incomplete_lines = []
    for line in input_list:
        stack = []
        illegal_found = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                last = stack[-1]
                illegal_found = None
                if char == ')':
                    if last != '(':
                        illegal_found = char
                if char == ']':
                    if last != '[':
                        illegal_found = char
                if char == '}':
                    if last != '{':
                        illegal_found = char
                if char == '>':
                    if last != '<':
                        illegal_found = char
                if illegal_found:
                    first_illegal[illegal_found] += 1
                    illegal_found = True
                    break
                stack.pop()
        if not illegal_found:
            print('stack: {}'.format(stack))
            incomplete_lines.append(line)

    incomplete_map = {
        ')' :   0,
        ']' :   0,
        '}' :   0,
        '>' :   0,
            }
    incomplete_list = []
    for line in incomplete_lines:
        stack = []
        incomplete = []
        for char in reversed(line):
            if char in [')', ']', '}', '>']:
                stack.append(char)
            else:
                # last = stack[0]
                if not stack:
                    missing = ''
                    if char == '(':
                        missing = ')'
                    if char == '{':
                        missing = '}'
                    if char == '<':
                        missing = '>'
                    if char == '[':
                        missing = ']'
                    incomplete_map[missing] += 1
                    incomplete.append(missing)
                else:
                    last = stack[-1]
                    match_found = True
                    if char == '(' and last == ')':
                        match_found = True
                    if char == '{' and last == '}':
                        match_found = True
                    if char == '<' and last == '>':
                        match_found = True
                    if char == '[' and last == ']':
                        match_found = True

                    if match_found:
                        stack.pop()
                
        print('incomplete: {}'.format(incomplete))
        incomplete_list.append(incomplete)

    score_multiplier_map = {
        ')' :  1,
        ']' :   2,
        '}' :   3,
        '>' :   4,
    }
    scores = []
    for incomplete in incomplete_list:
        score = 0
        for char in incomplete:
            score = (score * 5) + score_multiplier_map[char]
        scores.append(score)
    
    scores.sort()
    print(scores)
    print("answer: ")
    print(statistics.median(scores))


def main():
    filename = 'input.txt'
    # filename = 'example.txt'
    # filename = 'one.txt'
    # filename = 'two.txt'

    print("**********************************")
    print("Part 1, input: {}".format(filename))
    part1(filename)
    print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    part2(filename)
    print("**********************************")

if __name__ == "__main__":
    main()
