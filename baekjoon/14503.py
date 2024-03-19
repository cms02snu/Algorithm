# 14503

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check_notclean_vacant(x,y,clean):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if not clean[nx][ny] and graph[nx][ny]==0:
      return True

  return False

def solution(n,m,x,y,d,graph):
  clean = [[False]*m for _ in range(n)]

  count = 0

  while True:
    # Step 1
    if not clean[x][y]:
      clean[x][y] = True
      count += 1

    # Step 2
    if not check_notclean_vacant(x,y,clean):
      nx = x + dx[(d-2)%4]
      ny = y + dy[(d-2)%4]
      if graph[nx][ny]==0:
        x,y = nx,ny
        continue
      else:
        break

    # Step 3
    else:
      d = (d-1)%4
      nx = x + dx[d]
      ny = y + dy[d]
      if graph[nx][ny]==0 and not clean[nx][ny]:
        x,y = nx,ny

  return count

n,m = map(int,input().split())
x,y,d = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(n,m,x,y,0,graph))