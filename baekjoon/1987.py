# 1987

'''
bfs(i,j,visited) : (i,j)까지오는데 visited만큼 방문함
if not visited data[nx][ny] : bfs(nx,ny,visited+data[nx][ny])
visited : set or bit => bit

메모리 초과 해결해야됨 dfs + 백트래킹 적용
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

db = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

def dfs(x,y,visited,dist):
    global result
    result = max(result,dist)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if not (visited & 1<<db[graph[nx][ny]]):
                k = visited | 1<<db[graph[nx][ny]]
                dfs(nx,ny,k,dist+1)

def solution(graph):
    global result
    result = 0

    dfs(0,0,1<<db[graph[0][0]],1)

    return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

print(solution(graph))