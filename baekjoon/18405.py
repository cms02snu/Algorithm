# 18405

from collections import deque
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(n,k,graph,time,test_loc):
  viruses = []
  for i in range(n):
    for j in range(n):
      if graph[i][j]>0:
        viruses.append((graph[i][j],i,j))
  viruses.sort()

  queue = deque()
  for i,x,y in viruses:
    queue.append((0,i,x,y))

  temp = copy.deepcopy(graph)

  while queue:
    t,i,x,y = queue.popleft()
    if t>=time:
      break
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if temp[nx][ny]==0:
          temp[nx][ny] = i
          queue.append((t+1,i,nx,ny))

  return temp[test_loc[0]][test_loc[1]]

n,k = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
t,x,y = map(int,input().split())

print(solution(n,k,graph,t,(x-1,y-1)))