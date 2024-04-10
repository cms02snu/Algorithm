# 2252

'''
topology sort
indegree[i] : 학생 i보다 반드시 앞에 서야 하는 학생 수
data[i] : 학생 i보다 반드시 뒤에 서야 하는 학생들의 list

처음에 indegree가 0인 학생들부터 큐에 넣는다
큐에서 학생들을 꺼내고 가장 뒤에 줄 세운다.
이 학생 뒤에 오는 학생들의 indegree를 하나씩 감소시킨다.
indegree가 감소된 학생 중 indegree가 0이 된 학생이 있으면 큐에 넣는다.
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(indegree,data):
    if n==1:
        print(1)
        return
    
    queue = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    lineup = []

    while queue:
        x = queue.popleft()
        lineup.append(x)
        for nx in data[x]:
            indegree[nx] -= 1
            if indegree[nx]==0:
                queue.append(nx)

    for a in lineup:
        print(a,end=' ')        

n,m = map(int,input().split())
indegree= [0]*(n+1)
indegree[0] = -1
data = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    indegree[b] += 1
    data[a].append(b)

solution(indegree,data)