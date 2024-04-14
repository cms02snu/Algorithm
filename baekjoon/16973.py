# 16973

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y):
    # (x,y)로 움직이는게 가능한지 체크
    # (x,y)부터 (x+h-1,y+w-1) 구간합 0인지 1인지 체크

    if x==0 and y==0:
        temp = sum_graph[x+h-1][y+w-1]
    elif x==0:
        temp = sum_graph[x+h-1][y+w-1] - sum_graph[x+h-1][y-1]
    elif y==0:
        temp = sum_graph[x+h-1][y+w-1] - sum_graph[x-1][y+w-1]
    else:
        temp = sum_graph[x+h-1][y+w-1] - sum_graph[x+h-1][y-1] - sum_graph[x-1][y+w-1] + sum_graph[x-1][y-1]

    if temp>0:
        return False
    else:
        return True

def solution(graph,start,end):
    global sum_graph
    sum_graph = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                sum_graph[0][0] = graph[0][0]
            elif i==0:
                sum_graph[0][j] = sum_graph[0][j-1] + graph[0][j]
            elif j==0:
                sum_graph[i][0] = sum_graph[i-1][0] + graph[i][0]
            else:
                sum_graph[i][j] = sum_graph[i-1][j] + sum_graph[i][j-1] + graph[i][j] - sum_graph[i-1][j-1]

    visited = [[False]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<m and nx+h-1>=0 and nx+h-1<n and ny+w-1>=0 and ny+w-1<m:
                if not visited[nx][ny] and check(nx,ny):
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1

    if not visited[end[0]][end[1]]:
        return -1
    else:
        return dist[end[0]][end[1]]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
h,w,x0,y0,x1,y1 = map(int,input().split())
x0 -= 1
y0 -= 1
x1 -= 1
y1 -= 1

print(solution(graph,(x0,y0),(x1,y1)))