# 16680

import sys
input = lambda : sys.stdin.readline().rstrip()

def power(n,k):
    if k==0:
        return 1
    if k==1:
        return n
    x = power(n,k//2)
    if k%2==0:
        return x*x
    if k%2==1:
        return n*x*x      

def check(S):
    count = 0
    for a in S:
        if int(a)%2==1:
            count += 1

    if count%2==1:
        return True
    else:
        return False  
    
def d1(n):
    while True:
        if check(str(n)):
            return n
        n *= 2

def count0(S):
    count = 0
    for a in S[::-1]:
        if a=='0':
            count += 1
        else:
            break

    return count

def solution(S):
    if len(S)==1:
        return d1(int(S))
    
    while True:
        if check(S):
            return int(S)
        
        digit = len(S)
        count = count0(S)
        if int(S[0])+int(S[-count-1])>=10:
            x = int(S) * (power(10,digit-count-1)+1)
            if check(str(x)):
                return x
        
        S = str(int(S)*2)

for _ in range(int(input())):
    print(solution(input()))