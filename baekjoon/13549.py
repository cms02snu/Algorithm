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

def d2(i,n):
  while True:
    if i%2==1:
      return i
    
    if i//2<n:
      return i
    
    i //= 2

def solution2(n,k):
  if n>=k:
    return n-k
  
  table = [-1] * (2*k+1)

  for i in range(n):
    table[i] = n-i

  for i in range(n+1,k+1):
    if i%2==0:
      table[i] = i-n

  for i in range(n+1,2*k+1):
    if i%2==0:
      j = d2(i,n)
      if j%2==1:
        if table[j]==-1:
          table[j] = min(table[j-1],table[j+1]) + 1
      table[i] = table[j]

  print(table)

  return table[k]

n,k = map(int,input().split())

print(solution2(n,k))