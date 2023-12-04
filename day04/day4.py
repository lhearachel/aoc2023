import re

FORMAT = r'^Card\s+(\d+):((\s+\d+)+) \|((\s+\d+)+)'
with open('input_04.txt', 'r') as fin:
    INPUT = [line for line in fin.read().strip().split('\n')]


def winners(winning_nums, our_nums) -> list[int]:
    return [ours for ours in our_nums if ours in winning_nums]


p1 = 0
copies = [1] * len(INPUT)
for line in INPUT:
    parsed = re.match(FORMAT, line)
    card = int(parsed.group(1)) - 1
    theirs = parsed.group(2).split()
    ours = parsed.group(4).split()

    winning = winners(theirs, ours)
    if winning:
        p1 = p1 + (2 ** (len(winning) - 1))
        for i in range(len(winning)):
            copies[card + i + 1] += copies[card]


print(p1)
print(sum(copies))
