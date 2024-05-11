# 12852

'''
dp[i] : i 연산횟수 최솟값
dp[i] = min(dp[i//3],dp[i//2],dp[i-1]) + 1
'''

import sys
sys.setrecursionlimit(int(1e6))

def dp(i):
    if i==1:
        return 0,['1']
    
    if i in db:
        return db[i]
    
    _min = int(1e9)
    minval = -1
    curr = -1

    if i%3==0:
        k,temp = dp(i//3)
        if k<_min:
            _min = k
            minval = i//3
            curr = temp
    if i%2==0:
        k,temp = dp(i//2)
        if k<_min:
            _min = k
            minval = i//2
            curr = temp
    k,temp = dp(i-1)
    if k<_min:
        _min = k
        minval = i//2
        curr = temp

    db[i] = (_min+1,curr+[str(i)])

    return db[i]

db = {}

a,b = dp(int(input()))

print(a)
print(' '.join(b[::-1]))

