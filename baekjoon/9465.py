# 9465

def solution(n,data):
  dp = [[0]*n for _ in range(2)]
  dp[0][0] = data[0][0]
  dp[1][0] = data[1][0]

  # dp[i][j] : (i,j) 스티커 사용할 때 j열 전까지의 사용한 스티커들의 최댓값
  for i in range(1,n):
    dp[0][i] = max(dp[0][i-1],dp[1][i-1]+data[0][i])
    dp[1][i] = max(dp[1][i-1],dp[0][i-1]+data[1][i])

  return max([max(row) for row in dp])

t = int(input())
for _ in range(t):
  n = int(input())
  data = []
  for _ in range(2):
    data.append(list(map(int,input().split())))
  print(solution(n,data))