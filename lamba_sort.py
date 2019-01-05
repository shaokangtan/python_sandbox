#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    k = int(input().strip())

arr.sort(key= lambda x: x[k])

for i in arr:
    for j in i:
        print ("{} ".format(j), end="")
    print()