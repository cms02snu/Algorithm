# 21736

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        if graph[i][j]=='I':
            start = (i,j)

visited = [[False]*m for _ in range(n)]
visited[start[0]][start[1]] = True
count = 0

queue = deque()
queue.append(start)
while queue:
    x,y = queue.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if not visited[nx][ny]:
                if graph[nx][ny]=='O':
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                elif graph[nx][ny]=='P':
                    count += 1
                    queue.append((nx,ny))
                    visited[nx][ny] = True

if count==0:
    print('TT')
else:
    print(count)