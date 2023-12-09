from itertools import groupby, tee

with open('input_09.txt', 'r') as fin:
    INPUT = [list(map(int, line.split())) for line in fin.read().strip().splitlines()]

def pairwise(it):
    a, b = tee(it)
    next(b, None)
    return zip(a, b)

def all_equal(it):
    g = groupby(it)
    return next(g, True) and not next(g, False)

def make_tree(it):
    tree = [it]
    n = it
    while not all_equal(n):
        n = list(map(lambda x: x[1] - x[0], pairwise(n)))
        tree.append(n)
    tree.append([0] * (len(n) - 1))
    return tree 

def extrapolate_r(tree):
    tree[-1].append(0)
    for i in range(len(tree) - 1, 0, -1):
        child = tree[i]
        parent = tree[i - 1]
        parent.append(parent[-1] + child[-1])
    return tree[0][-1]

def extrapolate_l(tree):
    tree[-1].insert(0, 0)
    for i in range(len(tree) - 1, 0, -1):
        child = tree[i]
        parent = tree[i - 1]
        parent.insert(0, parent[0] - child[0])
    return tree[0][0]

print(sum([extrapolate_r(make_tree(line)) for line in INPUT]))
print(sum([extrapolate_l(make_tree(line)) for line in INPUT]))

