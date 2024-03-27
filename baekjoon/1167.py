# 1167

import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(x,d):
    global dist,far
    visited[x] = True
    last = True
    
    for nx,nd in edges[x]:
        if not visited[nx]:
            dfs(nx,d+nd)
            last = False

    if last:
        if d>dist:
            dist = d
            far = x

def solution(edges):
    global dist,far,visited
    dist = 0
    far = -1
    visited = [False] * v
    dfs(0,0)

    start = far
    dist = 0
    far = -1
    visited = [False] * v
    dfs(start,0)

    return dist

v = int(input())
edges = [[] for _ in range(v)]
for _ in range(v):
    temp = list(map(int,input().split()))
    a = temp.pop(0)
    while True:
        b = temp.pop(0)
        if b==-1:
            break
        c = temp.pop(0)
        edges[a-1].append((b-1,c))

print(solution(edges)) 