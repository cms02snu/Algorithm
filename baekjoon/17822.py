# 17822

'''
y좌표는 넘어가서 인접하지만 x좌표는 안그럼
구현함수
- i번째 원판 d방향으로 회전시키는 함수
- 인접한 수들의 집합 찾아서 없애는 함수
- 평균작하는 함수
'''

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate(board,i,d,k):
  temp = board[i][1:]
  if d==0:
    for _ in range(k):
      temp = [temp[-1]] + temp[:-1]
  else:
    for _ in range(k):
      temp = temp[1:] + [temp[0]]

  board[i] = ['X'] + temp

  return board

def adjacent(board):
  result = []
  for i in range(1,n+1):
    for j in range(1,m+1):
      if (i,j) in result:
        continue
      target = board[i][j]
      if target=='X':
        continue
      queue = deque()
      queue.append((i,j))
      while queue:
        x,y = queue.popleft()
        for d in range(4):
          nx = x + dx[d]
          ny = (y+dy[d]-1)%m + 1
          if nx>0 and nx<=n and ny>0 and ny<=m:
            if board[nx][ny]==target and (nx,ny) not in result:
              queue.append((nx,ny))
              result.append((nx,ny))

  return result

def normalize(board):
  _sum = 0
  count = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
      if board[i][j]!='X':
        _sum += board[i][j]
        count += 1

  if count==0:
    return board

  _mean = _sum / count
  for i in range(1,n+1):
    for j in range(1,m+1):
      if board[i][j]!='X':
        if board[i][j]>_mean:
          board[i][j] -= 1
        elif board[i][j]<_mean:
          board[i][j] += 1

  return board

def solution(board,data):
  for x,d,k in data:
    # step 1
    for i in range(1,n//x+1):
      board = rotate(board,i*x,d,k)

    # step 2
    temp = adjacent(board)
    if temp:
      for a,b in temp:
        board[a][b] = 'X'
    else:
      board = normalize(board)

  result = 0
  for i in range(1,n+1):
    for j in range(1,m+1):
      if board[i][j]!='X':
        result += board[i][j]

  return result

n,m,t = map(int,input().split())
board = [['X'] * (m+1)]
for _ in range(n):
  board.append(['X'] + list(map(int,input().split())))
data = []
for _ in range(t):
  data.append(list(map(int,input().split())))

print(solution(board,data))