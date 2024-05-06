# 12026

'''
dp[i] : i번째 칸에 도착하는 최소비용
dp[i] = min(dp[j]+k*k)
'''

def solution(n,temp):
    data = []
    for a in temp:
        if a=='B':
            data.append(0)
        elif a=='O':
            data.append(1)
        else:
            data.append(2)

    table = [0] * n

    for i in range(1,n):
        _min = int(1e9)
        for j in range(i):
            if data[j]==(data[i]-1)%3 and table[j]!=-1:
                k = table[j] + (i-j)*(i-j)
                _min = min(_min,k)
        if _min==int(1e9):
            table[i] = -1
        else:
            table[i] = _min

    return table[n-1]

n = int(input())
data = list(input())

print(solution(n,data))