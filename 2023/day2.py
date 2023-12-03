import sys
from collections import deque
import attrs

@attrs.define
class CubesSubset:
    red: int
    green: int
    blue: int

def get_game_id_to_games(lines):
    game_id_to_games = {}
    for line in lines:
        game_id_str, games_str = line.split(':')
        game_id = int(game_id_str.split()[1])
        games_raw = [x.strip() for x in games_str.split(';')]
        games = []
        for game in games_raw:
            cube_subset = CubesSubset(red=0, green=0, blue=0)
            cubes_raw = game.split(',')
            for cube_line in cubes_raw:
                num_cubes, type_cube = cube_line.split()
                num_cubes = int(num_cubes)
                if type_cube == 'red':
                    cube_subset.red += num_cubes
                elif type_cube == 'blue':
                    cube_subset.blue += num_cubes
                elif type_cube == 'green':
                    cube_subset.green += num_cubes
            games.append(cube_subset)
        game_id_to_games[game_id] = games 

    return game_id_to_games

def part1(game_id_to_games):
    red_limit = 12
    green_limit = 13
    blue_limit = 14

    possible_game_ids_sum = 0

    for game_id in game_id_to_games.keys():
        possible = True
        for game in game_id_to_games[game_id]:
            if (game.red > red_limit or game.blue > blue_limit or game.green > green_limit):
                possible = False
        if possible:
            possible_game_ids_sum += game_id

    print(f"[Part 1] {possible_game_ids_sum}")

def part2(game_id_to_games):

    game_id_to_min = {}

    for game_id in game_id_to_games.keys():
        min_subset = CubesSubset(red=0, green=0, blue=0)

        for game in game_id_to_games[game_id]:
            if game.red > min_subset.red:
                min_subset.red = game.red 

            if game.blue > min_subset.blue:
                min_subset.blue = game.blue 

            if game.green > min_subset.green:
                min_subset.green = game.green 

        game_id_to_min[game_id] = min_subset


    sum_of_powers = 0
    for game in game_id_to_min.values():
        sum_of_powers += (game.red * game.blue * game.green)


    print(f"[Part 2]: {sum_of_powers} ")


def main():
    infile = sys.argv[1] if len(sys.argv)>1 else 'input.txt'
    data = open(infile).read().strip()
    lines = [line for line in data.split('\n')]

    game_id_to_games = get_game_id_to_games(lines)

    part1(game_id_to_games)
    part2(game_id_to_games)



if __name__ == '__main__':
    main()
