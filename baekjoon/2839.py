# 2839

from collections import deque

def solution(n):
    db = [-1] * (5001)
    queue = deque()
    db[3] = 1
    db[5] = 1
    queue.append(3)
    queue.append(5)

    while queue:
        x = queue.popleft()
        for d in [3,5]:
            nx = x + d
            if nx<=n and db[nx]==-1:
                db[nx] = db[x] + 1
                queue.append(nx)

    return db[n]    

n = int(input())
print(solution(n))