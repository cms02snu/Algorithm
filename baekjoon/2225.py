# 2225

'''
table[x][i] : 동전 i개를 써서 x원을 만드는 경우의 수
table[x][i] = sum(table[x-c][i-1])
갱신순서 : dm 
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,k):
    table = [[0]*(k+1) for _ in range(n+1)]

    for x in range(n+1):
        for i in range(k+1):
            if i==0:
                table[x][i] = 0
            elif x==0 or i==1:
                table[x][i] = 1
            else:
                for c in range(x+1):
                    table[x][i] += table[x-c][i-1]
    
    return table[n][k] % int(1e9)

n,k = map(int,input().split())
print(solution(n,k))