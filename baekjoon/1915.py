# 1915

'''
dp(i,j) : (i,j)를 오른쪽아래로 하는 정사각형의 최대길이
dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1 (if 1 else 0)
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    table = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i==0 or j==0:
                if data[i][j]=='1':
                    table[i][j] = 1
                else:
                    table[i][j] = 0
            else:
                if data[i][j]=='1':
                    table[i][j] = min(table[i-1][j-1],table[i-1][j],table[i][j-1]) + 1
                else:
                    table[i][j] = 0

    k = max([max(row) for row in table])        

    return k*k

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(input()))

print(solution(data))