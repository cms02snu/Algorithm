# 1043

from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,m,truth,party,people):
    know = [False] * n
    queue = deque()
    for p in truth[1:]:
        queue.append(p-1)

    while queue:
        x = queue.popleft()
        know[x] = True
        for np in people[x]:
            for nx in party[np]:
                if not know[nx]:
                    queue.append(nx)

    count = 0
    for i in range(m):
        lie = True
        for p in party[i]:
            if know[p]:
                lie = False
                break
        if lie:
            count += 1

    return count     

n,m = map(int,input().split())
truth = list(map(int,input().split()))
party = [[] for _ in range(m)]
people = [[] for _ in range(n)]
for i in range(m):
    temp = list(map(int,input().split()))
    for p in temp[1:]:
        party[i].append(p-1)
        people[p-1].append(i)

print(solution(n,m,truth,party,people))