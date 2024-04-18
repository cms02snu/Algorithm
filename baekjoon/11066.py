# 11066

'''
행렬곱셈순서랑 똑같이 풀자
table[i][j] : i번째 파일부터 j번째 파일까지 합치는 최소비용
table[i][j] = min(table[i][t]+table[t+1][j]+sum[i:j])
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,data):
    _sum = [0] * n
    for i in range(n):
        if i==0:
            _sum[0] = data[0]
        else:
            _sum[i] = _sum[i-1] + data[i]

    table = [[0]*n for _ in range(n)]

    for term in range(1,n):
        for start in range(n):
            if start+term==n:
                break

            table[start][start+term] = int(1e9)

            for t in range(start,start+term):
                if start>0:
                    table[start][start+term] = min(table[start][start+term],
                                                table[start][t]+table[t+1][start+term]+_sum[start+term]-_sum[start-1])
                else:
                    table[start][start+term] = min(table[start][start+term],
                                                   table[start][t]+table[t+1][start+term]+_sum[start+term])

    return table[0][n-1]

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    print(solution(n,data))