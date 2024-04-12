# 1005

'''
bilinear : 먼저 지어야 하는 건물의 개수
graph : 나중에 지어야 하는 건물의 리스트
start : 건물 짓기 시작한 시간
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(build,bilinear,graph,target):
    queue = deque()
    start = [-1] * n
    for i in range(n):
        if bilinear[i]==0:
            start[i] = 0
            queue.append(i)

    while queue:
        x = queue.popleft()
        if x==target:
            return start[target] + build[target]
        
        for nx in graph[x]:
            bilinear[nx] -= 1
            if start[nx]==-1:
                start[nx] = start[x] + build[x]
            else:
                start[nx] = max(start[nx],start[x]+build[x])
            if bilinear[nx]==0:
                queue.append(nx)

for _ in range(int(input())):
    n,k = map(int,input().split())
    build = list(map(int,input().split()))
    bilinear = [0] * n
    graph = [[] for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        bilinear[b-1] += 1
        graph[a-1].append(b-1)
    target = int(input())-1
    print(solution(build,bilinear,graph,target))
