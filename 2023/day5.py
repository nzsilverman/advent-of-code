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
  seed_to_soil_map: dict = {}
  soil_to_fertilizer_map: dict = {}
  fertilizer_to_water_map: dict = {}
  water_to_light_map: dict = {}
  light_to_temperature_map: dict = {}
  temperature_to_humidity_map: dict = {}
  humidity_to_location_map: dict = {}


def BuildAlmanac(lines):
  chunks = [idx for idx, line in enumerate(lines) if line == ""]

  assert len(chunks) == 7
  almanac = Almanac()

  # offset is 2 for the whitespace and title for each section
  offset = 2
  maps = [
    almanac.seed_to_soil_map, almanac.soil_to_fertilizer_map,
    almanac.fertilizer_to_water_map, almanac.water_to_light_map,
    almanac.light_to_temperature_map, almanac.temperature_to_humidity_map,
    almanac.humidity_to_location_map
  ]

  assert len(maps) == len(chunks)

  map_lines = []
  for idx in range(len(chunks)):

    if idx == len(chunks) - 1:
      # Last item, must read to the end
      map_lines = lines[chunks[idx] + offset:]
    else:
      # Read a chunk
      map_lines = lines[chunks[idx] + offset:chunks[idx + 1]]

    for line in map_lines:
      dest_start, source_start, length = [int(x) for x in line.strip().split()]
      for i in range(length):
        dest = dest_start + i
        source = source_start + i
        maps[idx][source] = dest

  return almanac


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  seeds_line = lines[0]
  seeds = [int(x) for x in seeds_line.split(':')[1].strip().split()]

  PrintDebug(f"Seeds: {seeds}")

  almanac = BuildAlmanac(lines)

  for source in almanac.seed_to_soil_map.keys():
    PrintDebug(f"{source} -> {almanac.seed_to_soil_map[source]}")


if __name__ == '__main__':
  main()
