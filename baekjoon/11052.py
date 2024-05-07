# 11052

'''
dp[i] : i개 카드 최대금액
dp[i] = max(dp[i-k]+dp[k])
'''

def solution(n,data):
    table = [0] * (n+1)

    for i in range(1,n+1):
        if i==1:
            table[1] = data[0]
        else:
            _max = data[i-1]
            for k in range(1,i//2+1):
                _max = max(_max,table[i-k]+table[k])
            table[i] = _max

    return table[n]

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))