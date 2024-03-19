# 21610

dx = [0,-1,-1,-1,0,1,1,1,]
dy = [-1,-1,0,1,1,1,0,-1]

cx = [-1,-1,1,1]
cy = [-1,1,-1,1]

def water_duplicate(x,y,water):
  count = 0
  for i in range(4):
    nx = x + cx[i]
    ny = y + cy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if water[nx][ny]>0:
        count += 1

  water[x][y] += count

  return water

def solution(n,water,moves):
  clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
  for dir,dist in moves:
    # step 1
    for i,(x,y) in enumerate(clouds):
      nx = (x + dist*dx[dir])%n
      ny = (y + dist*dy[dir])%n
      clouds[i] = (nx,ny)

    # step 2
    for x,y in clouds:
      water[x][y] += 1

    # step 3

    # step 4
    for x,y in clouds:
      water = water_duplicate(x,y,water)

    # step 5
    new_clouds = []
    for i in range(n):
      for j in range(n):
        if water[i][j]>=2:
          if (i,j) not in clouds:
            new_clouds.append((i,j))
            water[i][j] -= 2
    clouds = new_clouds

  count = 0
  for i in range(n):
    for j in range(n):
      count += water[i][j]

  return count

n,m = map(int,input().split())
water = []
for _ in range(n):
  water.append(list(map(int,input().split())))
moves = []
for _ in range(m):
  a,b = map(int,input().split())
  moves.append((a-1,b))

print(solution(n,water,moves))