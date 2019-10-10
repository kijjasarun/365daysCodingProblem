#!/usr/bin/python3
# Day 010/365
# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# My idea : Kijjasarun 20191004
# My understand is delay n time and call function
import time


def fJob():
    print("Hello!.")


def fScheduler(f, n):
    mn = n / 1000  # milliSec to seconds
    time.sleep(mn)
    f()


fScheduler(fJob, 10000)  # 10sec
