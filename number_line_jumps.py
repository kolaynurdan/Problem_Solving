#Submissions	Leaderboard	Discussions	Editorial
#You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

#The first kangaroo starts at location  and moves at a rate of  meters per jump.
#The second kangaroo starts at location  and moves at a rate of  meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

exist = False
while(True):
    if x1 == x2:
        exist = True
        break
    if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1) or (v2 == v1 and x2 != x1):
        break
    x1 += v1
    x2 += v2
    
if exist:
    print('YES')
else:
    print('NO')
