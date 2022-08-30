#Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

#countApplesAndOranges has the following parameter(s):

#s: integer, starting point of Sam's house location.
#t: integer, ending location of Sam's house location.
#a: integer, location of the Apple tree.
#b: integer, location of the Orange tree.
#apples: integer array, distances at which each apple falls from the tree.
#oranges: integer array, distances at which each orange falls from the tree.
import math
import os
import random
import re
import sys
# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_Apples = 0
    count_Oranges= 0
    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            count_Apples +=1
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            count_Oranges +=1
    print(count_Apples)
    print(count_Oranges)
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
