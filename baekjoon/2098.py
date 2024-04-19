# 2098

'''
"외판원 순회"
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def dfs(i,visited):
    if visited==(1<<n)-1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return int(1e9)
        
    if (i,visited) in dp:
        return dp[(i,visited)]
    
    min_cost = int(1e9)
    for next in range(1,n):
        if graph[i][next]>0 and not (visited & (1<<next)):
            cost = dfs(next,visited|(1<<next)) + graph[i][next]
            min_cost = min(min_cost,cost)
    
    dp[(i,visited)] = min_cost
    return min_cost

def solution(graph):
    global dp
    dp = {}
    return dfs(0,1)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

print(solution(graph))