# 1939

'''
BFS
dist[i] : 시작부터 i번째 노드까지의 이동가능 최대중량
dist[nx] = max(dist[nx],min(dist[x],W(x->nx)))
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(graph,start,end):
    dist = [-1] * n
    dist[start] = int(1e9)

    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        for nx,w in graph[x]:
            if dist[nx]<min(dist[x],w):
                dist[nx] = min(dist[x],w)
                queue.append(nx)

    return dist[end]

n,m = map(int,input().split())
graph = [[] for _ in range(n)]
temp = {i:{} for i in range(n)}
for _ in range(m):
    a,b,c = map(int,input().split())
    if b-1 in temp[a-1]:
        temp[a-1][b-1] = max(temp[a-1][b-1],c)
    else:
        temp[a-1][b-1] = c
    if a-1 in temp[b-1]:
        temp[b-1][a-1] = max(temp[b-1][a-1],c)
    else:
        temp[b-1][a-1] = c

for i in temp:
    for a,b in temp[i].items():
        graph[i].append((a,b))

start,end = map(int,input().split())
start -= 1
end -= 1

print(solution(graph,start,end))