# 2502

'''
2 26 28 54 82 136 218

a b a-b 2b-a 2a-3b 5b-3a 5a-8b 13b-8a
(1,0) (0,1) (1,-1) (-1,2) (2,-3) (-3,5) (5,-8)

3a/5<b<2a/3 
'''

import math

def coef():
    result = []
    result.append((1,0))
    result.append((0,1))
    _sum = 0
    curr = 1
    for i in range(28):
        result.append((curr,_sum-curr))
        _sum,curr = curr,_sum-curr

    return result

def solution(d,k):
    C = coef()

    if d%2==0:
        y = k*C[d-1][0]*(-1)/C[d-1][1]
        if y==int(y):
            x = int(y+1)
        else:
            x = math.ceil(y)
    else:
        y = k*C[d-1][0]*(-1)/C[d-1][1]
        if y==int(y):
            x = int(y-1)
        else:
            x = math.floor(y)

    result = []
    for i in range(d):
        if i==0:
            result.append(k)
        elif i==1:
            result.append(x)
        else:
            result.append(result[i-2]-result[i-1])

    print(result[-1])
    print(result[-2])

d,k = map(int,input().split())
solution(d,k)