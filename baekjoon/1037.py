# 1037

def solution(n,array):
  if n==1:
    return array[0]**2
  else:
    array.sort()
    return array[0] * array[-1]

n = int(input())
array = list(map(int,input().split()))

print(solution(n,array))