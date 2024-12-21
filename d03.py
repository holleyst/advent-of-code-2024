#!/usr/bin/env python3

# Advent of Code 2024
# Day 3: Mull It Over
# https://adventofcode.com/2024/day/3

import re

input_file = "d03input.txt"
with open(input_file, "r") as f:
    data = f.read()


# part 1: sum of the multiplications

# get multiplication instructions
mul_list = re.findall(r"mul\((\d+),(\d+)\)", data)
mul_sum = 0
for pair in mul_list:
    mul_sum += int(pair[0]) * int(pair[1])

print("sum of the multiplications (part 1):", mul_sum)


# part 2: sum of the enabled multiplications

# discard disabled sections
enabled_str = re.sub(r"(?s)don\'t\(\).*?do\(\)", "", data)

# get multiplication instructions
enabled_list = re.findall(r"mul\((\d+),(\d+)\)", enabled_str)
enabled_sum = 0
for pair in enabled_list:
    enabled_sum += int(pair[0]) * int(pair[1])

print("sum of the enabled multiplications (part 2):", enabled_sum)

