# 17143

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def solution(n,m,shark_info):
  graph = [[[] for _ in range(m)] for _ in range(n)]
  for x,y,v,d,size in shark_info:
    graph[x][y] = [size]

  result = 0

  # 낚시왕이 i번째 열에 있을 때의 과정
  for i in range(m):
    # step 2
    temp = [(x,y,v,d,size) for x,y,v,d,size in shark_info if y==i]
    if temp:
      temp.sort()
      a = temp[0]
      s = a[4]
      result += s
      shark_info.remove(a)
      graph[a[0]][a[1]] = []

    # step 3
    new_shark_info = []
    for x,y,v,d,size in shark_info:
      graph[x][y].remove(size)
      moved = 0
      while moved<v:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=m:
          if d==0:
            d = 1
          elif d==1:
            d = 0
          elif d==2:
            d = 3
          elif d==3:
            d = 2
          continue
        x,y = nx,ny
        moved += 1

      new_shark_info.append((x,y,v,d,size))
      graph[x][y].append(size)
    shark_info = new_shark_info

    for i in range(n):
      for j in range(m):
        if len(graph[i][j])>1:
          max_size = 0
          for s in graph[i][j]:
            max_size = max(max_size,s)
          others = [s for s in graph[i][j] if s!=max_size]
          others_info = [a for a in shark_info if a[4] in others]
          for a in others_info:
            shark_info.remove(a)
          graph[i][j] = [max_size]

  return result

n,m,s = map(int,input().split())
shark_info = []
for _ in range(s):
  x,y,v,d,size = map(int,input().split())
  shark_info.append((x-1,y-1,v,d-1,size))

print(solution(n,m,shark_info))