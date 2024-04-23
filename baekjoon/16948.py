# 16948

from collections import deque

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def solution(r1,c1,r2,c2):
    queue = deque()
    dist = [[-1]*n for _ in range(n)]
    queue.append((r1,c1))
    dist[r1][c1] = 0

    while queue:
        x,y = queue.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if dist[nx][ny]==-1:
                    queue.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1

    return dist[r2][c2]

n = int(input())
r1,c1,r2,c2 = map(int,input().split())

print(solution(r1,c1,r2,c2))