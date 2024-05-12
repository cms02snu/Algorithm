# 1052

'''
1000000 5
524288(19) 262144(18) 131072(17) 65536(16) 16384(14) 512(9) 64(6)
2**14 - 2**9 - 2**6
'''

def power(i):
    if i==0:
        return 1
    
    if i==1:
        return 2
    
    if i%2==0:
        k = power(i//2)
        return k*k
    
    if i%2==1:
        k = power(i//2)
        return k*k*2

def expo(n):
    result = []
    i = 23
    while True:
        x = power(i)
        if n>=x:
            result.append(i)
            n -= x
            if n==0:
                break
        i -= 1

    return result

def solution(n,k):
    ex = expo(n)
    if len(ex)<=k:
        return 0
    
    result = power(ex[k-1])

    for i in range(k,len(ex)):
        result -= power(ex[i])

    return result

n,k = map(int,input().split())
print(solution(n,k))