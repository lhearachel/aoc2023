from collections import defaultdict

with open('input_03.txt') as fin:
    input = [list(line) for line in fin.read().strip().split('\n')]

ROWS = len(input)
COLS = len(input[0])
GEARS = defaultdict(list)

def walk_num(x, y, result, coords):
    result.append(input[x][y])
    coords[0] = coords[0] or find_syms(x, y)

    input[x][y] = '.' # don't process this node again
    y += 1
    if y < COLS and input[x][y].isdigit():
        walk_num(x, y, result, coords)

    return result, coords


def find_syms(x, y):
    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1):
        r = dx + x
        c = dy + y
        if 0 <= r < ROWS and 0 <= c < COLS and not input[r][c].isdigit() and input[r][c] != '.':
            return (r, c)


sum_p1 = 0
for x in range(ROWS):
    for y in range(COLS):
        if input[x][y].isdigit():
            result, coords = walk_num(x, y, [], [()])
            num = int(''.join(result))
            coords = coords[0]
            if coords:
                sum_p1 += num
                GEARS[coords].append(num)

sum_p2 = 0
for g in GEARS:
    c = GEARS[g]
    if len(c) == 2:
        sum_p2 += (c[0] * c[1])

print(sum_p1)
print(sum_p2)

