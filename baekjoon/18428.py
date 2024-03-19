# 18428

import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def avoid():
  result = True
  for i,j in students:
    if not result:
      break
    for d in range(4):
      if not result:
        break
      x,y = i,j
      while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<n:
          if temp[nx][ny]=='X':
            x,y = nx,ny
          elif temp[nx][ny]=='O' or temp[nx][ny]=='S':
            break
          else:
            result = False
            break
        else:
          break

  return result

def dfs(count):
  global result
  if count==3:
    if avoid():
      result = True

  else:
    for i in range(n):
      for j in range(n):
        if temp[i][j]=='X':
          temp[i][j] = 'O'
          dfs(count+1)
          temp[i][j] = 'X'

def solution(n,graph):
  global result
  global students
  global temp

  result = False
  students = []
  for i in range(n):
    for j in range(n):
      if graph[i][j]=='S':
        students.append((i,j))

  temp = copy.deepcopy(graph)

  dfs(0)

  if not result:
    return 'NO'
  else:
    return 'YES'

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(input().split()))

print(solution(n,graph))