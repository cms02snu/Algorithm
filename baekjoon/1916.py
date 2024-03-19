# 1916

import heapq

def solution(n,m,graph,start,end):
  dist = [int(1e9)] * n
  h = []
  dist[start] = 0
  heapq.heappush(h,(0,start))

  while h:
    d,x = heapq.heappop(h)
    for nx,nd in graph[x]:
      if dist[nx]>d+nd:
        dist[nx] = d+nd
        heapq.heappush(h,(dist[nx],nx))

  return dist[end]

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
temp = {}
for _ in range(m):
  a,b,c = map(int,input().split())
  if (a,b) not in temp.keys():
    temp[(a,b)] = c
    graph[a-1].append((b-1,c))
  else:
    if c<temp[(a,b)]:
      graph[a-1].remove((b-1,temp[(a,b)]))
      temp[(a,b)] = c
      graph[a-1].append((b-1,c))

start,end = map(int,input().split())

print(solution(n,m,graph,start-1,end-1))