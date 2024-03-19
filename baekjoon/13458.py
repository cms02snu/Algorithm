# 13458

def count_n(a,b,c):
  if a<=b:
    return 1
  else:
    a -= b
    q = a//c
    r = a%c
    if r==0:
      return 1+q
    else:
      return 2+q

def solution(n,data,b,c):
  result = [-1] * n
  for i in range(n):
    result[i] = count_n(data[i],b,c)

  return sum(result)

n = int(input())
data = list(map(int,input().split()))
b,c = map(int,input().split())

print(solution(n,data,b,c))