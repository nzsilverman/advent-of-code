import sys
from collections import deque
from enum import Enum
import heapq


def PrintRed(skk, end="\n"):
  PrintDebug("\033[91m{}\033[00m".format(skk), end=end)


def PrintGreen(skk, end="\n"):
  PrintDebug("\033[92m{}\033[00m".format(skk), end=end)


def PrintYellow(skk, end="\n"):
  PrintDebug("\033[93m{}\033[00m".format(skk), end=end)


def PrintLightPurple(skk, end="\n"):
  PrintDebug("\033[94m{}\033[00m".format(skk), end=end)


DEBUG = 0


def PrintDebug(skk, end="\n"):
  if DEBUG:
    print(skk, end=end)


class HandType(Enum):
  five_of_kind = 7 << 30
  four_of_kind = 6 << 30
  full_house = 5 << 30
  three_of_kind = 4 << 30
  two_pair = 3 << 30
  one_pair = 2 << 30
  high_card = 1 << 30


def NumDistinctCharacters(hand):
  return len(set([x for x in hand]))


def CalculateTypeNoJokers(hand):
  num_distinct = NumDistinctCharacters(hand)
  if num_distinct == 1:
    return HandType.five_of_kind
  elif num_distinct == 2:
    # Can be four of a kind or full house
    counts = []
    for char in hand:
      counts.append(hand.count(char))

    highest_count = max(counts)

    if highest_count == 4:
      return HandType.four_of_kind
    else:
      return HandType.full_house
  elif num_distinct == 3:
    # Can be three of a kind, two pair
    counts = []
    for char in hand:
      counts.append(hand.count(char))

    highest_count = max(counts)
    if highest_count == 3:
      return HandType.three_of_kind
    else:
      return HandType.two_pair
  elif num_distinct == 4:
    return HandType.one_pair
  elif num_distinct == 5:
    return HandType.high_card


def CalculateTypeWithJokers(hand):
  if 'J' in hand:
    highest_type = None
    for char in ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
      test_hand = hand.replace('J', char)
      test_type = CalculateTypeNoJokers(test_hand)
      if highest_type is None or test_type.value > highest_type.value:
        highest_type = test_type

    return highest_type
  else:
    return CalculateTypeNoJokers(hand)


def TestCalculateHandType():
  assert CalculateTypeNoJokers("AAAAA") == HandType.five_of_kind
  assert CalculateTypeNoJokers("AA8AA") == HandType.four_of_kind
  assert CalculateTypeNoJokers("23332") == HandType.full_house
  assert CalculateTypeNoJokers("TTT98") == HandType.three_of_kind
  assert CalculateTypeNoJokers("23432") == HandType.two_pair
  assert CalculateTypeNoJokers("A23A4") == HandType.one_pair
  assert CalculateTypeNoJokers("23456") == HandType.high_card
  assert CalculateTypeNoJokers("5TTTT") == HandType.four_of_kind


def CalculateHandValue(hand, hand_char_to_hex_char, jokers=False):
  if jokers:
    hand_type_value = CalculateTypeWithJokers(hand).value
  else:
    hand_type_value = CalculateTypeNoJokers(hand).value

  hex_str = ""
  for char in hand:
    hex_str += hand_char_to_hex_char[char]
  hex_value = int(hex_str, 16)
  return hand_type_value + hex_value


def TestCalculateHandValue():
  hand_char_to_hex_char_no_jokers = {
    "T": "A",
    "J": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
  }
  assert CalculateHandValue(
    "33332", hand_char_to_hex_char_no_jokers) > CalculateHandValue(
      "2AAAA", hand_char_to_hex_char_no_jokers)
  assert CalculateHandValue(
    "77888", hand_char_to_hex_char_no_jokers) > CalculateHandValue(
      "77788", hand_char_to_hex_char_no_jokers)
  assert CalculateHandValue(
    "22222", hand_char_to_hex_char_no_jokers) > CalculateHandValue(
      "AAAA2", hand_char_to_hex_char_no_jokers)


def Part1(lines):
  hand_char_to_hex_char = {
    "T": "A",
    "J": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
  }
  pq = []
  for line in lines:
    hand, bid = line.split()
    hand_value = CalculateHandValue(hand, hand_char_to_hex_char)
    pq.append((hand_value, (hand, int(bid))))

  heapq.heapify(pq)

  rank = 1
  total_winnings = 0
  while len(pq):
    item = heapq.heappop(pq)
    PrintDebug(f"Item: {item}, Rank: {rank}")
    total_winnings += rank * item[1][1]
    rank += 1

  print(f"[Part 1] Total winnings: {total_winnings}")


def Part2(lines):
  hand_char_to_hex_char = {
    "T": "A",
    "J": "1",
    "Q": "C",
    "K": "D",
    "A": "E",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
  }
  pq = []
  for line in lines:
    hand, bid = line.split()
    hand_value = CalculateHandValue(hand, hand_char_to_hex_char, jokers=True)
    pq.append((hand_value, (hand, int(bid))))

  heapq.heapify(pq)

  rank = 1
  total_winnings = 0
  while len(pq):
    item = heapq.heappop(pq)
    PrintDebug(f"Item: {item}, Rank: {rank}")
    total_winnings += rank * item[1][1]
    rank += 1

  print(f"[Part 2] Total winnings: {total_winnings}")


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  TestCalculateHandType()
  TestCalculateHandValue()

  Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
