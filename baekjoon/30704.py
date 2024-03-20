# 30704

def find_x(x,r,c):
    while True:
        if r==c:
            if r*c<x<=(r+1)*c:
                return r,c
            else:
                r += 1
        if r==c+1:
            if r*c<x<=r*(c+1):
                return r,c
            else:
                c += 1

def solution(data):
    data = [(a,i) for i,a in enumerate(data)]
    data.sort()
    result = [-1] * t
    r = 1
    c = 0

    while data:
        x,i = data.pop(0)
        r,c = find_x(x,r,c)
        if r==c:
            result[i] = 2*(r+1+c)
        if r==c+1:
            result[i] = 2*(r+c+1)

    for a in result:
        print(a)

data = []
t = int(input())
for _ in range(t):
    data.append(int(input()))

solution(data)