# 3190

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solution(n,apples,moves):
  snakes = [(0,0)]
  x,y = 0,0
  d = 1
  time = 0

  while True:
    time += 1

    nx = x + dx[d]
    ny = y + dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=n:
      break
    else:
      if (nx,ny) in snakes:
        break
      else:
        if (nx,ny) in apples:
          apples.remove((nx,ny))
          snakes.append((nx,ny))
        else:
          snakes.pop(0)
          snakes.append((nx,ny))

    x,y = nx,ny

    if moves:
      if time==moves[0][0]:
        if moves[0][1]=='L':
          d = (d-1)%4
        else:
          d = (d+1)%4
        moves.pop(0)

  return time

n = int(input())
apples = []
for _ in range(int(input())):
  a,b = map(int,input().split())
  apples.append((a-1,b-1))
moves = []
for _ in range(int(input())):
  a,b = input().split()
  moves.append((int(a),b))

print(solution(n,apples,moves))