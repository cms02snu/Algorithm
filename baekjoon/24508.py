# 24508

def solution(k,t,A):
    if A==[0]*n:
        return 'YES'
    
    if sum(A)%k!=0:
        return 'NO'
    
    A.sort(key=lambda x:-x)
    m = sum(A)//k
    temp = A[m:]
    if sum(temp)<=t:
        return 'YES'
    else:
        return 'NO'

n,k,t = map(int,input().split())
A = list(map(int,input().split()))

print(solution(k,t,A))