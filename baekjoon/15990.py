# 15990

'''
dp[i][j] : i를 마지막자리 j인 수들의 합으로 나타내는 경우의 수
dp[i][j] = sum(dp[i-k][j!=k])
'''

N = int(1e9) + 9

def solution(n):
    table = [[0]*4 for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,4):
            if i==1:
                if j==1:
                    table[1][1] = 1
            elif i==2:
                if j==2:
                    table[2][2] = 1
            elif i==3:
                if j==1:
                    table[3][1] = 1
                elif j==2:
                    table[3][2] = 1
                else:
                    table[3][3] = 1
            else:
                _sum = 0
                for k in range(1,4):
                    if k!=j:
                        _sum += table[i-j][k]
                table[i][j] = _sum%N
    
    return table

table = solution(int(1e5))

for _ in range(int(input())):
    print(sum(table[int(input())])%N)