# 15824

import sys
input = lambda : sys.stdin.readline().rstrip()

def power(a,k):
    if k==0:
        return 1
    if k==1:
        return a

    half = power(a,k//2)
    
    if k%2==0:
        return (half * half) % (int(1e9)+7)
    else:
        return (half * half * a) % (int(1e9)+7)

def solution(data):
    data.sort()
    result = 0
    for i,a in enumerate(data):
        result += a * (power(2,i)-power(2,n-i-1)) % (int(1e9)+7)

    return result % (int(1e9)+7)

n = int(input())
data = list(map(int,input().split()))

print(solution(data))