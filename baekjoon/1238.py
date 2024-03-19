# 1238

import heapq

def solution(n,target,graph_go,graph_back):
  # GO
  dist_go = [int(1e9)] * n
  h = []
  dist_go[target] = 0
  heapq.heappush(h,(dist_go[target],target))

  while h:
    d,x = heapq.heappop(h)
    for nx,nd in graph_go[x]:
      if dist_go[nx]>d+nd:
        dist_go[nx] = d+nd
        heapq.heappush(h,(dist_go[nx],nx))

  # BACK
  dist_back = [int(1e9)] * n
  h = []
  dist_back[target] = 0
  heapq.heappush(h,(dist_back[target],target))

  while h:
    d,x = heapq.heappop(h)
    for nx,nd in graph_back[x]:
      if dist_back[nx]>d+nd:
        dist_back[nx] = d+nd
        heapq.heappush(h,(dist_back[nx],nx))

  result = 0
  for i in range(n):
    if dist_go[i]!=int(1e9) and dist_back[i]!=int(1e9):
      result = max(result,dist_go[i]+dist_back[i])

  return result

n,m,target = map(int,input().split())
graph_go = [[] for _ in range(n)]
graph_back = [[] for _ in range(n)]
for _ in range(m):
  a,b,c = map(int,input().split())
  graph_go[b-1].append((a-1,c))
  graph_back[a-1].append((b-1,c))

print(solution(n,target-1,graph_go,graph_back))