# 17352

'''
다리 순환하면서 섬 이은다음에 
parent가 다른 두 섬 아무거나 하나만 찾으면 됨
parent가 a인 섬, b인 섬 두개밖에 없을거고,
모든 섬은 두개 중 하나에 포함되며 각 섬의 아들들은
적어도 하나씩 있음
'''

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
    parent = list(range(n))

    for a,b in edges:
        if find_parent(parent,a)!=find_parent(parent,b):
            union(a,b)

    result = {}

    for i in range(n):
        x = find_parent(parent,i)
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]

    for i in result:
        print(result[i][0]+1,end=' ')

n = int(input())
edges = []
for _ in range(n-2):
    a,b = map(int,input().split())
    edges.append((a-1,b-1))

solution(edges)