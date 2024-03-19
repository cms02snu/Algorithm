# 21608

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def satisfy(x,y):
  count = 0
  student = graph[x][y]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<n:
      if graph[nx][ny] in likes[student]:
        count += 1

  if count==0:
    return 0
  else:
    return 10**(count-1)

def sit(student,like):
  num_likes_vacant = []
  for x in range(n):
    for y in range(n):
      if graph[x][y]==-1:
        count_likes = 0
        count_vacant = 0
        for d in range(4):
          nx = x + dx[d]
          ny = y + dy[d]
          if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] in like:
              count_likes += 1
            elif graph[nx][ny]==-1:
              count_vacant += 1
        num_likes_vacant.append((-count_likes,-count_vacant,x,y))

  num_likes_vacant.sort()
  _,_,i,j = num_likes_vacant[0]
  graph[i][j] = student

def solution(n,order,likes):
  global graph
  graph = [[-1]*n for _ in range(n)]
  for i in order:
    sit(i,likes[i])

  result = 0
  for i in range(n):
    for j in range(n):
      result += satisfy(i,j)

  return result

n = int(input())
order = []
likes = [-1 for _ in range(n**2)]
for _ in range(n**2):
  a,b,c,d,e = map(int,input().split())
  order.append(a-1)
  likes[a-1] = [b-1,c-1,d-1,e-1]

print(solution(n,order,likes))