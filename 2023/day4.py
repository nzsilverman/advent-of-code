import sys
from collections import deque


def PrintRed(skk, end="\n"):
  PrintDebug("\033[91m{}\033[00m".format(skk), end=end)


def PrintGreen(skk, end="\n"):
  PrintDebug("\033[92m{}\033[00m".format(skk), end=end)


def PrintYellow(skk, end="\n"):
  PrintDebug("\033[93m{}\033[00m".format(skk), end=end)


def PrintLightPurple(skk, end="\n"):
  PrintDebug("\033[94m{}\033[00m".format(skk), end=end)


DEBUG = 1


def PrintDebug(skk, end="\n"):
  if DEBUG:
    print(skk, end=end)


def Part1(winning_numbers, nums_in_hand):
  total_sum = 0
  for idx, (win, hand) in enumerate(zip(winning_numbers, nums_in_hand)):
    num_in_win = sum(el in win for el in hand)
    if num_in_win:
      score = 2**(num_in_win - 1)
      total_sum += score

  print(f"Part 1 Answer: {total_sum}")


def Part2(winning_numbers, nums_in_hand):
  assert len(winning_numbers) == len(nums_in_hand)
  num_of_card_at_index = [1 for i in winning_numbers]
  for idx, (win, hand) in enumerate(zip(winning_numbers, nums_in_hand)):
    num_in_win = sum(el in win for el in hand)
    for _ in range(num_of_card_at_index[idx]):
      for i in range(num_in_win):
        num_of_card_at_index[i + idx + 1] += 1

  print(f"Part 2 answer: {sum(num_of_card_at_index)}")


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  winning_numbers = []
  nums_in_hand = []
  for line in lines:
    win, hand = [x.strip() for x in line.split(':')[1].split('|')]
    win = [int(num) for num in win.split()]
    hand = [int(num) for num in hand.split()]
    winning_numbers.append(win)
    nums_in_hand.append(hand)

  Part1(winning_numbers, nums_in_hand)
  Part2(winning_numbers, nums_in_hand)


if __name__ == '__main__':
  main()
