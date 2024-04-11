# 1647

import sys
input = lambda : sys.stdin.readline().rstrip()

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

def solution(edges):
    global parent
    edges.sort()
    parent = list(range(n))
    count = 0
    result = 0

    for cost,a,b in edges:
        if count==n-2:
            break
        if find_parent(parent,a)!=find_parent(parent,b):
            union(a,b)
            count += 1
            result += cost

    return result

n,m = map(int,input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a-1,b-1))

print(solution(edges))