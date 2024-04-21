# 15729

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int,input().split()))

def press(i,data):
    for x in [i,i+1,i+2]:
        if x>=0 and x<n:
            data[x] = (data[x]+1)%2

def solution(data):
    count = 0
    for i in range(n):
        if data[i]:
            press(i,data)
            count += 1

    return count

print(solution(data))