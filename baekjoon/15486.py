# 15486

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,data):
    table = [0] * n

    for i in range(n-1,-1,-1):
        if i==n-1:
            if i+data[i][0]>n:
                table[i] = 0
            else:
                table[i] = data[i][1]
        else:
            if i+data[i][0]>n:
                table[i] = table[i+1]
            elif i+data[i][0]==n:
                table[i] = max(table[i+1],data[i][1])
            else:
                table[i] = max(table[i+1],table[i+data[i][0]]+data[i][1])

    return table[0]

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int,input().split())))

print(solution(n,data))