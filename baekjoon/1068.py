# 1068

'''
delete : 제거여부 저장 리스트
child : 각 노드의 자식 저장 리스트
indegree : 자식 수 저장 리스트

child 이용해서 제거노드 자손들 싹다 제거
indegree 0이고 delete 되지 않은 노드 개수 체크
'''

from collections import deque

def solution(n,parent,del_node):
    delete = [False] * n
    child = [[] for _ in range(n)]
    indegree = [0] * n
    for i,p in enumerate(parent):
        if p!=-1:
            child[p].append(i)
            indegree[p] += 1
        if i==del_node:
            indegree[p] -= 1

    queue = deque()
    queue.append(del_node)
    delete[del_node] = True

    while queue:
        x = queue.popleft()
        for nx in child[x]:
            queue.append(nx)
            delete[nx] = True

    count = 0

    for i in range(n):
        if indegree[i]==0 and not delete[i]:
            count += 1

    return count     

n = int(input())
parent = list(map(int,input().split()))
del_node = int(input())

print(solution(n,parent,del_node))