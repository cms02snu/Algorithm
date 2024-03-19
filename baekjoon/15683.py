# 15683

'''
1번 - 상우하좌
2번 - 수직수평수직수평
3번 - 반시계쪽에 있는 화살표가 상우하좌
4번 - 빈 곳이 상우하좌
'''

import itertools
import copy

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def oneway_monitor(x,y,d,graph):
  while True:
    nx = x + dx[d]
    ny = y + dy[d]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if graph[nx][ny]==6:
        break
      if graph[nx][ny]==0:
        graph[nx][ny] = '#'
      x,y = nx,ny
    else:
      break

  return graph

def bfs(d,num,i,j,graph):
  if num==1:
    dir = d
    graph = oneway_monitor(i,j,dir,graph)

  if num==2:
    if d%2==0:
      for dir in [0,2]:
        graph = oneway_monitor(i,j,dir,graph)
    else:
      for dir in [1,3]:
        graph = oneway_monitor(i,j,dir,graph)

  if num==3:
    for dir in [d,(d+1)%4]:
      graph = oneway_monitor(i,j,dir,graph)

  if num==4:
    for dir in [dir for dir in list(range(4)) if dir!=d]:
      graph = oneway_monitor(i,j,dir,graph)

  if num==5:
    for dir in range(4):
      graph = oneway_monitor(i,j,dir,graph)

  return graph

def monitor(graph,dir_array,cctv_loc):
  for d,(num,i,j) in zip(dir_array,cctv_loc):
    graph = bfs(d,num,i,j,graph)

  return graph

def blindspot(graph):
  count = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j]==0:
        count += 1

  return count

def solution(_graph):
  cctv = {1:[],2:[],3:[],4:[],5:[]}

  for i in range(n):
    for j in range(m):
      if 6>_graph[i][j]>0:
        cctv[_graph[i][j]].append((i,j))

  cc1,cc2,cc3,cc4,cc5 = len(cctv[1]),len(cctv[2]),len(cctv[3]),len(cctv[4]),len(cctv[5])
  cctv_loc = [(1,i,j) for i,j in cctv[1]] + [(2,i,j) for i,j in cctv[2]] + [(3,i,j) for i,j in cctv[3]] + [(4,i,j) for i,j in cctv[4]] + [(5,i,j) for i,j in cctv[5]]

  result = 65
  for temp in itertools.product([0,1,2,3],repeat=cc1+cc2+cc3+cc4+cc5):
    graph = copy.deepcopy(_graph)
    graph = monitor(graph,temp,cctv_loc)
    result = min(result,blindspot(graph))

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(graph))