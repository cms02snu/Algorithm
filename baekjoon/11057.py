# 11057

'''
dp[i][j] : i번째 자리 j로 끝나는 경우의 수
'''

N = int(1e4)+7

def solution(n):
    table = [[0]*10 for _ in range(n)]

    for i in range(n):
        for j in range(10):
            if i==0:
                table[0][j] = 1
            else:
                table[i][j] = sum(table[i-1][:j+1])%N
    
    return sum(table[n-1])%N

print(solution(int(input())))