#!/bin/python3

import sys
from itertools import permutations as tp

def expectedAmount(a):
    count = 0
    sum = 0
    for rlist in tp(a, len(a)):
        count += 1
        pt = rlist[0]
        if len(rlist) == 1:
            sum += pt
            print("\n{}".format(pt))
            return

        elif len(rlist) == 2:
            sum += rlist[1]

        else:



    print("{}/{}".format(sum,count))



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        expectedAmount(a)

