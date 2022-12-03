import numpy as np

def read_input(filename):
    """ Read bingo input file and return parsed data structures.
        
        Args:
            filename        Name of bingo configuration file to read in

        Returns:
            (moves, boards, board_scores)   
                moves           A list of the moves as strings
                boards          A list of boards, where each entry is a 2D numpy array representing the board
                board_scores    A list of board scores, where each entry is a 2D numpy array that is initialized to 
                                all zeroes and is the same size as the board at the corresponding index in the boards list.
                                In this list, a 1 will represent a marked square, and a 0 will represent a non marked score.
    """
    moves = []
    boards = [] # A list containing individual boards. Individual boards are 2d arrays
    board = [] # A temporary board used to create new boards to add to the boards array
    board_scores = []
    with open(filename, "r") as f:
        for line in f:
            if not moves: # Must be the first line
                moves = [int(move) for move in line.strip().split(',')]
            elif line == '\n':
                # Board is done being read in, add to the boards list and restart
                if board:
                    np_array = np.array(board)
                    boards.append(np_array)
                    board_scores.append(np.zeros(np_array.shape))
                board = []
            else:
                board.append([int(square) for square in line.strip().split()])

        # Add the last board since no newline will be found
        if board:
            np_array = np.array(board)
            boards.append(np_array)
            board_scores.append(np.zeros(np_array.shape))

    return moves, boards, board_scores

def check_if_winner(board_score):
    """ Returns True/False if a board is a winner.

    A winner is defined as a complete column or row.
    """
    num_rows, num_cols = board_score.shape
    column_sums = (np.sum(board_score, axis=0))
    row_sums = (np.sum(board_score, axis=1))

    if num_rows in row_sums:
        print("A complete row has been found!")
        return True

    if num_cols in column_sums:
        print("A complete column has been found!")
        return True


def puzzle1():
    moves, boards, board_scores = read_input('input.txt')
    # moves, boards, board_scores = read_input('example.txt')

    for move in moves:
        for idx, board in enumerate(boards):
            where_is_move = np.asarray(np.where(board == move)).T.tolist()

            # Mark squares where number matches move
            for row, col in where_is_move:
                board_scores[idx][row][col] = 1

            if check_if_winner(board_scores[idx]):
                print("Winner found. Index: {}. Last Move: {}".format(idx, move))

                # Create a mask that is False if an element was marked, and True if it was unmarked
                unmarked_mask = []
                for line in board_scores[idx]:
                    new_line = []
                    for item in line:
                        if item == 1:
                            new_line.append(False)
                        else:
                            new_line.append(True)
                    unmarked_mask.append(new_line)
                unmarked_mask = np.array(unmarked_mask, dtype=bool)
                
                sum_all_unmarked_squares = np.sum(board, where=unmarked_mask)
                return move * sum_all_unmarked_squares

def puzzle2():
    moves, boards, board_scores = read_input('input.txt')
    # moves, boards, board_scores = read_input('example.txt')

    # A queue keeping track of the scores for boards that finish, in order of when they finish
    finished_boards = [] 
    finished_boards_idx = []

    for move in moves:
        for idx, board in enumerate(boards):
            if idx not in finished_boards_idx:
                where_is_move = np.asarray(np.where(board == move)).T.tolist()

                # Mark squares where number matches move
                for row, col in where_is_move:
                    board_scores[idx][row][col] = 1

                if check_if_winner(board_scores[idx]):
                    print("Winner found. Index: {}. Last Move: {}".format(idx, move))

                    # Create a mask that is False if an element was marked, and True if it was unmarked
                    unmarked_mask = []
                    for line in board_scores[idx]:
                        new_line = []
                        for item in line:
                            if item == 1:
                                new_line.append(False)
                            else:
                                new_line.append(True)
                        unmarked_mask.append(new_line)
                    unmarked_mask = np.array(unmarked_mask, dtype=bool)
                    
                    sum_all_unmarked_squares = np.sum(board, where=unmarked_mask)
                    finished_boards.append(move * sum_all_unmarked_squares)
                    finished_boards_idx.append(idx)
                    if len(finished_boards) == len(boards):
                        print(finished_boards)
                        # All boards have been finished
                        return finished_boards[-1]

def main():
    print("************* puzzle 1 *******************")
    result = puzzle1()
    print("Puzzle 1 answer: {}".format(result))
    print("************* end puzzle 1 *******************")

    print("************* puzzle 2 *******************")
    result = puzzle2()
    print("Puzzle 2 answer: {}".format(result))
    print("************* end puzzle 2 *******************")


if __name__ == '__main__':
    main()
