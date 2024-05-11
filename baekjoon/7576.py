# 7576

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(data):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                queue.append((i,j,0))

    _max = 0

    while queue:
        x,y,t = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if data[nx][ny]==0:
                    data[nx][ny] = 1
                    _max = max(_max,t+1)
                    queue.append((nx,ny,t+1))

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                return -1
            
    return _max

m,n = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

print(solution(data))