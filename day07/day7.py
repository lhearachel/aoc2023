from collections import Counter

with open('input_07.txt', 'r') as fin:
    INPUT = [line for line in fin.read().strip().splitlines()]

SUB_SCORES = '23456789TJQKA'
JOK_SCORES = 'J23456789TQKA'

def jokerize(hand):
    c = Counter(hand)
    j = c.most_common()[0][0]
    if j == 'J' and hand != 'JJJJJ':
        j = c.most_common()[1][0]

    return hand.replace('J', j)

def score(hand, wild=False):
    if wild:
        tiebreaker = [JOK_SCORES.index(c) for c in hand]
        hand = jokerize(hand)
    else:
        tiebreaker = [SUB_SCORES.index(c) for c in hand]

    match sorted(Counter(hand).values()):
        case [5]:          score = 6
        case [1, 4]:       score = 5
        case [2, 3]:       score = 4
        case [1, 1, 3]:    score = 3
        case [1, 2, 2]:    score = 2
        case [1, 1, 1, 2]: score = 1
        case _:            score = 0

    return score, tiebreaker


hand_scores = sorted(INPUT, key=lambda l: score(l.split()[0], False))
wild_scores = sorted(INPUT, key=lambda l: score(l.split()[0], True))

print(sum(i * int(line.split()[1]) for i, line in enumerate(hand_scores, 1)))
print(sum(i * int(line.split()[1]) for i, line in enumerate(wild_scores, 1)))
