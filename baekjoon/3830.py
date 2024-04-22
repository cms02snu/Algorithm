# 3830

'''
parent : i번째 노드의 부모와 부모와의 차이를 담은 리스트 (p, a_i - a_p)
find_parent : x번째 노드의 부모와 부모와의 차이를 갱신하는 함수
union : a와 b의 부모를 갱신하고 a와 b의 차이를 계산해서 갱신하는 함수
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e5))

def find_parent(parent,x):
    if x!=parent[x][0]:
        p,d = find_parent(parent,parent[x][0])
        parent[x] = (p,d+parent[x][1])

    return parent[x]

def union(a,b,w):
    par_a,d_a = find_parent(parent,a)
    par_b,d_b = find_parent(parent,b)

    if par_a<par_b:
        parent[par_b] = (par_a, d_a - d_b + w)
    else:
        parent[par_a] = (par_b, d_b - d_a - w)

while True:
    n,m = map(int,input().split())
    if n==0 and m==0: break
    parent = [(i,0) for i in range(n)]
    for _ in range(m):
        temp = list(input().split())
        if temp[0]=='!':
            a,b,w = map(int,temp[1:])
            a -= 1
            b -= 1
            if find_parent(parent,a)[0] != find_parent(parent,b)[0]:
                union(a,b,w)
        else:
            a,b = map(int,temp[1:])
            a -= 1
            b -= 1
            par_a,d_a = find_parent(parent,a)
            par_b,d_b = find_parent(parent,b)
            if par_a != par_b:
                print('UNKNOWN')
            else:
                print(d_b - d_a)
