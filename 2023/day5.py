import sys
from collections import deque

import attrs


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


@attrs.define
class Almanac():
  seed_to_soil_map: dict
  soil_to_fertilizer_map: dict
  fertilizer_to_water_map: dict
  water_to_light_map: dict
  light_to_temperature_map: dict
  temperature_to_humidity_map: dict
  humidity_to_location_map: dict


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  seeds_line = lines[0]
  seeds = [int(x) for x in seeds_line.split(':')[1].strip().split()]

  PrintDebug(f"Seeds: {seeds}")

  chunks = [idx for idx, line in enumerate(lines) if line == ""]
  PrintDebug(f"Chunks: {chunks}")

  assert len(chunks) == 7

  # offset is 2 for the whitespace and title for each section
  offset = 2
  for line in lines[chunks[1] + 2:chunks[2]]:
    # seed_to_soil
    PrintDebug(line)


if __name__ == '__main__':
  main()
