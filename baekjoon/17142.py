# 17142

import itertools
import copy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def infect(graph,active):
    queue = deque()
    for i,j in active:
        queue.append((i,j))

    nonactive = set()

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]==-1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
                elif graph[nx][ny]=='*':
                    nonactive.add((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    
    max_time = 0
    for i in range(n):
        for j in range(n):
            if (i,j) not in nonactive:
                if graph[i][j]==-1:
                    return int(1e4)
                if type(graph[i][j]) is int:
                    max_time = max(max_time,graph[i][j])

    return max_time

def solution(graph,m):
    virus = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]==0:
                graph[i][j] = -1
            elif graph[i][j]==1:
                graph[i][j] = '-'
            else:
                graph[i][j] = '*'
                virus.append((i,j))

    min_time = int(1e4)
    for active in itertools.combinations(virus,m):
        temp = copy.deepcopy(graph)
        for i,j in active:
            temp[i][j] = 0
        min_time = min(min_time,infect(temp,active))
    
    if min_time==int(1e4):
        return -1
    else:
        return min_time

'''n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))'''

n,m = 7,3
graph = [
    [2,0,2,0,1,1,0],
    [0,0,1,0,1,0,0],
    [0,1,1,1,1,0,0],
    [2,1,0,0,0,0,2],
    [1,0,0,0,0,1,1],
    [0,1,0,0,0,0,0],
    [2,1,0,0,2,0,2]
]

print(solution(graph,m))