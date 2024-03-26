# 1967

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e5))

def dfs(x,d):
    global far,dist
    visited[x] = True
    last = True

    for nx,nd in graph[x]:
        if not visited[nx]:
            dfs(nx,nd+d)
            last = False

    if last:
        if d>dist:
            dist = d
            far = x

def solution(graph):
    global far,dist,visited
    dist = 0
    far = -1
    visited = [False] * n
    dfs(0,0)

    start = far
    far = -1
    dist = 0
    visited = [False] * n
    dfs(start,0)

    return dist

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

print(solution(graph))