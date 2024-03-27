# 19238

'''
만약 특정 위치로 택시가 이동할 수 없는경우
move 함수에서 -1을 return
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_next_pass(taxi_loc,passengers,graph):
    if taxi_loc in passengers:
        x,y = taxi_loc
        nx,ny = passengers[(x,y)]
        return x,y,nx,ny,0
    
    queue = deque()
    queue.append(taxi_loc)
    dist = [[-1]*n for _ in range(n)]
    dist[taxi_loc[0]][taxi_loc[1]] = 0
    result = []

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]==0 and dist[nx][ny]==-1:
                    if (nx,ny) in passengers:
                        result.append((dist[x][y]+1,nx,ny))
                    queue.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1

    if not result:
        return -1,-1,-1,-1,-1
    
    result.sort()
    
    d,x,y = result[0]
    nx,ny = passengers[(x,y)]
    return x,y,nx,ny,d  

def move(start,end,graph):
    if start==end:
        return 0
    
    queue = deque()
    dist = [[0]*n for _ in range(n)]
    queue.append(start)

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if (nx,ny)==end:
                    return dist[x][y] + 1
                if graph[nx][ny]==0 and dist[nx][ny]==0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))

    return -1

def solution(graph,fuel,start,passengers):
    taxi_loc = start
    while passengers:
        x,y,nx,ny,d = find_next_pass(taxi_loc,passengers,graph)
        if d==-1 or d>fuel:
            return -1
        fuel -= d

        d = move((x,y),(nx,ny),graph)
        if d==-1 or d>fuel:
            return -1
        passengers.pop((x,y))
        fuel += d
        taxi_loc = (nx,ny)

    return fuel

n,m,fuel = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
x,y = map(int,input().split())
start = (x-1,y-1)
passengers = {}
for _ in range(m):
    a,b,c,d = map(int,input().split())
    passengers[(a-1,b-1)] = (c-1,d-1)

print(solution(graph,fuel,start,passengers))