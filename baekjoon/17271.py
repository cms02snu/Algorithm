# 17271

'''
p = N//M
M을 p번까지 사용가능

M을 k(<=p)번 사용하는 경우의 수 (A = N-KM)
com(A+k,k) = com(N-K(M-1),k)
'''

A = int(1e9) + 7

def combination(n,r):
    r = min(r,n-r)

    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    for i in range(1,r+1):
        result //= i

    return result%A

def solution(n,m):
    p = n//m
    result = 0
    for i in range(p+1):
        result += combination(n-i*(m-1),i)
        result = result

    return result%A

n,m = map(int,input().split())
print(solution(n,m))