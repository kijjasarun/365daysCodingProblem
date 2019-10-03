#!/usr/bin/python3
# Day 002/365
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# My idea: Kijjasarun 20191003
# len list for loop
# loop 1[1, 2, 3, 4, 5] is new [2*3*4*5,w,x,y,z]
# loop 2[1, 2, 3, 4, 5] is new [x,1*3*4*5,x,y,z]
# end loop 5

l1 = [1, 2, 3, 4, 5]
#l1 = [3, 2, 1]
l2 =[]
y = 1
for i in l1:
    x = 1
    s = 1
    for z in l1:
        if y != x:
            s *= x
        x += 1
    y += 1
    l2.append(s)

print(l2)
