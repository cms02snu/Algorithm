# 1149

def solution(n,data):
  dp = [[0]*3 for _ in range(n)]
  for i in range(n):
    if i==0:
      for j in range(3):
        dp[0][j] = data[0][j]
    else:
      for j in range(3):
        dp[i][j] = min(dp[i-1][(j-1)%3],dp[i-1][(j+1)%3]) + data[i][j]

  return min(dp[n-1])

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,data))