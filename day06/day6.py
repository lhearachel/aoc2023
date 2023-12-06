import functools
import math

with open('input_06.txt', 'r') as fin:
    INPUT = fin.read().strip().splitlines()

# Part 1: Brute Force
TIMES = list(map(int, INPUT[0].split()[1:]))
RECORDS = list(map(int, INPUT[1].split()[1:]))

def mul(p, tr):
    L, R = tr
    return p * len([t*(L-t) for t in range(1, L) if t*(L-t) > R])

print(functools.reduce(mul, zip(TIMES, RECORDS), 1))

# Part 2: Quadratic formula
#
# T -> travel time
# L -> race time limit
# B -> time pressing the button
# D -> distance traveled
#
# T = L - B
# D = T * B
# D = (L - B) * B
# D = L*B - B^2
# B^2 - L*B + D = 0
# 
# Find the zeroes of this quadratic function, then take
# the difference in those two zeroes to find the number
# of new possible records
TIME_P2 = int(''.join(map(str, TIMES)))
RECORD_P2 = int(''.join(map(str, RECORDS)))
p2_1 = int((TIME_P2 + math.sqrt(TIME_P2**2 - (4 * RECORD_P2))) / 2)
p2_2 = int((TIME_P2 - math.sqrt(TIME_P2**2 - (4 * RECORD_P2))) / 2)
print(p2_1 - p2_2)
