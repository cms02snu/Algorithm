# 1932

def solution(n,data):
  for i in range(1,n):
    for j in range(i+1):
      if j==0:
        data[i][0] = data[i-1][0] + data[i][0]
      elif j==i:
        data[i][i] = data[i-1][i-1] + data[i][i]
      else:
        data[i][j] = max(data[i-1][j-1],data[i-1][j]) + data[i][j]

  return max(data[n-1])

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,data))