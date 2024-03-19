# 1753

import heapq

def solution(n,start,graph):
  dist = [int(1e9)] * n
  dist[start] = 0
  h = []
  heapq.heappush(h,(0,start))

  while h:
    curr_d,x = heapq.heappop(h)
    for nx,next_d in graph[x]:
      if curr_d + next_d < dist[nx]:
        dist[nx] = curr_d + next_d
        heapq.heappush(h,(dist[nx],nx))

  for d in dist:
    if d==int(1e9):
      print('INF')
    else:
      print(d)

n,e = map(int,input().split())
start = int(input())
start -= 1
graph = [[] for _ in range(n)]
for _ in range(e):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  graph[a].append((b,c))

solution(n,start,graph)