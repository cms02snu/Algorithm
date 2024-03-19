# 13172

import itertools

def solution(n,m,data):
  data.sort()
  printed = set()

  for temp in itertools.permutations(data,m):
    if temp not in printed:
      printed.add(temp)
      for i,a in enumerate(temp):
        if i==m-1:
          print(a)
        else:
          print(a,end=' ')

n,m = map(int,input().split())
data = list(map(int,input().split()))

solution(n,m,data)