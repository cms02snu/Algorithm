'''
LIS
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def lis(dataset):
    table = [0] * n
    table[0] = 1

    for i in range(1,n):
        _max = 0
        for j in range(i):
            if dataset[j]<dataset[i]:
                _max = max(_max,table[j])
        table[i] = _max+1

    return max(table)

def solution(n,data):
    data.sort()

    temp = [b for (a,b) in data]

    return n - lis(temp)

n = int(input())
data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

print(solution(n,data))