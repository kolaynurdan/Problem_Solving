#!/bin/python3

import sys


n = int(input().strip())
squares = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
# your code goes here

count = 0
for i in range(m, n+1):
#    print(i-m, i, squares[i-m:i], d)
    if sum(squares[i-m:i]) == d:
        count += 1
        
print(count)       
