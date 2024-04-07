# 2294

'''
table[i] : i원을 만드는데 필요한 최소동전개수
table[i] = min(table[i-c]) + 1
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(1e9)

def solution(k,coin):
    table = [-1] * (k+1)
    table[0] = 0

    for i in range(1,k+1):
        _min = N
        for c in coin:
            if i-c>=0:
                if table[i-c]!=-1:
                    _min = min(_min,table[i-c])
        if _min<N:
            table[i] = _min + 1

    return table[k]

n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

print(solution(k,coin))