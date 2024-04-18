# 1891

def f(k):
    x,y = 0,0
    for i in range(n):
        if k[n-1-i]=='1':
            dx,dy = 2**i,2**i
        elif k[n-1-i]=='2':
            dx,dy = -2**i,2**i
        elif k[n-1-i]=='3':
            dx,dy = -2**i,-2**i
        elif k[n-1-i]=='4':
            dx,dy = 2**i,-2**i

        x += dx
        y += dy

    return x,y

def g(x,y):
    result = ''
    for i in range(n-1,-1,-1):
        if x>0 and y>0:
            result += '1'
            dx,dy = -2**i,-2**i
        elif x<0 and y>0:
            result += '2'
            dx,dy = 2**i,-2**i
        elif x<0 and y<0:
            result += '3'
            dx,dy = 2**i,2**i
        elif x>0 and y<0:
            result += '4'
            dx,dy = -2**i,2**i

        x += dx
        y += dy

    return result           

def solution(k,dx,dy):
    x,y = f(k)
    x += 2*dx
    y += 2*dy

    if abs(x)>=2**n or abs(y)>2**n:
        return -1
    
    result = g(x,y)

    return result

n,k = input().split()
n = int(n)
dx,dy = map(int,input().split())

print(solution(k,dx,dy))
