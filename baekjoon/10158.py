# 10158

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

x = (p+t)//w
y = (q+t)//h

rx = bool(x%2)
ry = bool(y%2)

nx = (p+t)%w
ny = (q+t)%h

if rx:
    nx = abs(nx-w)
if ry:
    ny = abs(ny-h)

print(nx,ny)