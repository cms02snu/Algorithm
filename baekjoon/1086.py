# 1086

'''
bottom up
dp(visited,r) : visited에 있는 숫자들을 사용해서 나머지가 r인 수를 만드는 경우의 수
dp(visited,r) : 안 쓴 숫자 확인 후 해당 숫자들에 대하여
dp(visited|x , r+r_x) 진행
'''

def dp(visited,r):
    for i in range(n):
        if not (1<<i) & visited:
            table[visited|1<<i][(r+remain[i])%k]



def solution(n,k,data):
    global table
    table = [[0]*k for _ in range(1<<n)]

    dp(0,0)

    a = dp[(1<<n)-1][0]

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
k = int(input())

print(solution(n,k,data))