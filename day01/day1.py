import re

def first_and_last(line):
    first = -1
    last = 0
    for c in line:
        if c.isnumeric():
            if first < 0:
                first = int(c)
            last = int(c)

    return (first * 10) + last

def exec(part):
    infile = open('input_01.txt', 'r')

    sum = 0
    for line in infile:
        if not line.strip():
            continue

        if part == 2:
            line = line.replace('one', 'one1one') \
                       .replace('two', 'two2two') \
                       .replace('three', 'three3three') \
                       .replace('four', 'four4four') \
                       .replace('five', 'five5five') \
                       .replace('six', 'six6six') \
                       .replace('seven', 'seven7seven') \
                       .replace('eight', 'eight8eight') \
                       .replace('nine', 'nine9nine')

        sum = sum + first_and_last(line)

    print(sum)
    infile.close()

