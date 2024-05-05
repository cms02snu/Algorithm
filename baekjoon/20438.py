# 20438

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(sleep,first):
    first.sort()
    attendance = [False] * (n+3)
    for x in first:
        if sleep[x]:
            continue
        if attendance[x]:
            continue
        k = x
        while True:
            if x>=n+3:
                break
            if sleep[x]:
                x += k
                continue
            attendance[x] = True
            x += k

    return attendance

n,k,q,m = map(int,input().split())
sleep = [False] * (n+3)
for i in map(int,input().split()):
    sleep[i] = True
first = list(map(int,input().split()))

attendance = solution(sleep,first)
temp = [0] * (n+1)
for i in range(1,n+1):
    if i==1:
        if not attendance[3]:
            temp[1] = 1
    else:
        if not attendance[i+2]:
            temp[i] = temp[i-1] + 1
        else:
            temp[i] = temp[i-1]

for _ in range(m):
    s,e = map(int,input().split())
    print(temp[e-2] - temp[s-3])