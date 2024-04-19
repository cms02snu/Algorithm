# 16946

'''
BFS
(x,y,wall,count)
visited : {(x,y,wall)}
첫번째 칸부터 반복문 진행
not visited 칸에 대해서만 진행
인접한 칸의 개수를 센다
이동할 때마다 wall이 0이 아니라면 wall result 갱신

result : 각 벽 index별 최대 인접칸 개수 저장

메모리 초과...
'''

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(graph):
    k = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='0':
                graph[i][j] = 0
            else:
                k += 1
                graph[i][j] = k

    visited = set()
    queue = deque()
    result = [0] * (k+1)

    for i in range(n):
        for j in range(m):
            if (i,j,graph[i][j]) not in visited:
                visited.add((i,j,graph[i][j]))
                queue.append((i,j,graph[i][j]))
                while queue:
                    x,y,wall = queue.popleft()
                    if wall>0:
                        result[wall] += 1
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if nx>=0 and nx<n and ny>=0 and ny<m:
                            if wall>0 and graph[nx][ny]>0:
                                continue
                            if (nx,ny,max(graph[nx][ny],wall)) not in visited:
                                visited.add((nx,ny,max(graph[nx][ny],wall)))
                                queue.append((nx,ny,max(graph[nx][ny],wall)))

    temp = []
    for i in range(n):
        s = ''
        for j in range(m):
            if graph[i][j]==0:
                s += '0'
            else:
                s += str(result[graph[i][j]])
        temp.append(s)

    for a in temp:
        print(a)

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

solution(graph)