# 16936

def d23(a):
    i,j = 0,0

    while True:
        if a%2!=0:
            break
        else:
            i += 1
            a //= 2

    while True:
        if a%3!=0:
            break
        else:
            j += 1
            a //=3

    return i,j

def solution(n,data):
    factor = []
    for a in data:
        i,j = d23(a)
        factor.append((a,i,j))

    factor.sort(key=lambda x: (x[1],-x[2]))

    result = []
    for a,_,_ in factor:
        result.append(str(a))

    return ' '.join(result)

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))