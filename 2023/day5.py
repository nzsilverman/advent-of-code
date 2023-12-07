import sys
import math
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


@attrs.define
class Locations():
  soil: int
  fertilizer: int
  water: int
  light: int
  temperature: int
  humidity: int
  location: int


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


def FindDestinationNumber(maps, start):
  for mapping in maps:
    if mapping.source_start <= start < mapping.source_start + mapping.length:
      return mapping.dest_start + abs(mapping.source_start - start)

  return start


def BuildSeedToLocationsMap(seeds, almanac):
  seed_to_locations = {}
  for seed in seeds:
    PrintDebug(f"Seed {seed}")

    soil = FindDestinationNumber(almanac.seed_to_soil_maps, seed)
    PrintDebug(f"Soil: {soil}")

    fertilizer = FindDestinationNumber(almanac.soil_to_fertilizer_maps, soil)
    PrintDebug(f"fertilizer: {fertilizer}")

    water = FindDestinationNumber(almanac.fertilizer_to_water_maps, fertilizer)
    PrintDebug(f"water: {water}")

    light = FindDestinationNumber(almanac.water_to_light_maps, water)
    PrintDebug(f"light: {light}")

    temperature = FindDestinationNumber(almanac.light_to_temperature_maps,
                                        light)
    PrintDebug(f"temperature: {temperature}")

    humidity = FindDestinationNumber(almanac.temperature_to_humidity_maps,
                                     temperature)
    PrintDebug(f"humidity: {humidity}")

    location = FindDestinationNumber(almanac.humidity_to_location_maps,
                                     humidity)
    PrintDebug(f"location: {location}")

    seed_to_locations[seed] = Locations(soil=soil,
                                        fertilizer=fertilizer,
                                        water=water,
                                        light=light,
                                        temperature=temperature,
                                        humidity=humidity,
                                        location=location)

  return seed_to_locations


def FindAndPrintLowestSeed(seed_to_locations):
  lowest = None
  lowest_seed = None
  for seed in seed_to_locations.keys():
    if lowest is None or seed_to_locations[seed].location < lowest:
      lowest = seed_to_locations[seed].location
      lowest_seed = seed

  print(f"Seed {lowest_seed} has a location of {lowest}")


def Part1(lines):
  seeds_line = lines[0]
  seeds = [int(x) for x in seeds_line.split(':')[1].strip().split()]

  almanac = BuildAlmanac(lines)

  seed_to_locations = BuildSeedToLocationsMap(seeds, almanac)

  print("\nPart 1 Answer:")
  FindAndPrintLowestSeed(seed_to_locations)


def Part2(lines):
  seeds_line = lines[0]
  seeds_raw = [int(x) for x in seeds_line.split(':')[1].strip().split()]
  assert len(seeds_raw) % 2 == 0

  seeds = []
  for start, length in zip(seeds_raw[:-1:2], seeds_raw[1::2]):
    seeds.extend([x for x in range(start, start + length)])
    PrintDebug(f"start: {start}, length: {length}")

  PrintDebug(seeds)

  almanac = BuildAlmanac(lines)

  seed_to_locations = BuildSeedToLocationsMap(seeds, almanac)

  print("\nPart 2 Answer:")
  FindAndPrintLowestSeed(seed_to_locations)


def main():
  infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
  data = open(infile).read().strip()
  lines = [line for line in data.split('\n')]

  # Part1(lines)
  Part2(lines)


if __name__ == '__main__':
  main()
