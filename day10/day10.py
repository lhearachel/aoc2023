with open('input_10.txt', 'r') as fin:
    MAP = [line.strip() for line in fin.read().strip().splitlines()]

PIPES = {
    '|': ['n', 's'],
    '-': ['e', 'w'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['s', 'e'],
    'S': ['n', 's', 'e', 'w'],
}

DIRS = {
    'n': (-1,  0, 's'),
    's': ( 1,  0, 'n'),
    'e': ( 0,  1, 'w'),
    'w': ( 0, -1, 'e'),
}

for i in range(len(MAP)):
    for j in range(len(MAP[i])):
        if MAP[i][j] == 'S':
            START = (i, j)

# Part 1 is just BFS, keeping track of distances to visit each node.
visited = dict()
search = [(START, 0)]
while len(search) > 0:
    cur, dist = search.pop(0)
    if cur in visited: continue
    visited[cur] = dist
    i, j = cur
    paths = PIPES[MAP[i][j]]
    for path in paths:
        di, dj, opp = DIRS[path]
        next = (i + di, j + dj)
        
        if i + di < 0 or i + di >= len(MAP):         continue
        if j + dj < 0 or j + dj >= len(MAP[i + di]): continue

        next_pipe = MAP[i + di][j + dj]
        if next_pipe not in PIPES: continue

        next_paths = PIPES[next_pipe]
        if opp in next_paths:
            search.append((next, dist + 1))

print(max(visited.values()))

# Part 2 has a trick: count the number of times you pass through a
# vertical bar to get to each tile. If that number is odd, then it's
# an interior tile.
# My S tile is a horizontal pipe so I don't count it.
in_out = [['.'] * len(MAP[0]) for _ in range(len(MAP))]
for i in range(len(MAP)):
    outside = True 
    for j in range(len(MAP[i])):
        cur = MAP[i][j]
        if (i, j) in visited:
            paths = PIPES[cur]
            if 'n' in paths and cur != 'S': # excluding S in my input
                outside = not outside 
            continue

        in_out[i][j] = 'o' if outside else 'i'

print('\n'.join([''.join(line) for line in in_out]).count('i'))

