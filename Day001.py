#!/usr/bin/python3
# Day 001/365
# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

# My idea: Kijjasarun 20191003
# a+b = c
# case i0 => i1, i0 => i2, i0 => i3
# case i1 => i2, i1 => i3
# case i2 => i3

l1 = [10, 15, 3, 7]
X1 = len(l1)

for i in l1:
    X1 -= len(l1) - 1
    X2 = len(l1)

    if X1 != 4:
        # print("X1: ", X1)
        while X2 > X1:
            if l1[X1 - 1] + l1[X2 - 1] == 17:
                print(l1[X1 - 1], "+", l1[X2 - 1], "= 17")
            X2 -= 1
    X1 += len(l1)
