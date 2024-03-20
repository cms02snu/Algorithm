# 4307

def solution(l,data):
    data.sort()
    temp = [min(a,l-a) for a in data]
    m = max(temp)

    a = data[0]
    b = data[-1]

    M = max(b,l-a)

    print(m,end=' ')
    print(M)

for _ in range(int(input())):
    l,n = map(int,input().split())
    data = []
    for _ in range(n):
        data.append(int(input()))
    solution(l,data)