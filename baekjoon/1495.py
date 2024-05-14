# 1495

def solution(n,s,m,data):
    table = [[False]*(m+1) for _ in range(n)]

    for i in range(n):
        for j in range(m+1):
            if i==0:
                if j==s-data[0] or j==s+data[0]:
                    table[0][j] = True
            else:
                if 0<=j-data[i]<=m:
                    if table[i-1][j-data[i]]:
                        table[i][j] = True
                if 0<=j+data[i]<=m:
                    if table[i-1][j+data[i]]:
                        table[i][j] = True

    for j in range(m,-1,-1):
        if table[n-1][j]:
            return j
        
    return -1

n,s,m = map(int,input().split())
data = list(map(int,input().split()))

print(solution(n,s,m,data))