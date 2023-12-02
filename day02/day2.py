import enum
import re

game_id_pt = r'Game (\d+)'
cube_set_pt = r'(\d+) (blue|green|red)'

def parse_line(line) -> tuple[int, list[dict[str, int]]]:
    game_id = int(re.match(game_id_pt, line).group(1))
    line_sets = []

    list_start = line.find(':') + 2
    sets = line[list_start:].split('; ')
    for s in sets:
        cubes_qty = {}
        cubes_spl = s.split(', ')
        for c in cubes_spl:
            match = re.match(cube_set_pt, c)
            cubes_qty[match.group(2)] = int(match.group(1))
        line_sets.append(cubes_qty)

    return (game_id, line_sets)

def valid_color(entry, color, max) -> bool:
    if color in entry and entry[color] > max:
        return False
    return True

def is_valid(line_sets):
    for entry in line_sets:
        if not valid_color(entry, 'red', 12):
            return False 
        if not valid_color(entry, 'green', 13):
            return False 
        if not valid_color(entry, 'blue', 14):
            return False

    return True 

def calc_power(line_sets):
    red_max = 0
    green_max = 0
    blue_max = 0

    for entry in line_sets:
        if entry.get('red', 0) > red_max:
            red_max = entry.get('red')
        if entry.get('green', 0) > green_max:
            green_max = entry.get('green')
        if entry.get('blue', 0) > blue_max:
            blue_max = entry.get('blue')

    return red_max * green_max * blue_max

def exec(part):
    infile = open('input_02.txt', 'r')

    sum = 0
    for line in infile:
        if not line.strip():
            continue

        (game_id, line_sets) = parse_line(line)

        if part == 1 and is_valid(line_sets):
            sum = sum + game_id
        elif part == 2:
            sum = sum + calc_power(line_sets)

    print(sum)
    infile.close()

