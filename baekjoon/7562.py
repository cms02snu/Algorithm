# 7562

from collections import deque

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

def solution(i,j,ni,nj):
    dist = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append((i,j))
    dist[i][j] = 0

    while queue:
        x,y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if dist[nx][ny]==-1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))

    return dist[ni][nj]

for _ in range(int(input())):
    n = int(input())
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    print(solution(start_x,start_y,end_x,end_y))