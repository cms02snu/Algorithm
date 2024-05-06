# 2468

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sink):
    visited = [[False]*n for _ in range(n)]
    count = 0
    queue = deque()

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and not sink[i][j]:
                count += 1
                queue.append((i,j))
                visited[i][j] = True
                while queue:
                    x,y = queue.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx>=0 and nx<n and ny>=0 and ny<n:
                            if not sink[nx][ny] and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx,ny))

    return count

def solution(n,data):
    count = 1
    sink = [[False]*n for _ in range(n)]
    for h in range(1,101):
        for i in range(n):
            for j in range(n):
                if data[i][j]==h:
                    sink[i][j] = True
        count = max(count,bfs(sink))

    return count

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

print(solution(n,data))