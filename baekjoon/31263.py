# 31263

'''
dp[i] : i번째 숫자까지 구성하는 최소인원
dp[i] = min(dp[i-3],dp[i-2],dp[i-1]) + 1 (가능한것만)
data[i-k]가 0이라면 dp[i-k-1]은 후보에서 제외
'''

def solution(n,data):
    table = [0] * n
    for i in range(n):
        if i==0:
            table[0] = 1
        elif i==1:
            table[1] = 1
        elif i==2:
            if int(data[:3])>641:
                table[2] = 2
            else:
                table[2] = 1
        else:
            _min = int(1e9)
            for k in range(3):
                if k==2:
                    if int(data[i-2:i+1])<=641:
                        if data[i-2]!='0':
                            _min = min(_min,table[i-3])
                else:
                    if data[i-k]!='0':
                        _min = min(_min,table[i-k-1])
            table[i] = _min+1
    print(table)
    return table[n-1]           

n = int(input())
data = input()

print(solution(n,data))

