# 1086

'''
bottom up
dp(visited,r) : visited에 있는 숫자들을 사용해서 나머지가 r인 수를 만드는 경우의 수
dp(visited,r) : 안 쓴 숫자 확인 후 해당 숫자들에 대하여
dp(visited|x , r+r_x) 진행

r_visited : visited 별 자릿수 담은 리스트
r_power : 10**(최대자릿수+1) k로 나눈 나머지 담은 리스트
r_data : data k로 나눈 나머지 담은 리스트
'''

import math,sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,k,data):
    r10 = 10 % k
    r_data = []
    for i in range(n):
        r_data.append(data[i]%k)

    r_visited = [0] * (1<<n)
    temp = [len(str(a)) for a in data]

    for visited in range(1<<n):
        for i in range(n):
            if 1<<i & visited:
                r_visited[visited] += temp[i]

    M = sum(temp)
    r_power = [0] * M
    for p in range(M):
        if p==0:
            r_power[0] = 1
        else:
            r_power[p] = (r_power[p-1] * r10)%k      

    table = [[0]*k for _ in range(1<<n)]
    table[0][0] = 1

    for visited in range(1<<n):
        for next in range(n):
            if 1<<next & visited: continue
            for r in range(k):
                # rnext : data[next] * 10**l 나머지
                rnext = (r_data[next] * r_power[r_visited[visited]]) % k
                table[visited|1<<next][(r+rnext)%k] += table[visited][r]

    p = table[(1<<n)-1][0]
    q = sum(table[(1<<n)-1])
    g = math.gcd(p,q)

    print(f'{p//g}/{q//g}')

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
k = int(input())

solution(n,k,data)