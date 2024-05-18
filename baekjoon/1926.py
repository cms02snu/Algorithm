# 1926

from collections import deque

def solution(graph):
    dist = [-1] * n
    dist[0] = 0
    queue = deque()
    queue.append(0)

    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if dist[nx]==-1:
                dist[nx] = dist[x] + 1
                queue.append(nx)

    argmax = -1
    _max = 0
    count = 0
    for i in range(1,n):
        if dist[i]>_max:
            _max = dist[i]
            count = 1
            argmax = i+1
        elif dist[i]==_max:
            count += 1

    print(argmax,_max,count)

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

solution(graph)