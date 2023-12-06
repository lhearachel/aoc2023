import math

with open('input_06.txt', 'r') as fin:
    INPUT = fin.read().strip().splitlines()

TIMES = list(map(int, INPUT[0].split()[1:]))
RECORDS = list(map(int, INPUT[1].split()[1:]))

# Leaving my brute-force impl for part1 for illustrative purposes
part1 = 1
for i, r in enumerate(RECORDS):
    time = TIMES[i]
    opts = 0
    for t in range(1, time):
        d = t * (time - t)
        if d > r:
            opts += 1
    part1 *= opts

print(part1)

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
