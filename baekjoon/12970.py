# 12970

def solution(n,k):
    x = n//2
    if k>x*(n-x):
        return -1
    
    section = []

    for i in range(1,x+1):
        section.append(i*(n-i))

    for i in range(x):
        if k<=section[i]:
            d = i
            break

    result = 'A'*d
    right = k - d*(n-d-1)
    left = n - d - right - 1

    return result + 'B'*left + 'A' + 'B'*right

n,k = map(int,input().split())

print(solution(n,k))