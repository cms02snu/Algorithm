# 19237

from collections import deque
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def shark_move(i,x,y,d):
  for dir in next_dir[i][d]:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if smell[nx][ny]==-1:
        return nx,ny,dir

  for dir in next_dir[i][d]:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if smell[nx][ny][0]==i:
        return nx,ny,dir

def solution(n,m,k,graph,dir,next_dir):
  global smell

  shark_loc = [-1] * m
  temp = [[[] for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if graph[i][j]>0:
        shark_loc[graph[i][j]-1] = (i,j)
        temp[i][j].append(graph[i][j]-1)

  smell = [[-1]*n for _ in range(n)]
  for i,(x,y) in enumerate(shark_loc):
    smell[x][y] = [i,k]

  curr_dir = copy.copy(dir)

  time = 0

  while time<1000:
    # 시간 증가
    time += 1

    # 상어 이동
    for i,a in enumerate(shark_loc):
      if a!=-1:
        x,y = a
        nx,ny,nd = shark_move(i,x,y,curr_dir[i])
        temp[nx][ny].append(i)
        temp[x][y].remove(i)
        shark_loc[i] = (nx,ny)
        curr_dir[i] = nd

    # 겹치면 경쟁
    for i in range(n):
      for j in range(n):
        if len(temp[i][j])>1:
          strong = min(temp[i][j])
          out = [a for a in temp[i][j] if a!=strong]
          temp[i][j] = [strong]
          for a in out:
            shark_loc[a] = -1
            curr_dir[a] = -1

    # 1번 상어만 남았다면 종료
    if shark_loc[1:]==[-1]*(m-1):
      return time

    # 냄새 시간 감소
    for i in range(n):
      for j in range(n):
        if smell[i][j]!=-1:
          smell[i][j][1] -= 1
          if smell[i][j][1]==0:
            smell[i][j] = -1

    # 이동한 자리에 냄새 뿌리기
    for i,a in enumerate(shark_loc):
      if a!=-1:
        x,y = a
        smell[x][y] = [i,k]

  return -1

n,m,k = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
dir = list(map(int,input().split()))
dir = [d-1 for d in dir]
next_dir = []
for _ in range(m):
  temp = []
  for _ in range(4):
    a = list(map(int,input().split()))
    a = [d-1 for d in a]
    temp.append(a)
  next_dir.append(temp)

print(solution(n,m,k,graph,dir,next_dir))