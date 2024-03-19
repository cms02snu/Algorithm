# 19236

import copy

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def fish_move(fish_loc,fish_dir):
  fish_loc_db = [-1] * 17
  for i in range(4):
    for j in range(4):
      if fish_loc[i][j]!=-1:
        fish_loc_db[fish_loc[i][j]] = (i,j)

  for num,loc in enumerate(fish_loc_db):
    if num==0 or loc==-1:
      continue
    x,y = loc
    d = fish_dir[x][y]
    temp = [i for i in range(d,8)] + [i for i in range(0,d)]
    for dir in temp:
      nx = x + dx[dir]
      ny = y + dy[dir]
      if nx>=0 and nx<4 and ny>=0 and ny<4:
        if (nx,ny)!=shark_loc:
          fish_loc_db[num] = (nx,ny)
          if fish_loc[nx][ny]!=-1:
            fish_loc_db[fish_loc[nx][ny]] = (x,y)
          fish_loc[nx][ny],fish_loc[x][y] = fish_loc[x][y],fish_loc[nx][ny]
          fish_dir[x][y] = fish_dir[nx][ny]
          fish_dir[nx][ny] = dir
          break

  return fish_loc,fish_dir

def shark_move(fish_loc,fish_dir):
  x,y = shark_loc
  d = shark_dir
  next_sharks = []
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx>=0 and nx<4 and ny>=0 and ny<4:
      if fish_loc[nx][ny]!=-1:
        next_sharks.append((nx,ny))
      x,y = nx,ny
    else:
      break

  return next_sharks

def dfs(count,fish_loc,fish_dir):
  global result,shark_loc,shark_dir
  fish_loc,fish_dir = fish_move(fish_loc,fish_dir)
  next_sharks = shark_move(fish_loc,fish_dir)

  if not next_sharks:
    result = max(result,count)
    return

  for nx,ny in next_sharks:
    temp_loc = copy.deepcopy(fish_loc)
    temp_dir = copy.deepcopy(fish_dir)
    shark_loc = (nx,ny)
    shark_dir = temp_dir[nx][ny]
    a = temp_loc[nx][ny]
    temp_loc[nx][ny] = -1
    temp_dir[nx][ny] = -1
    dfs(count+a,temp_loc,temp_dir)

def solution(fish_loc,fish_dir):
  global result,shark_loc,shark_dir
  result = 0

  shark_loc = (0,0)
  shark_dir = fish_dir[0][0]
  ate = fish_loc[0][0]
  fish_dir[0][0] = -1
  fish_loc[0][0] = -1

  dfs(ate,fish_loc,fish_dir)

  return result

fish_loc = []
fish_dir = []
for _ in range(4):
  a0,a1,b0,b1,c0,c1,d0,d1 = map(int,input().split())
  fish_loc.append([a0,b0,c0,d0])
  fish_dir.append([a1-1,b1-1,c1-1,d1-1])

print(solution(fish_loc,fish_dir))