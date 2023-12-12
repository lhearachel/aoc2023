with open('input_11.txt', 'r') as fin:
    STARMAP = [list(line) for line in fin.read().strip().splitlines()]

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def find_empty(m):
    return set([i
                for i, row in enumerate(m)
                if all(c == '.' for c in row)])

EMPTY_ROWS = find_empty(STARMAP)
EMPTY_COLS = find_empty(transpose(STARMAP))
GALAXIES = [(i, j)
            for i, row in enumerate(STARMAP)
            for j, c in enumerate(row)
            if c == '#']

def delta(g, h):
    if g < h:
        return set(range(g, h))
    return set(range(h, g))

def dist(g, h, scale_x=0, scale_y=0):
    delta_y = delta(g[0], h[0])
    delta_x = delta(g[1], h[1])
    scale = [0, 0]
    for y in EMPTY_ROWS:
        scale[0] += (scale_y * int(y in delta_y))
    for x in EMPTY_COLS:
        scale[1] += (scale_x * int(x in delta_x))
    return abs(g[0] - h[0]) + scale[0] + abs(g[1] - h[1]) + scale[1] 

print(sum([dist(g, h, 1, 1)
           for i, g in enumerate(GALAXIES)
           for h in GALAXIES[i+1:]]))
print(sum([dist(g, h, 999999, 999999)
           for i, g in enumerate(GALAXIES)
           for h in GALAXIES[i+1:]]))

