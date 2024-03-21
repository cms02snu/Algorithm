# 1520

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dp(x,y):
    count = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]<graph[x][y]:
                if (nx,ny)==(n-1,m-1):
                    count += 1
                    continue
                if table[nx][ny]==0:
                    dp(nx,ny)
                if table[nx][ny]!=-1:
                    count += table[nx][ny]

    if count==0:
        table[x][y] = -1
    else:
        table[x][y] = count        

def solution(graph):
    if (n,m)==(1,1):
        return 1
    
    global table
    table = [[0]*m for _ in range(n)]

    dp(0,0)

    if table[0][0]==-1:
        return 0

    return table[0][0]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

print(solution(graph))