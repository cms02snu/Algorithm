# 16234

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
  i,j = x,y
  if parent[x][y]==(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
      x,y = queue.popleft()
      for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<n:
          if (nx,ny)!=(i,j) and parent[nx][ny]==(nx,ny) and M>=abs(data[nx][ny]-data[x][y])>=m:
            parent[nx][ny] = parent[i][j]
            queue.append((nx,ny))

def solution(n,m,M,data):
  global parent

  day = 0
  while True:
    parent = [[-1]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        parent[i][j] = (i,j)

    for i in range(n):
      for j in range(n):
        bfs(i,j)

    temp = {}
    for i in range(n):
      for j in range(n):
        if parent[i][j]==(i,j):
          temp[(i,j)] = [(i,j)]
        else:
          temp[parent[i][j]].append((i,j))

    move = False
    for groups in temp.values():
      if len(groups)>1:
        move = True
        ssum = 0
        total = 0
        for i,j in groups:
          ssum += data[i][j]
          total += 1
        result = ssum//total
        for i,j in groups:
          data[i][j] = result

    if not move:
      break

    day += 1

  return day

n,m,M = map(int,input().split())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,m,M,data))