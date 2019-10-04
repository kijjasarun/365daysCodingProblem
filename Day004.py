#!/usr/bin/python3
# Day 004/365
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time
# and constant space. In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#You can modify the input array in-place.

# My idea : Kijjasarun 20191004
# Sorting array and compare integers then stop to find it.

#l1 = [3, 4, -1, 1]
l1 = [1, 2, 0]
l1.sort()
l2 = []
print(l1)
for x in range(len(l1)):
    if x != len(l1)-1:
        s = l1[x] - l1[x+1]
        if s < -1:
            sm = l1[x] +1
            if sm > 0:
                print(sm)
                break
    else:
        sm = l1[x] +1
        print(sm)
