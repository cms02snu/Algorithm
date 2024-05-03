# 15717

'''
f(n) = 2**(n-1)
거듭제곱알고리즘 사용
'''

import sys
sys.setrecursionlimit(int(1e2))

q = int(1e9) + 7

def power(n):
    if n==0:
        return 1

    if n==1:
        return 2
    
    if n%2==0:
        k = power(n//2)
        return (k*k)%q
    
    if n%2==1:
        k = power(n//2)
        return (2*k*k)%q

n = int(input())
if n==0:
    print(1)
else:   
    print(power(n-1))