import statistics
import math
import numpy as np
import copy
import sys


def read_input(filename):
    with open(filename, "r") as f:
        p1_start, p2_start = [int(c[1]) for c in [y.split(': ') for y in [x.strip() for x in f.readlines()]]]
    return p1_start, p2_start

class deterministic_die():
    num_rolls = 0

    def roll(self):
        self.num_rolls += 1
        if self.num_rolls % 100 == 0:
            roll = 100
        else:
            roll = self.num_rolls % 100
        return roll

class player():
    score = 0

    def __init__(self, position):
        assert 1 <= position <= 10
        self.position = position

    def move_forward(self, num):
        """ Move player to new square and increase score. """
        new_position = (self.position + num) % 10
        if new_position == 0:
            self.position = 10
        else:
            self.position = new_position
        self.score += self.position

def part1(filename):
    p1_start, p2_start = read_input(filename)

    die = deterministic_die()
    p1 = player(p1_start)
    p2 = player(p2_start)

    while True:
        die_rolls_sum = 0
        for i in range(3):
            die_rolls_sum += die.roll()
        p1.move_forward(die_rolls_sum)
        if p1.score >= 1000:
            print("Player 1 wins.")
            print("Player 2 score: {}, Number of die rolls: {}".format(p2.score, die.num_rolls))
            print("Player 2 score * number of die rolls: {}".format(p2.score * die.num_rolls))
            break

        die_rolls_sum = 0
        for i in range(3):
            die_rolls_sum += die.roll()
        p2.move_forward(die_rolls_sum)
        if p2.score >= 1000:
            print("Player 2 wins.")
            print("Player 1 score: {}, Number of die rolls: {}".format(p1.score, die.num_rolls))
            print("Player 1 score * number of die rolls: {}".format(p1.score * die.num_rolls))
            break

P1_SUM = 0
P2_SUM = 0

def dirac_game(p1, p2):
    global P1_SUM
    global P2_SUM
    """ returns p1_sum, p2_sum """

    while True:
        for p1_roll in range(1,4):
            p1_copy = copy.deepcopy(p1)
            p1_copy.move_forward(p1_roll)
            if p1_copy.score >= 21:
                P1_SUM += 1
                print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
                return
            p2_copy = copy.deepcopy(p2)
            dirac_game(p1_copy, p2_copy)


        for p2_roll in range(1,4):
            p2_copy = copy.deepcopy(p2)
            p2_copy.move_forward(p2_roll)
            if p2_copy.score >= 21:
                P2_SUM += 1
                print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
                return
            p1_copy = copy.deepcopy(p1)
            dirac_game(p1_copy, p2_copy)

## Map a tuple of (p1_score, p1_roll, p2_score, p2_roll) to an outcome of p1(1) p2(2)
## Map a tuple of (p1_score, p2_score) to an outcome of p1(1) or p2(2). roll_sum is sum of all rolls to this point
# # Map a tuple of (position, current_player_score, other_player_score) to (current player num wins, other player num wins)
# MEMO = {}
# MEMO_SET = set()
# def dirac_game_with_memo_bad(p1, p2, path):
#     """ play dirac game
#         
#         Args:
#             p1      player object
#             p2      player object
#             path    path to get here as tuples of (p1_score, p2_score)
#     """
#     global P1_SUM
#     global P2_SUM
#     global MEMO
#     global MEMO_SET
#     """ returns p1_sum, p2_sum """
# 
#     while True:
#         for p1_roll in range(1,4):
# 
#             p1_copy = copy.deepcopy(p1)
#             p1_copy.move_forward(p1_roll)
#             path_copy = copy.deepcopy(path)
#             path_copy.append((p1_copy.score, p2.score, p1_roll))
#             if p1_copy.score >= 21:
#                 P1_SUM += 1
#                 print("path_copy: {}".format(path_copy))
#                 print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
#                 for path in path_copy:
#                     assert path not in MEMO
#                     MEMO[path] = 1
#                 return
#             p2_copy = copy.deepcopy(p2)
#             if (p1_copy.score, p2.score) in  MEMO:
#                 if MEMO[(p1_copy.score, p2.score)] == 1:
#                     P1_SUM += 1
#                 elif MEMO[(p1_copy.score, p2.score)] == 2: 
#                     P2_SUM += 1
#                 print(MEMO)
#                 return
#             else:
#                 dirac_game_with_memo(p1_copy, p2_copy, path_copy)
# 
# 
#         for p2_roll in range(1,4):
#             p2_copy = copy.deepcopy(p2)
#             p2_copy.move_forward(p2_roll)
#             path_copy = copy.deepcopy(path)
#             path_copy.append((p1.score, p2_copy.score))
#             if p2_copy.score >= 21:
#                 P2_SUM += 1
#                 print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
#                 print("path_copy: {}".format(path_copy))
#                 for path in path_copy:
#                     assert path not in MEMO
#                     MEMO[path] = 2
#                 print(MEMO)
#                 return
#             p1_copy = copy.deepcopy(p1)
#             if (p1.score, p2_copy.score) in  MEMO:
#                 if MEMO[(p1.score, p2_copy.score)] == 1:
#                     P1_SUM += 1
#                 elif MEMO[(p1.score, p2_copy.score)] == 2: 
#                     P2_SUM += 1
#                 return
#             else:
#                 dirac_game_with_memo(p1_copy, p2_copy, path_copy)

# Map a tuple of (position, current_player_score, other_player_score) to (current player num wins, other player num wins)
MEMO = {}
MEMO_SET = set()
def dirac_game_with_memo(p1, p2, path):
    """ play dirac game
        
        Args:
            p1      player object
            p2      player object
            # path    path to get here as tuples of (position, current_player_score, other_player_score)
            path    path to get here as tuples of (p1_position, p2_position, p1_score, p2_score)
    """
    global P1_SUM
    global P2_SUM
    global MEMO
    global MEMO_SET
    """ returns p1_sum, p2_sum """

    while True:
        for p1_roll in range(1,4):
            for p2_roll in range(1, 4):
                p1_copy = copy.deepcopy(p1)
                p2_copy = copy.deepcopy(p2)
                path_copy = copy.deepcopy(path)

                p1_copy.move_forward(p1_roll)
                p2_copy.move_forward(p2_roll)
                memo_tuple = (p1_copy.position, p2_copy.position, p1_copy.score, p2_copy.score)
                path_copy.append(memo_tuple)

                if p1_copy.score >= 21:
                    P1_SUM += 1
                    print("Player 1 Won. P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
                    for item in path_copy:
                        if item not in MEMO:
                            MEMO[item] = [1, 0]
                        else:
                            MEMO[item][0] += 1
                    return

                if p2_copy.score >= 21:
                    P2_SUM += 1
                    print("Player 2 Won. P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
                    for item in path_copy:
                        if item not in MEMO:
                            MEMO[item] = [0, 1]
                        else:
                            MEMO[item][1] += 1
                    return

                if memo_tuple in MEMO:
                    print("Memo being used for tuple: {}. MEMO[{}]={}".format(memo_tuple, memo_tuple, MEMO[memo_tuple]))
                    p1_wins, p2_wins = MEMO[memo_tuple]
                    print("p1 wins: {}, p2 wins: {}".format(p1_wins, p2_wins))
                    print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))

                    P1_SUM += p1_wins
                    P2_SUM += p2_wins
                    return
                else:
                    dirac_game_with_memo(p1_copy, p2_copy, path_copy)

# def dirac_game_with_memo(p1, p2, path):
#     """ play dirac game
#         
#         Args:
#             p1      player object
#             p2      player object
#             path    path to get here as tuples of (position, current_player_score, other_player_score)
#     """
#     global P1_SUM
#     global P2_SUM
#     global MEMO
#     global MEMO_SET
#     """ returns p1_sum, p2_sum """
# 
#     while True:
#         for p1_roll in range(1,4):
#             p1_copy = copy.deepcopy(p1)
#             p2_copy = copy.deepcopy(p2)
#             p1_copy.move_forward(p1_roll)
#             memo_tuple = (p1_copy.position, p1_copy.score, p2_copy.score)
#             path_copy = copy.deepcopy(path)
#             path_copy.append(memo_tuple)
#             if p1_copy.score >= 21:
#                 P1_SUM += 1
#                 print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
#                 for item in path_copy:
#                     if item not in MEMO:
#                         MEMO[item] = 1
#                     else:
#                         MEMO[item] += 1
#                 return
# 
#             if memo_tuple in MEMO:
#                 print(f"player 1 accessing memo: {memo_tuple}")
#                 P1_SUM += MEMO[memo_tuple]
#                 return
# 
#             dirac_game_with_memo(p1_copy, p2_copy, path_copy)
# 
# 
#         for p2_roll in range(1,4):
#             p1_copy = copy.deepcopy(p1)
#             p2_copy = copy.deepcopy(p2)
#             p2_copy.move_forward(p2_roll)
#             memo_tuple = (p2_copy.position, p2_copy.score, p1_copy.score)
#             path_copy = copy.deepcopy(path)
#             path_copy.append(memo_tuple)
#             if p2_copy.score >= 21:
#                 P2_SUM += 1
#                 print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
#                 for item in path_copy:
#                     if item not in MEMO:
#                         MEMO[item] = 1
#                     else:
#                         MEMO[item] += 1
#                 return
# 
#             if memo_tuple in MEMO:
#                 print(f"player 2 accessing memo: {memo_tuple}")
#                 P2_SUM += MEMO[memo_tuple]
#                 return
# 
#             dirac_game_with_memo(p1_copy, p2_copy, path_copy)
    
def part2(filename):
    p1_start, p2_start = read_input(filename)

    p1 = player(p1_start)
    p2 = player(p2_start)
    dirac_game(p1, p2)
    print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))

def part2_memo(filename):
    p1_start, p2_start = read_input(filename)

    p1 = player(p1_start)
    p2 = player(p2_start)
    dirac_game_with_memo(p1, p2, [] )
    print("P1_SUM: {}, P2_SUM: {}".format(P1_SUM, P2_SUM))
    # print("MEMO: {}".format(MEMO))

def main(filename):
    print("**********************************")
    print("Part 1, input: {}".format(filename))
    part1(filename)
    print("**********************************")

    print("\n\n**********************************")
    print("Part 2, input: {}".format(filename))
    # part2(filename)
    part2_memo(filename)
    print("**********************************")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: <filename>")
        exit(-1)
    main(sys.argv[1])
