# 2206

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(n,m,graph):
  dist = [[[int(1e9),int(1e9)] for _ in range(m)] for _ in range(n)]
  queue = deque()
  dist[0][0] = [1,1]
  queue.append((0,0,0))

  while queue:
    x,y,count = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if count==0:
          if graph[nx][ny]==0:
            if dist[nx][ny][0]>dist[x][y][0]+1:
              dist[nx][ny][0] = dist[x][y][0] + 1
              queue.append((nx,ny,0))
            if dist[nx][ny][1]>dist[x][y][1]+1:
              dist[nx][ny][1] = dist[x][y][1] + 1
              queue.append((nx,ny,1))
          else:
            if dist[nx][ny][1]>dist[x][y][0]+1:
              dist[nx][ny][1] = dist[x][y][0] + 1
              queue.append((nx,ny,1))
        else:
          if graph[nx][ny]==0:
            if dist[nx][ny][1]>dist[x][y][1] + 1:
              dist[nx][ny][1] = dist[x][y][1] + 1
              queue.append((nx,ny,1))

  result = min(dist[n-1][m-1])
  if result==int(1e9):
    return -1

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  a = list(input())
  b = [int(i) for i in a]
  graph.append(b)

print(solution(n,m,graph))