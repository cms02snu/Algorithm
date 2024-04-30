# 11062

'''
dfs(array) : (선공이 얻는 점수,후공이 얻는 점수)
선공은 다음 상태에서 후공이 얻는 점수가 최대가 되도록 카드를 가져간다

_,k1 = dfs(next_0)
_,k2 = dfs(next_1)
k1과 k2 중 큰 쪽 카드를 가져간다

2개 남았을 때 큰 걸 선공이 가져가고 작은걸 후공이 가져가도록 return 한다
'''

def dfs(data):
    if data in dp:
        return dp[data]
    
    if len(data)==1:
        dp[data] = (data[0],0)
        return dp[data]
    
    if len(data)==2:
        dp[data] = (max(data),min(data))
        return dp[data]
    
    a0,b0 = dfs(data[1:])
    a1,b1 = dfs(data[:-1])

    if data[0]+b0>data[-1]+b1:
        dp[data] = (data[0]+b0,a0)    
    else:
        dp[data] = (data[-1]+b1,a1)

    return dp[data]

for _ in range(int(input())):
    n = int(input())
    data = tuple(map(int,input().split()))
    dp = {}
    print(dfs(data)[0])