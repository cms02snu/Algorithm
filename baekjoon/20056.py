# 20056

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move(x,y,s,d):
  nx = (x + s*dx[d])%n
  ny = (y + s*dy[d])%n

  return nx,ny

def solution(fireball,k):
  data = [[[] for _ in range(n)] for _ in range(n)]

  for _ in range(k):
    # step 1
    while fireball:
      x,y,m,s,d = fireball.pop(0)
      nx,ny = move(x,y,s,d)
      data[nx][ny].append((m,s,d))

    # step 2
    for i in range(n):
      for j in range(n):
        if len(data[i][j])>1:
          sum_m = 0
          sum_s = 0
          count = 0
          dir = -1
          nd = 0
          while data[i][j]:
            m,s,d = data[i][j].pop(0)
            sum_m += m
            sum_s += s
            count += 1
            if dir==-1:
              dir = d%2
            else:
              if dir!=d%2:
                nd = 1
          nm = sum_m//5
          ns = sum_s//count
          if nm>0:
            for mul in range(4):
              fireball.append((i,j,nm,ns,2*mul+nd))
        else:
          while data[i][j]:
            m,s,d = data[i][j].pop(0)
            fireball.append((i,j,m,s,d))

  result = 0
  for _,_,m,_,_ in fireball:
    result += m

  return result

n,m,k = map(int,input().split())
fireball = []
for _ in range(m):
  a,b,c,d,e = map(int,input().split())
  fireball.append([a-1,b-1,c,d,e])

print(solution(fireball,k))