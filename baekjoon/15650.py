# 15650

import itertools

def solution(n,m):
  for temp in itertools.combinations(list(range(1,n+1)),m):
    for i,a in enumerate(temp):
      if i==m-1:
        print(a)
      else:
        print(a,end=' ')

n,m = map(int,input().split())

solution(n,m)