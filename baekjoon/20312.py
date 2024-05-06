# 20312

'''
a+b+c+ab+bc+abc
a(1+b+bc)+b(1+c)+c(1)

a+b+c+d+ab+bc+cd+abc+bcd+abcd
a(1+b+bc+bcd) + b(1+c+cd) + c(1+d) + d(1)

d + c(1+d) + b(1+c+cd) + a(1+b+bc+bcd)

dp[i] = data[i] * (dp[i-1]+1)
'''

N = int(1e9) + 7

def solution(n,data):
    data = data[::-1]
    table = [0] * (n-1)

    for i in range(n-1):
        if i==0:
            table[0] = data[0]
        else:
            table[i] = (data[i]*(table[i-1]+1))%N

    return sum(table)%N

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))