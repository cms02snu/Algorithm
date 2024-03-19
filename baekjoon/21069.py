# 21069

import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_biggest_group(data):
  visited = [[False]*n for _ in range(n)]
  groups = []

  for i in range(n):
    for j in range(n):
      if not visited[i][j] and data[i][j]>0:
        group = [(i,j)]
        visited[i][j] = True
        num = data[i][j]
        queue = deque([(i,j)])
        visited_zero = []
        while queue:
          x,y = queue.popleft()
          for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
              if not visited[nx][ny]:
                if data[nx][ny]==0 or data[nx][ny]==num:
                  if data[nx][ny]==num:
                    visited[nx][ny] = True
                  else:
                    if (nx,ny) in visited_zero:
                      continue
                    else:
                      visited_zero.append((nx,ny))
                  group.append((nx,ny))
                  queue.append((nx,ny))
        groups.append(group)

  # 그룹크기,무지개블록수,기준블록좌표
  group_info = []
  for group in groups:
    count_len = 0
    count_rb = 0
    temp = []
    for x,y in group:
      count_len += 1
      if data[x][y]==0:
        count_rb+=1
      else:
        temp.append((x,y))
    temp.sort()
    standard = temp[0]
    group_info.append((count_len,count_rb,standard))

  if groups:
    temp = [(-group_info[i][0],-group_info[i][1],-group_info[i][2][0],-group_info[i][2][1],group) for i,group in enumerate(groups)]
    temp.sort()
    return -temp[0][0], temp[0][4]
  else:
    return 0,[]

def gravity(data):
  '''
좌우반전 후 행별로 오른쪽으로 민 후 다시 행별로 합쳐서 다시 좌우반전
  '''
  mirrored_data = [[0]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      mirrored_data[i][j] = data[j][i]

  mirrored_result = []
  for i in range(n):
    temp = mirrored_data[i]
    while True:
      changed = False
      for j in range(n-2,-1,-1):
        if temp[j]>=0 and temp[j+1]==-2:
          temp[j+1] = temp[j]
          temp[j] = -2
          changed = True
      if not changed:
        break
    mirrored_result.append(temp)

  result = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      result[i][j] = mirrored_result[j][i]

  return result

def rotate(data):
  temp0 = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      temp0[i][j] = data[i][n-1-j]
  temp1 = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      temp1[i][j] = temp0[j][i]

  return temp1

def solution(n,m,_data):
  data = copy.deepcopy(_data)

  result = 0

  while True:
    # Step 1
    num,group = find_biggest_group(data)
    if num<=1:
      break
    # Step 2
    for x,y in group:
      data[x][y] = -2
    result += num**2
    # Step 3
    data = gravity(data)
    # Step 4
    data = rotate(data)
    # Step 5
    data = gravity(data)

  return result

n,m = map(int,input().split())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,m,data))