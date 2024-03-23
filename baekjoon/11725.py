# 11725

from collections import deque

def solution(edges):
    parent = [0]*(n+1)

    queue = deque()
    queue.append(1)

    while queue:
        x = queue.popleft()
        for nx in edges[x]:
            if parent[nx]==0:
                parent[nx] = x
                queue.append(nx)

    for par in parent[2:]:
        print(par)

n = int(input())
edges = {}
for i in range(1,n+1):
    edges[i] = []
for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

solution(edges)