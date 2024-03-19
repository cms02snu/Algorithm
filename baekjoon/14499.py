# 14499

'''
d - 동 서 북 남
dice - 윗면, 아랫면. 상, 하, 좌, 우
'''

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def roll(dice,d):
  if d==0:
    return [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]]
  elif d==1:
    return [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]]
  elif d==2:
    return [dice[3],dice[2],dice[0],dice[1],dice[4],dice[5]]
  elif d==3:
    return [dice[2],dice[3],dice[1],dice[0],dice[4],dice[5]]

def solution(n,m,x,y,graph,moves):
  dice = [0,0,0,0,0,0]

  for d in moves:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=m:
      continue
    else:
      dice = roll(dice,d)
      if graph[nx][ny]==0:
        graph[nx][ny] = dice[1]
      else:
        dice[1] = graph[nx][ny]
        graph[nx][ny] = 0
      x,y = nx,ny

    print(dice[0])

n,m,x,y,k = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
moves = list(map(int,input().split()))
moves = [a-1 for a in moves]

solution(n,m,x,y,graph,moves)