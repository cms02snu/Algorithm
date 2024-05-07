# 17626

'''
dp[i] : i 제곱수 최소개수
dp[i] = min(dp[i-k^2])
'''

def solution(n):
    table = [0] * (n+1)

    for i in range(1,n+1):
        k = 1
        _min = int(1e9)
        while i-k*k>=0:
            _min = min(_min,table[i-k*k])
            k += 1
        table[i] = _min+1

    return table[n]

print(solution(int(input())))