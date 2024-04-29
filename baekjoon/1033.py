# 1033

'''
parent : (p,x)
p : parent 번호
x : parent와의 비율
x=1/3 : k = p * (1/3)
마지막에는 x값이 -인 것들의 최소공배수 구한다

0 1 : 1 3 parent[1] = (0,3)
2 3 : 1 2 parent[3] = (2,2)
union(1,3,5,4)
parent[2] = (0,)

1 3 = 5:4
0 1 = 1:3
2 3 = 1:2
0 2 = 1: 3 * (4/5) * (1/2)
'''

import math

def gcd(data):
    if len(data)<2:
        return 1
    
    a = data.pop(0)
    b = data.pop(0)
    k = math.gcd(a,b)

    while data:
        x = data.pop(0)
        k = math.gcd(x,k)

    return k   

def find_parent(parent,x):
    if x!=parent[x]:
        p,a = find_parent(parent,parent[x][0])
        parent[x] = (p,a*parent[x][1])

    return parent[x]

def union(a,b,p,q):
    par_a,x_a = find_parent(parent,a)
    par_b,x_b = find_parent(parent,b)

    if par_a<par_b:
        parent[par_b] = (par_a,x_a*(q/p)*(1/x_b))
    else:
        parent[par_a] = (par_b,x_b*(p/q)*(1/x_a))

n = int(input())
parent = [(i,1) for i in range(n)]
for _ in range(n-1):
    a,b,x,y = map(int,input().split())
    union(a,b,x,y)

result = [1] * n
temp = []

for p,x in parent:
    if x<0:
        temp.append(-x)

k = gcd(temp)

for i in range(n):
    x = parent[i][1]
    if x>0:
        result[i] = result[i] * x
    else:
        for j in range(n):
            if j!=i:
                result[j] = result[j] * (-x)

for i in range(n):
    result[i] = str(result[i]//k)

print(' '.join(result))