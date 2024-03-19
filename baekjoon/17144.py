# 17144

import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread(graph):
  temp = [[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      temp[i][j] = graph[i][j]

  for x in range(n):
    for y in range(m):
      if graph[x][y]>0:
        for d in range(4):
          nx = x + dx[d]
          ny = y + dy[d]
          if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]!=-1:
              temp[nx][ny] += graph[x][y]//5
              temp[x][y] -= graph[x][y]//5

  return temp

def fresh(graph,fresh_loc):
  x,y = fresh_loc[0]
  d = 0
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx>=0 and nx<fresh_loc[0][0]+1 and ny>=0 and ny<m:
      if graph[nx][ny]==-1:
        break
      if graph[x][y]==-1:
        graph[nx][ny] = 0
      else:
        graph[x][y] = graph[nx][ny]
        graph[nx][ny] = 0
      x,y = nx,ny
    else:
      d = (d+1)%4

  x,y = fresh_loc[1]
  d = 2
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx>=fresh_loc[1][0] and nx<n and ny>=0 and ny<m:
      if graph[nx][ny]==-1:
        break
      if graph[x][y]==-1:
        graph[nx][ny] = 0
      else:
        graph[x][y] = graph[nx][ny]
        graph[nx][ny] = 0
      x,y = nx,ny
    else:
      d = (d-1)%4

  return graph

def solution(t,_graph):
  graph = copy.deepcopy(_graph)

  fresh_loc = []
  for i in range(n):
    for j in range(m):
      if graph[i][j]==-1:
        fresh_loc.append((i,j))

  time = 0
  while time<t:
    graph = spread(graph)
    graph = fresh(graph,fresh_loc)
    time += 1

  result = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j]>0:
        result += graph[i][j]

  return result

n,m,t = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(t,graph))