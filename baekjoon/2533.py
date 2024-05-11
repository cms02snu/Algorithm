# 2533

'''
indegree가 0인것들 큐에 넣고 그 위에 노드 얼리 처리, 얼리노드 윗노드 indegree -1
큐에서 꺼낸 노드가 얼리라면 : 그냥 패스
윗노드가 얼리라면 : 그냥 패스
큐 빌때까지 반복
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(parent,indegree):
    early = [False] * n
    queue = deque()
    for i in range(n):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        if not early[x]:
            nx = parent[x]
            if nx!=-1 and not early[nx]:
                early[nx] = True
                if parent[nx]!=-1:
                    indegree[parent[nx]] -= 1
                    if indegree[parent[nx]]==0:
                        queue.append(parent[nx])

    return sum(early)           

n = int(input())
parent = [-1] * n
indegree = [0] * n
for _ in range(n-1):
    a,b = map(int,input().split())
    parent[max(a,b)-1] = min(a,b)-1
    indegree[min(a,b)-1] += 1

print(solution(parent,indegree))