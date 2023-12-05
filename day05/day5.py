from functools import reduce

with open('input_05.txt', 'r') as fin:
    INPUT = [line for line in fin.read().strip().split('\n\n') if line]


# mappings are sequential, handy
MAPPINGS = []
for mapping in INPUT[1:]:
    cur = []
    for line in mapping.split('\n')[1:]:
        dst_st, src_st, rg_len = tuple(map(int, line.split()))
        cur.append([src_st, src_st + rg_len - 1, dst_st - src_st])

    # each mapping should be sorted for range-processing
    MAPPINGS.append(sorted(cur))


def lookup(key, mapping):
    for src_st, src_ed, delta in mapping:
        if key > src_ed:
            continue
        elif key < src_st:
            return key
        else:
            return key + delta
    return key


def lookup_range(start, end, mapping):
    result = []
    for src_st, src_ed, delta in mapping:
        # input range exists wholly outside mapping range 
        if start > src_ed or end < src_st:
            continue

        if start < src_st:
            # input range overlaps; end could be inside
            # the mapping range or outside (> src_ed)
            # need to track both possible overlap points
            result.extend([
                (start,          src_st - 1),
                (src_st + delta, min(src_ed, end) + delta)
            ])
        else:
            # input range starts within mapping range; end
            # may be outside the mapping range
            result.append((start + delta, min(src_ed, end) + delta))
        
        if src_ed > end:
            # input range is a true subset of the mapping range
            return result
        start = src_ed # update to the next cursor position

    return result or [(start, end)]


def pairs(seeds):
    # manual reduce, basically
    rg = [(seeds[0], seeds[0] + seeds[1])]
    for mapping in MAPPINGS:
        result = []
        for start, end in rg:
            result.extend(lookup_range(start, end, mapping))
        rg = result
    return min(result)[0]


seeds = list(map(int, INPUT[0][7:].split()))
print(min(reduce(lookup, MAPPINGS, s) for s in seeds))
print(min([pairs(seeds[i:i+2]) for i in range(0, len(seeds), 2)]))

