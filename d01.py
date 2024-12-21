#!/usr/bin/env python3

# Advent of Code 2024
# Day 1: Historian Hysteria
# https://adventofcode.com/2024/day/1

import re

list1 = []
list2 = []
distances = []

# read input file
input_file = "d01input.txt"
with open(input_file, "r") as f:
    # add numbers to lists
    for line in f:
        nums = re.findall(r"(\d+)", line)
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))


# part 1: get total distance
for n1, n2 in zip(sorted(list1), sorted(list2)):
    distances.append(abs(n1 - n2))

total_distance = sum(distances)
print("total distance (part 1):", total_distance)


# part 2: get similarity score
similarity_score = 0
for num in list1:
    # how many times is num in right list?
    freq = list2.count(num)
    similarity_score += freq * num

print("similarity score (part 2):", similarity_score)

