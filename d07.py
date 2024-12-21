#!/usr/bin/env python3

# Advent of Code 2024
# Day 7: Bridge Repair 
# https://adventofcode.com/2024/day/7

import itertools

input_file = "d07input.txt"
with open(input_file, "r") as f:
    data = f.read().strip()


# part 1: total calibration result
#   - sum of the test values from just the equations that could possibly be true, using addition or multiplication

total_calibration = 0

for line in data.split("\n"):
    test_str, num_str = line.split(":")
    test_val = int(test_str)
    operands = list(map(int, num_str.split()))
    
    for operators in itertools.product("*+", repeat=len(operands)-1):
        eq_sum = operands[0]
        for operator, operand in zip(operators, operands[1:]):
            if operator == "+":
                eq_sum += operand
            else:
                eq_sum *= operand
            if eq_sum > test_val:
                break
        if eq_sum == test_val:
            total_calibration += eq_sum
            break

print("total calibration result (part 1):", total_calibration)


# part 2: total calibration result after allowing concatentation operator
#   - takes ~30s to process, probably could improve this

total_calibration = 0
   
for line in data.split("\n"):
    test_str, num_str = line.split(":")
    test_val = int(test_str)
    operands = list(map(int, num_str.split()))
    
    for operators in itertools.product("*+|", repeat=len(operands)-1):
        eq_sum = operands[0]
        for operator, operand in zip(operators, operands[1:]):
            if operator == "+":
                eq_sum += operand
            elif operator == "*":
                eq_sum *= operand
            else:
                eq_sum = int(str(eq_sum) + str(operand))
            if eq_sum > test_val:
                break
        if eq_sum == test_val:
            total_calibration += eq_sum
            break

print("total calibration result (part 2):", total_calibration)

