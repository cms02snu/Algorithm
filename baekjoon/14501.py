# 14501

'''
dp(i) : i일 이후까지의 최댓값
'''

def dp(i):
  d,a = data[i]
  if i==n-1:
    if i+d<=n:
      table[n-1] = a
    else:
      table[n-1] = 0

  else:
    if i+d<n:
      table[i] = max(table[i+1],a+table[i+d])
    elif i+d==n:
      table[i] = max(table[i+1],a)
    else:
      table[i] = table[i+1]

def solution(n,data):
  global table
  table = [0] * n

  for i in range(n-1,-1,-1):
    dp(i)

  return table[0]

n = int(input())
data = []
for _ in range(n):
  a,b = map(int,input().split())
  data.append((a,b))

print(solution(n,data))