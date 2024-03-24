# 23288

'''
주사위의 상태를 담고있는 리스트 - dice
주사위를 굴리는 함수 - roll
(x,y)에서의 점수를 계산하는 함수 - score
'''

from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def score(graph,i,j):
    s = graph[i][j]
    count = 1
    queue = deque()
    queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==s:
                    queue.append((nx,ny))
                    count += 1

    return count * s

def roll(dice,d):
    if d==0:
        dice = [d[4],d[0],d[2],d[3],d[5],d[1]]
    if d==1:
        dice = [d[3],d[1],d[0],d[5],d[4],d[2]]
    if d==2:
        dice = [d[1],d[5],d[2],d[3],d[0],d[4]]
    if d==3:
        dice = [d[2],d[1],d[5],d[0],d[4],d[3]]

    return dice

def solution(k,graph):
    dice = [1,2,3,4,5,6]
    x,y = 0,0
    d = 1
    result = 0

    for _ in range(k):
        # step 1
        nx = x + dx[d]
        ny = y + dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            d = (d+2)%4
            nx = x + dx[d]
            ny = y + dy[d]

        # step 2
        result += score(graph,nx,ny)

        # step 3
        if dice[5]>graph[nx][ny]:
            d = (d+1)%4
        elif dice[5]<graph[nx][ny]:
            d = (d-1)%4
        
        x,y = nx,ny

    return result

n,m,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

print(solution(k,graph))