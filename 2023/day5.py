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
class Map():
  dest_start: int = 0
  source_start: int = 0
  length: int = 0


@attrs.define
class Almanac():
  seed_to_soil_maps: list = []
  soil_to_fertilizer_maps: list = []
  fertilizer_to_water_maps: list = []
  water_to_light_maps: list = []
  light_to_temperature_maps: list = []
  temperature_to_humidity_maps: list = []
  humidity_to_location_maps: list = []


def BuildAlmanac(lines):
  chunks = [idx for idx, line in enumerate(lines) if line == ""]

  assert len(chunks) == 7
  almanac = Almanac()

  # offset is 2 for the whitespace and title for each section
  offset = 2
  maps = [
    almanac.seed_to_soil_maps, almanac.soil_to_fertilizer_maps,
    almanac.fertilizer_to_water_maps, almanac.water_to_light_maps,
    almanac.light_to_temperature_maps, almanac.temperature_to_humidity_maps,
    almanac.humidity_to_location_maps
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
      mapping = Map()
      mapping.dest_start = dest_start
      mapping.source_start = source_start
      mapping.length = length
      maps[idx].append(mapping)

  return almanac


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  seeds_line = lines[0]
  seeds = [int(x) for x in seeds_line.split(':')[1].strip().split()]

  PrintDebug(f"Seeds: {seeds}")

  almanac = BuildAlmanac(lines)

  PrintDebug(f"Seed to soil map")
  for mapping in almanac.seed_to_soil_maps:
    PrintDebug(
      f"{mapping.source_start} -> {mapping.dest_start} over range {mapping.length}"
    )


if __name__ == '__main__':
  main()
