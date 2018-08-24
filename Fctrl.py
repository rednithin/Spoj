#!/usr/bin/python3
# http://www.spoj.com/problems/FCTRL/
import math

def calcFives(num):
    fives = 0
    divisor = 5
    while True:
        ans = math.floor(num / divisor)
        if ans == 0:
            break
        fives += ans
        divisor *= 5
    return fives

n = int(input())

while n != 0:
    num = int(input())
    fives = calcFives(num)
    print(fives)
    n -= 1