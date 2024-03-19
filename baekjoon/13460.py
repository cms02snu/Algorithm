# 13460

'''
4**10(1,000,000)을 모두 계산한다는 생각으로 가야돼
RB가 한 라인에 있을 때의 움직임을 잘 구현하는게 포인트
특정 방향으로 기울였을 때 구슬 위치이동 없다면 체크해야
두 구슬이 구멍에 같이 빠지는 경우도 잘 고려해야됨
'''

'''
incline 함수
- B가 구멍에 빠지는 경우 => -1 return
- R만 구멍에 빠졌을 경우 => 1 return
- 그 외 0 return
'''

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move_rb(graph,r_loc,b_loc,dir):
  for i in range(n):
    for j in range(m):
      if graph[i][j] in ['R','B']:
        graph[i][j] = '.'

  x,y = r_loc
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if graph[nx][ny]=='#':
      final_r_loc = (x,y)
      break
    elif graph[nx][ny]=='O':
      final_r_loc = (-1,-1)
      break
    else:
      graph[x][y] = '.'
      graph[nx][ny] = 'R'
      x,y = nx,ny

  x,y = b_loc
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if graph[nx][ny]=='#':
      final_b_loc = (x,y)
      break
    elif graph[nx][ny]=='O':
      final_b_loc = (-1,-1)
      break
    else:
      graph[x][y] = '.'
      graph[nx][ny] = 'B'
      x,y = nx,ny

  if final_b_loc==(-1,-1):
    return -1,graph
  elif final_r_loc==(-1,-1):
    return 1,graph
  elif final_b_loc==final_r_loc:
    if dir==0:
      if b_loc[0]<r_loc[0]:
        final_r_loc = (final_r_loc[0]+1,final_r_loc[1])
      else:
        final_b_loc = (final_b_loc[0]+1,final_b_loc[1])
    elif dir==1:
      if b_loc[0]<r_loc[0]:
        final_b_loc = (final_b_loc[0]-1,final_b_loc[1])
      else:
        final_r_loc = (final_r_loc[0]-1,final_r_loc[1])
    elif dir==2:
      if b_loc[1]>r_loc[1]:
        final_b_loc = (final_b_loc[0],final_b_loc[1]+1)
      else:
        final_r_loc = (final_r_loc[0],final_r_loc[1]+1)
    elif dir==3:
      if b_loc[1]<r_loc[1]:
        final_b_loc = (final_b_loc[0],final_b_loc[1]-1)
      else:
        final_r_loc = (final_r_loc[0],final_r_loc[1]-1)

  graph[final_r_loc[0]][final_r_loc[1]] = 'R'
  graph[final_b_loc[0]][final_b_loc[1]] = 'B'

  return 0,graph

def move_r_b(graph,r_loc,b_loc,dir):
  x,y = r_loc
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if graph[nx][ny]=='#':
      break
    elif graph[nx][ny]=='O':
      return 1,graph
    else:
      graph[x][y] = '.'
      graph[nx][ny] = 'R'
      x,y = nx,ny

  x,y = b_loc
  while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if graph[nx][ny]=='#':
      break
    elif graph[nx][ny]=='O':
      return -1,graph
    else:
      graph[x][y] = '.'
      graph[nx][ny] = 'B'
      x,y = nx,ny

  return 0,graph

def incline(graph,dir):
  temp = [[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      temp[i][j] = graph[i][j]
      if graph[i][j]=='R':
        r_loc = (i,j)
      elif graph[i][j]=='B':
        b_loc = (i,j)
      elif graph[i][j]=='O':
        o_loc = (i,j)

  # 위나 아래로 기울이는 경우
  if dir<=1:
    # R과 B가 같은 열에 있는 경우
    if r_loc[1]==b_loc[1]:
      check,temp = move_rb(temp,r_loc,b_loc,dir)
    # R과 B가 다른 열에 있는 경우
    else:
      check,temp = move_r_b(temp,r_loc,b_loc,dir)
  # 좌나 우로 기울이는 경우
  else:
    # R가 B가 같은 행에 있는 경우
    if r_loc[0]==b_loc[0]:
      check,temp = move_rb(temp,r_loc,b_loc,dir)
    # R과 B가 다른 행에 있는 경우
    else:
      check,temp = move_r_b(temp,r_loc,b_loc,dir)

  return check,temp

def dfs(graph,count):
  global result
  if count==10:
    return

  for dir in range(4):
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
      for j in range(m):
        temp[i][j] = graph[i][j]
    check,temp = incline(temp,dir)
    if check==0:
      dfs(temp,count+1)
    if check==1:
      result = min(result,count+1)

def solution(n,m,graph):
  global result
  result = 11

  dfs(graph,0)

  if result==11:
    return -1

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

print(solution(n,m,graph))