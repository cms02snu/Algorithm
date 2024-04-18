# 11049

'''
dp[i][j] : i번째 행렬부터 j번째 행렬까지 최소연산횟수
dp[i][j] = min(dp[i][t]+dp[t+1][j]+data[i][0]*data[t][1]*data[j][1]) for t
t(term)이 작은것부터 갱신 
'''

def solution(data):
    table = [[0]*n for _ in range(n)]

    for t in range(1,n):
        for i in range(n):
            if i+t==n:
                break

            table[i][i+t] = int(1e9)

            for term in range(i,i+t):
                table[i][i+t] = min(table[i][i+t],
                                    table[i][term]+table[term+1][i+t]+
                                    data[i][0]*data[term][1]*data[i+t][1])

    return table[0][n-1]

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int,input().split())))

print(solution(data))