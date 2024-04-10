# 10942

'''
dp[i][j] : j부터 i까지 펠린드롬 여부(j<i)
dp[i][j] = if data[i]==data[j] : dp[i-1][j+1]
           else : False

-
--
---
----
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def db(data):
    database = [[0]*(i+1) for i in range(n)]

    for d in range(n):
        if d==0:
            for j in range(n):
                database[j][j] = 1
        elif d==1:
            for j in range(n-1):
                if data[j]==data[j+1]:
                    database[j+1][j] = 1
        else:
            for j in range(n-d):
                if data[j]==data[j+d]:
                    database[j+d][j] = database[j+d-1][j+1]

    return database

n = int(input())
data = list(map(int,input().split()))
database = db(data)

for _ in range(int(input())):
    s,e = map(int,input().split())
    print(database[e-1][s-1])