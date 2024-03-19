# 1010

def solution(m,n):
    m = min(m,n-m)
    result = 1
    for i in range(n-m+1,n+1):
        result = result * i
    for i in range(1,m+1):
        result = result // i

    return result

for _ in range(int(input())):
    m,n = map(int,input().split())
    print(solution(m,n))