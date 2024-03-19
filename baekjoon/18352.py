# 18352

from collections import deque

def solution(graph,n,k,start):
  dist = [int(1e9)] * n
  queue = deque()
  dist[start] = 0
  queue.append(start)

  while queue:
    x = queue.popleft()
    for nx in graph[x]:
      if dist[nx]>dist[x]+1:
        queue.append(nx)
        dist[nx] = dist[x] + 1

  check = False
  for i,d in enumerate(dist):
    if d==k:
      print(i+1)
      check = True

  if not check:
    print(-1)

n,m,k,start = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a-1].append(b-1)

solution(graph,n,k,start-1)