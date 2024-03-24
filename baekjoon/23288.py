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
    visited = set()
    visited.add((i,j))

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if graph[nx][ny]==s and (nx,ny) not in visited:
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                    count += 1

    return count * s

def roll(dice,d):
    if d==0:
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    if d==1:
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    if d==2:
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    if d==3:
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]

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

        dice = roll(dice,d)

        # step 2
        result += score(graph,nx,ny)

        # step 3
        if dice[5]>graph[nx][ny]:
            d = (d+1)%4
        elif dice[5]<graph[nx][ny]:
            d = (d-1)%4
        
        x,y = nx,ny

    return result

'''n,m,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))'''

n,m,k = 4,5,1000
graph = [
    [4,1,2,3,3],
    [6,1,1,3,3],
    [5,6,1,3,2],
    [5,5,6,5,5]
]

print(solution(k,graph))