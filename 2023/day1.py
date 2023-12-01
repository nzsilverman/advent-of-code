import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(infile).read().strip()
lines = [line for line in data.split('\n')]


def part_1():
  calibration_sum = 0
  for line in lines:
    nums = [x for x in line if x.isnumeric()]
    assert len(nums) >= 1
    calibration_value = int(nums[0] + nums[-1])
    calibration_sum += calibration_value

  print(f"[Part 1] Calibration sum: {calibration_sum}")


def replace_spelled_out_nums(line):
  word_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
  }
  new_str = ""
  for idx, char in enumerate(line):
    found = False
    for word in word_to_num.keys():
      if line[idx:].startswith(word):
        new_str += word_to_num[word]
        found = True
        break

    if not found:
      new_str += char

  return new_str


def part_2():
  calibration_sum = 0
  for line in lines:
    replaced_line = replace_spelled_out_nums(line)
    nums = [x for x in replaced_line if x.isnumeric()]
    assert len(nums) >= 1
    calibration_value = int(nums[0] + nums[-1])
    calibration_sum += calibration_value

  print(f"[Part 2] Calibration sum: {calibration_sum}")


part_1()
part_2()
