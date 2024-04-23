# 2688

'''
dp[i][k] : i자리수가 k로 끝나는 안줄수 개수
dp[i][k] = sum(dp[i-1][x<=k])
'''

def solution(n):
    table = [[0]*10 for _ in range(n)]
    for i in range(n):
        if i==0:
            for k in range(10):
                table[0][k] = 1
        else:
            for k in range(10):
                _sum = 0
                for x in range(k+1):
                    _sum += table[i-1][x]
                table[i][k] = _sum

    return sum(table[n-1])

result = [-1] * 65
for i in range(1,65):
    result[i] = solution(i)

for _ in range(int(input())):
    print(result[int(input())])