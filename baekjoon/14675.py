# 14675

'''
하나의 정점과만 연결된 정점은 단절점이 아니다
모든 간선은 단절선이다
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        if len(graph[b])>1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")