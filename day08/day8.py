import math, re

with open('input_08.txt', 'r') as fin:
    data = fin.read().strip().splitlines()
    DIRS = data[0]
    NODES = { n: (l, r) for n, l, r in (re.findall(r'[A-Z]{3}', line) for line in data[2:]) }

def steps(fr, to):
    result = 0
    dir = DIRS[0]
    while not re.match(to, fr):
        fork = NODES[fr]
        fr = fork[0] if dir == 'L' else fork[1]
        result = result + 1
        dir = DIRS[result % len(DIRS)]

    return result 

print(steps('AAA', r'ZZZ'))

start_nodes = [n for n in NODES if n[-1] == 'A']
ghost_steps = [steps(n, r'..Z') for n in start_nodes]
print(math.lcm(*ghost_steps))
