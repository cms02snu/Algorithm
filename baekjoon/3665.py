# 3665

import copy

def solution(n,data,reverse):
  indegree = [-1]*(n+1)
  for rank,i in enumerate(data):
    indegree[i] = rank

  new_indegree = copy.copy(indegree)
  for a,b in reverse:
    if indegree[a]>indegree[b]:
      new_indegree[a] -= 1
      new_indegree[b] += 1
    else:
      new_indegree[a] += 1
      new_indegree[b] -= 1

  temp = [(new_indegree[i],i) for i in range(1,n+1)]
  temp.sort()

  if sorted(new_indegree[1:])==list(range(n)):
    for rank,i in temp:
      if rank==n-1:
        print(i)
      else:
        print(i,end=' ')

  else:
    print('IMPOSSIBLE')

for _ in range(int(input())):
  n = int(input())
  data = list(map(int,input().split()))
  reverse = []
  for _ in range(int(input())):
    a,b = map(int,input().split())
    reverse.append((a,b))

  solution(n,data,reverse)