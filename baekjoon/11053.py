# 11053

def solution(n,data):
  table = [0]*n
  table[0] = 1
  for i in range(1,n):
    max_val = 0
    for j in range(i):
      if data[j]<data[i]:
        max_val = max(max_val,table[j])
    table[i] = max_val + 1

  return max(table)

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))