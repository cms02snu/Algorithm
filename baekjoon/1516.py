# 1516

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(indegree,graph,build):
    result = [0] * n
    prev = [0] * n
    queue = deque()
    for i in range(n):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result[x] = prev[x] + build[x]
        for nx in graph[x]:
            indegree[nx] -= 1
            prev[nx] = max(prev[nx],result[x])
            if indegree[nx]==0:
                queue.append(nx)

    for a in result:
        print(a)       

n = int(input())
indegree = [0] * n
graph = [[] for _ in range(n)]
build = []
for i in range(n):
    temp = list(map(int,input().split()))
    build.append(temp[0])
    for a in temp[1:-1]:
        graph[a-1].append(i)
        indegree[i] += 1

solution(indegree,graph,build)