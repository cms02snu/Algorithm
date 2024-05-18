# 22114

'''
O(n)
k보다 작은 가장 긴 수열(하나는 큰거 껴있어도 됨)
dp[i][k] : i번째 시작, 점프 k번일 때 최대개수
dp[i][0] = dp[i+1][0]+1 or 0
dp[i][1] = dp[i+1][1]+1 or dp[i+1][0]+1
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,k,data):
    table = [[0]*2 for _ in range(n-1)]

    for i in range(n-2,-1,-1):
        if i==n-2:
            if data[i]>k:
                table[i][0] = 0
                table[i][1] = 1
            else:
                table[i][0] = 1
                table[i][1] = 1
        else:
            if data[i]>k:
                table[i][0] = 0
                table[i][1] = table[i+1][0] + 1
            else:
                table[i][0] = table[i+1][0] + 1
                table[i][1] = table[i+1][1] + 1

    return max([max(row) for row in table]) + 1

n,k = map(int,input().split())
data = list(map(int,input().split()))
print(solution(n,k,data))