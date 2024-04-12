# 2623

'''
topology sort
bilinear 0인거 없으면 실패
bilinear : 반드시 앞에 와야 하는 가수 수
graph : 반드시 뒤에 오는 가수 list
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(priority):
    bilinear = [0] * n
    graph = [[] for _ in range(n)]
    for num,P in priority:
        for i in range(num):
            bilinear[P[i]-1] += i
            for j in range(i+1,num):
                graph[P[i]-1].append(P[j]-1)

    queue = deque()
    for i in range(n):
        if bilinear[i]==0:
            queue.append(i)

    result = []

    while queue:
        x = queue.popleft()
        result.append(x)
        for nx in graph[x]:
            bilinear[nx] -= 1
            if bilinear[nx]==0:
                queue.append(nx)

    if len(result)==n:
        for a in result:
            print(a+1)
    else:
        print(0)

n,m = map(int,input().split())
priority = []
for _ in range(m):
    temp = list(map(int,input().split()))
    priority.append((temp[0],temp[1:]))

solution(priority)