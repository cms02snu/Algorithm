# 1946

import sys

input = lambda:sys.stdin.readline().rstrip()

def solution(data):
    data.sort()
    count = 0
    prev = int(1e6)
    for _,i in data:
        if i<prev:
            prev = i
            count += 1

    return count        

for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        a,b = map(int,input().split())
        data.append((a,b))
    print(solution(data))