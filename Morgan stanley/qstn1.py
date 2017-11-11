#!/bin/python3

import sys

def maximizeProfit(a, b, m, k):
    res = []
    for unit, cur in zip(b,a):
        res.append(m * unit * cur)
    mx = max(res)
    dlr_cr = m*k
    if dlr_cr > mx:
        return dlr_cr
    else:
        return mx


if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = maximizeProfit(a, b, m, k)
    print(result)