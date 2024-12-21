#!/usr/bin/env python3

# Advent of Code 2024
# Day 5: Print Queue
# https://adventofcode.com/2024/day/5

import re

input_file = "d05input.txt"
with open(input_file, "r") as f:
    data = f.read()

# get page ordering rules
rules = [list(map(int, line.split("|"))) for line in re.sub(r"(?s)^(.+)\n\s*\n.+$", r"\1", data).splitlines()]
# get updates
updates = [list(map(int, line.split(","))) for line in re.sub(r"(?s)^.+\n\s*\n(.+)$", r"\1", data).splitlines()]


# part 1: add up the middle page numbers from correctly-ordered updates
good_updates = []
bad_updates = []

for u in updates:
    flag = 0
    for r in rules:
        checklist = [x for x in r if x in u]
        # if both pages in ordering rule are in the update
        if len(checklist) == 2:
            # if update is not correctly ordered, flag and exit loop
            if u.index(r[0]) > u.index(r[1]):
                flag = 1
                break
    
    if flag == 0:
        good_updates.append(u)
    else:
        bad_updates.append(u)           

middle_sum = 0
for u in good_updates:
    middle_sum += u[len(u)//2]
print("sum of middle page numbers from correctly-ordered updates (part 1):", middle_sum)


# part 2: fix incorrectly-ordered updates and add up those middle page numbers
fixed_updates = []
# find correct order from position/count of each page in rules
for u in bad_updates:
    first_positions = { k: 0 for k in u }
    for r in rules:
        if all(e in u for e in r):
            first_positions[r[0]] += 1
    first_positions_sorted = dict(sorted(first_positions.items(), key=lambda item: item[1], reverse=True))
    fixed_updates.append(list(first_positions_sorted.keys()))

fixed_middle_sum = 0
for u in fixed_updates:
    fixed_middle_sum += u[len(u)//2]
print("sum of middle page numbers from fixed updates (part 2):", fixed_middle_sum)

