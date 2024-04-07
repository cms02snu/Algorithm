# 2293

'''
table[i] : i원을 만들 수 있는 경우의 수
갱신방식 : 동전의 가치별로 바텀업 갱신
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(k,coin):
    table = [0] * (k+1)

    for c in coin:
        for i in range(k+1):
            if i<c:
                continue
            elif i==c:
                table[i] += 1
            else:
                if table[i-c]>0:
                    table[i] += table[i-c]

    return table[k]

n,k = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

print(solution(k,coin))