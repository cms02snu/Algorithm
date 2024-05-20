# 15989

'''
dp[i][k] : k가 가장 큰 수인 i합 개수
dp[i][1] = dp[i-1][1]
dp[i][2] = dp[i-2][1] + dp[i-2][2]
dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
'''

def solution(n):
    table = [[0]*3 for _ in range(n+1)]

    for i in range(1,n+1):
        if i==1:
            table[1] = (1,0,0)
        elif i==2:
            table[2] = (1,1,0)
        elif i==3:
            table[3] = (1,1,1)
        else:
            table[i][0] = table[i-1][0]
            table[i][1] = table[i-2][0] + table[i-2][1]
            table[i][2] = table[i-3][0] + table[i-3][1] + table[i-3][2]

    return table

table = solution(int(1e4))
for _ in range(int(input())):
    print(sum(table[int(input())]))