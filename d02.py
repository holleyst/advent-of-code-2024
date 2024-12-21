#!/usr/bin/env python3

# Advent of Code 2024
# Day 2: Red-Nosed Reports
# https://adventofcode.com/2024/day/2

import re

reports = []
input_file = "d02input.txt"
with open(input_file, "r") as f:
    # each line is a report
    for line in f:
        # each number is a level
        levels = re.findall(r"(\d+)", line)
        reports.append([int(x) for x in levels])


# check report safety
def check_safety(report):
    # check if levels are strictly increasing or decreasing
    if all(x < y for x, y in zip(report, report[1:])) or all(x > y for x, y in zip(report, report[1:])):
        # check if levels differ by at least 1 and at most 3
        diffs = [abs(x - y) for x, y in zip(report[:-1], report[1:])]
        if all(x in [1, 2, 3] for x in diffs):
            # safe
            return True
    # not safe
    return False


# part 1: how many reports are safe?
safe_reports = [r for r in reports if check_safety(r)]
print("safe reports (part 1):", len(safe_reports))


# part 2: how many reports are safe after removing a single unsafe level?
unsafe_reports = [r for r in reports if not r in safe_reports]
more_safe_reports = []
for r in unsafe_reports:
    for idx in range(0, len(r)):
        test_report = r.copy()
        del test_report[idx]
        if check_safety(test_report):
            more_safe_reports.append(test_report)
            break

print("safe reports (part 2):", len(safe_reports) + len(more_safe_reports))

