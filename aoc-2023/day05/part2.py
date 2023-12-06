from fileinput import input
import itertools
import functools

lines = input()

seed_ranges = list(int(x) for x in next(lines).split(':')[1].split(' ') if x!= '')
seed_ranges = zip(seed_ranges[::2], seed_ranges[1::2])

def seeds():
    for first_seed, num_seeds in seed_ranges:
        yield from range(first_seed, first_seed + num_seeds)

next(lines) # skip the empty line after seeds

def parse_maps(lines):
    """
    Generates a sequence of maps
    """
    ranges = []
    for line in lines:
        if line == '\n':
            yield ranges.copy()
            ranges.clear() 
        if line[0].isnumeric():
            ranges.append(tuple(int(x) for x in line.split(' ')))

maps = list(parse_maps(lines))

def apply_map(x, map):
    for dest, src, width in map:
        if src <= x < src+width:
            return dest + (x - src)
    return x 

def location(seed):
    for map in maps:
        seed = apply_map(seed, map)
    return seed 

print(min(location(seed) for seed in seeds()))