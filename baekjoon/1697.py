# 1697

from collections import deque

def solution(s,e):
    queue = deque()
    queue.append(s)
    dist = [-1] * (2*max(s,e)+1)
    dist[s] = 0
    way = [1] * (2*max(s,e)+1)

    while queue:
        x = queue.popleft()
        if x-1>=0: 
            if dist[x-1]==-1:
                dist[x-1] = dist[x] + 1
                queue.append(x-1)
                way[x-1] = way[x]
            elif dist[x-1]==dist[x]+1:
                way[x-1] += way[x]
        if x+1<=2*e: 
            if dist[x+1]==-1:
                dist[x+1] = dist[x] + 1
                queue.append(x+1)
                way[x+1] = way[x]
            elif dist[x+1]==dist[x]+1:
                way[x+1] += way[x]
        if 2*x<=2*e: 
            if dist[2*x]==-1:
                dist[2*x] = dist[x] + 1
                queue.append(2*x)
                way[2*x] = way[x]
            elif dist[2*x]==dist[x]+1:
                way[2*x] += way[x]

    print(dist[e])
    print(way[e])

s,e = map(int,input().split())

solution(s,e)