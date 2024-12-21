#!/usr/bin/env python3

# Advent of Code 2024
# Day 19: Linen Layout
# https://adventofcode.com/2024/day/19

import functools

input_file = "d19input.txt"

with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

# make patterns a tuple since list is not hashable, returns TypeError with cache
patterns = tuple(x.strip() for x in lines[0].split(","))
designs = lines[2:]


# count how many ways string can be formed using list of substrings
@functools.cache
def count_arrangements(string, substrings):
    count = 0
    for sub in substrings:
        sublen = len(sub)
        if string.startswith(sub):
            if sublen == len(string):
                count += 1
            else:
                count += count_arrangements(string[sublen:], substrings)
    return count


possible_designs = 0
total_arrangements = 0
for d in designs:
    tmp_count = count_arrangements(d, patterns)
    total_arrangements += tmp_count
    if tmp_count > 0:
        possible_designs += 1

print("how many designs are possible? (part 1):", possible_designs)
print("how many total arrangements? (part 2):", total_arrangements)

