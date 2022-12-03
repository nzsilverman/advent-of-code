def part_1():
    choice_to_value = {
                'X':1,
                'Y':2,
                'Z':3
            }
    choice_to_play = {
            'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors'
            }
    elf_to_play = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
            }
    with open('input.txt', 'r') as f:
    #with open('example.txt', 'r') as f:
        total_score = 0
        for line in f:
            round_score = 0
            elf, choice = line.strip().split()
            round_score = choice_to_value[choice]

            elf_play = elf_to_play[elf]
            choice_play = choice_to_play[choice]

            if choice_play == 'rock' and elf_play == 'scissors':
                round_score += 6
            elif choice_play == 'paper' and elf_play == 'rock':
                round_score += 6
            elif choice_play == 'scissors' and elf_play == 'paper':
                round_score += 6
            elif choice_play == elf_play:
                round_score += 3

            print(f"round_score: {round_score}")

            total_score += round_score

        print(f"total score: {total_score}")

def part_2():
    shape_to_value = {
                'rock':1,
                'paper':2,
                'scissors':3
            }
    elf_to_play = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors'
            }
    play_to_win = {
            'rock' : 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
            }
    play_to_lose = {
            'rock' : 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
            }
    # X = lose, Y= draw, Z = win
    with open('input.txt', 'r') as f:
    # with open('example.txt', 'r') as f:
        total_score = 0
        for line in f:
            round_score = 0
            elf, outcome = line.strip().split()

            elf_play = elf_to_play[elf]

            if outcome == 'X':
                # lose
                round_score += shape_to_value[play_to_lose[elf_play]]
            if outcome == 'Y':
                # tie
                round_score += shape_to_value[elf_play]
                round_score += 3
            if outcome == 'Z':
                # win
                round_score += shape_to_value[play_to_win[elf_play]]
                round_score += 6


            print(f"round_score: {round_score}")

            total_score += round_score

        print(f"total score: {total_score}")



def main():
    print("Day 2")
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
