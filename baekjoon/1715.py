# 1715

import heapq

def solution(n,h):
  result = 0
  while len(h)>1:
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    heapq.heappush(h,(x+y))
    result += x+y

  return result

n = int(input())
data = []
for _ in range(n):
  heapq.heappush(data,int(input()))

print(solution(n,data))