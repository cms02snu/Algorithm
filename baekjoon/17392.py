# 17392

'''
n개의 약속들의 합 = S
S가 m-n 이상이면 우울 0
S가 m-n보다 작고 m-2n-1 이상이면 우울 S-(m-n)
S가 m-2n-1보다 작고 m-3n-2 이상이면 우울 S-(m-2n-1)
'''

n,m = map(int,input().split())
data = list(map(int,input().split()))

S = sum(data)

def solution(S,n,m):
    if S>=m-n:
        return 0
    
    result = 0
    count = 0
    coef = 1

    m -= S+n
    
    while m>0:
        m -= 1
        count += 1
        result += coef*coef
        if count==n+1:
            count = 0
            coef += 1

    return result

print(solution(S,n,m))