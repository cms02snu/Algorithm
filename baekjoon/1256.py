# 1256

'''
a x n / z x m
k > (n-1+m,m) : 맨앞자리수 z , k -= (n-1+m,m), m-=1
k <= (n-1+m,m) : 맨앞자리수 a, n-=1
n이나 m 둘중하나 0 되면 종료
'''

def C(n,m):
    m = min(m,n-m)
    result = 1
    for i in range(m):
        result *= n-i
    for i in range(1,m+1):
        result = result//i

    return result

def solution(n,m,k):
    if C(n+m,n)<k:
        return -1
    
    result = ''

    while n>0 and m>0:
        if k>C(n-1+m,m):
            result += 'z'
            k -= C(n-1+m,m)
            m -= 1
        else:
            result += 'a'
            n -= 1
            
    result += 'a'*n 
    result += 'z'*m

    return result

n,m,k = map(int,input().split())
print(solution(n,m,k))