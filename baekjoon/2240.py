# 2240

'''
dp[i][j] : i번째 자두까지 j번 이동했을 때 받는 자두 최댓값
if data[i]==j%2:
    dp[i][j] = max(dp[i-1][j]+1,dp[i-1][j-1]+1)
else:
    dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])

(0,0)=0 (0,1)=1
(1,0)=1 (1,1)=1 (1,2)=2
(2,0)=2 (2,1)=1 (2,2)=3
(3,0)=2 (3,1)=3 (3,2)=3
'''

def solution(t,w,data):
    table = [[0]*(w+1) for _ in range(t)]

    for i in range(t):
        for j in range(w+1):
            if j>i+1:
                continue
            if i==0:
                if j==0:
                    if data[0]==0:
                        table[0][0] = 1
                        table[0][1] = 0
                    else:
                        table[0][0] = 0
                        table[0][1] = 1

            else:
                if j==0:
                    if data[i]==j%2:
                        table[i][0] = table[i-1][0]+1
                    else:
                        table[i][0] = table[i-1][0]
                else:
                    if data[i]==j%2:
                        table[i][j] = max(table[i-1][j-1],table[i-1][j])+1
                    else:
                        table[i][j] = max(table[i-1][j-1],table[i-1][j])

    return max(table[t-1])

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(int(input())-1)

print(solution(n,m,data))