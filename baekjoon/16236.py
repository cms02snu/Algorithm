# 16236

from collections import deque
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_next_fish(graph,loc,s):
  x,y = loc
  dist = [[int(1e9)]*n for _ in range(n)]
  h = []

  queue = deque()
  queue.append((x,y))
  dist[x][y] = 0

  while queue:
    x,y = queue.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if graph[nx][ny]<=s and dist[nx][ny]>dist[x][y]+1:
          dist[nx][ny] = dist[x][y] + 1
          queue.append((nx,ny))
          if 0<graph[nx][ny]<s:
            heapq.heappush(h,(dist[nx][ny],nx,ny))

  if not h:
    return False,-1,-1,-1
  else:
    d,x,y = heapq.heappop(h)
    return True,d,x,y

def solution(n,graph):
  for i in range(n):
    for j in range(n):
      if graph[i][j]==9:
        graph[i][j] = 0
        shark_loc = (i,j)

  shark_size = 2
  eat = 0
  time = 0

  while True:
    check,t,x,y = find_next_fish(graph,shark_loc,shark_size)
    if not check:
      break

    graph[x][y] = 0
    shark_loc = (x,y)

    eat += 1
    if eat==shark_size:
      eat = 0
      shark_size += 1

    time += t

  return time

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(n,graph))