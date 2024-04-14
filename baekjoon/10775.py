# 10775

'''
분리집합 이용...
'''

def find_parent(parent,x):
    if x!=parent[x]:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union(a,b):
    par_a = find_parent(parent,a)
    par_b = find_parent(parent,b)

    if par_a<par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b

def solution(plane):
    global parent
    parent = list(range(g+1))
    count = 0

    for x in plane:
        par = find_parent(parent,x)
        if par==0:
            break
        else:
            union(par,par-1)
            count += 1

    return count

g = int(input())
p = int(input())
plane = []
for _ in range(p):
    plane.append(int(input()))

print(solution(plane))