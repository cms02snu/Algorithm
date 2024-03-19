# 18310

def solution(n,data):
  data.sort()
  return data[(n-1)//2]

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))