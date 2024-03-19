# 21611

'''
블리자드 마법 시전(구슬 파괴)
=> 구슬 이동해서 빈칸 채우기
=> 4개 이상 연속하는 구슬 폭발, 구슬 이동해서 빈칸 채우기
=> 4개 이상 연속하는 구슬 없을때까지 위의 과정 반복
=> 그룹별로 구슬 변화

구현 함수
0-1. n*n 칸 번호 그래프 생성하는 함수
0-2. 번호 별 좌표 리스트 생성하는 함수
1. 블리자드 마법 시전해서 구슬 파괴하는 함수
2. 빈칸 채우는 함수
3. 연속하는 구슬 찾아서 폭발시키는 함수
4. 그룹 찾아서 변화시키는 함수
'''

import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def graph_num(n):
  graph = [[0]*n for _ in range(n)]
  dx = [0,1,0,-1]
  dy = [-1,0,1,0]
  x,y = n//2,n//2-1
  graph[x][y] = 1
  x,y = n//2+1,n//2-1
  graph[x][y] = 2
  d = 2

  next = 2
  count_d = 0
  count_n = 0
  while graph[0][0]!=n**2-1:
    nx = x + dx[d]
    ny = y + dy[d]
    graph[nx][ny] = graph[x][y] + 1
    x,y = nx,ny
    count_d += 1
    if count_d==next:
      count_d = 0
      d = (d+1)%4
      count_n += 1
      if count_n==2:
        next += 1
        count_n = 0

  return graph

def num_sequence(n):
  num_graph = graph_num(n)
  x,y = n//2,n//2
  result = [(x,y)]

  for _ in range(n**2):
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if nx>=0 and nx<n and ny>=0 and ny<n:
        if num_graph[nx][ny]==num_graph[x][y]+1:
          result.append((nx,ny))
          x,y = nx,ny
          break

  return result

def blizzard(d,s,graph):
  x,y = n//2,n//2
  for _ in range(s):
    nx = x + dx[d]
    ny = y + dy[d]
    graph[nx][ny] = 0
    x,y = nx,ny

  return graph

def vacant(graph):
  x,y = n//2,n//2-1

  while True:
    # 가장 가까운 빈칸 찾기
    blank_start = -1
    blank_end = -1
    for i,(x,y) in enumerate(num_list):
      if i==0:
        continue
      if graph[x][y]==0:
        if blank_start==-1:
          blank_start = i
        else:
          blank_end = i
      else:
        if blank_start==-1:
          continue
        else:
          blank_end = i-1
          break

    # 빈칸 없다면 그만
    if blank_end==n**2-1 or blank_end==-1 or blank_start==-1:
      return graph

    # 있다면 땡겨
    k = blank_end-blank_start+1
    for i,(x,y) in enumerate(num_list):
      if i<=blank_end:
        continue
      nx,ny = num_list[i-k]
      graph[nx][ny] = graph[x][y]
      graph[x][y] = 0

def continuous(graph):
  con_start = -1
  count = 0
  curr_num = -1
  check = False
  bomb = 0

  for i,(x,y) in enumerate(num_list):
    if graph[x][y]!=curr_num:
      if count>=4:
        for i,j in num_list[con_start:con_start+count]:
          k = graph[i][j]
          graph[i][j] = 0
          check = True
        bomb += k*count
      con_start = i
      count = 1
      curr_num = graph[x][y]
    else:
      count += 1

  return check,bomb,graph

def change(graph):
  groups = []
  curr_num = graph[n//2][n//2-1]
  start = 1

  for i,(x,y) in enumerate(num_list):
    if i==0 or i==1:
      continue
    if graph[x][y]!=curr_num:
      groups.append(list(range(start,i)))
      curr_num = graph[x][y]
      start = i

  new_graph = [[0]*n for _ in range(n)]
  next = 1
  for group in groups:
    if next==n**2:
      break
    if next==n**2-1:
      new_graph[0][0] = len(group)
      break

    a = len(group)
    x0,y0 = num_list[next]
    x1,y1 = num_list[next+1]
    x2,y2 = num_list[group[0]]
    b = graph[x2][y2]
    new_graph[x0][y0] = a
    new_graph[x1][y1] = b

    next += 2

  return new_graph

def solution(n,graph,magic):
  global num_list,num_graph
  num_list = num_sequence(n)
  num_graph = graph_num(n)
  temp = copy.deepcopy(graph)
  result = 0

  for d,s in magic:
    # 블리자드 마법 시전(구슬 파괴)
    temp = blizzard(d,s,temp)

    # 빈칸 채우기
    temp = vacant(temp)

    # 연속하는 구슬 폭발, 빈칸 채우기
    while True:
      check,bomb,temp = continuous(temp)
      if not check:
        break
      result += bomb
      temp = vacant(temp)

    # 구슬 변화
    temp = change(temp)

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))
magic = []
for _ in range(m):
  a,b = map(int,input().split())
  magic.append((a-1,b))

print(solution(n,graph,magic))