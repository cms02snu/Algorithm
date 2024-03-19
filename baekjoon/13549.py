# 13549

from collections import deque

N = int(1e5)

def solution(n,k):
  table = [-1] * (N+1)
  table[n] = 0

  queue = deque()
  queue.append(n)

  while queue:
    x = queue.popleft()
    if x*2<=N:
      if table[x*2]==-1:
        table[x*2] = table[x]
        queue.appendleft(x*2)
    if x-1>=0:
      if table[x-1]==-1:
        table[x-1] = table[x] + 1
        queue.append(x-1)
    if x+1<=N:
      if table[x+1]==-1:
        table[x+1] = table[x] + 1
        queue.append(x+1)

  return table[k]

n,k = map(int,input().split())

print(solution(n,k))