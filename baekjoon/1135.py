# 1135

'''
- 직접 상사의 인덱스를 담은 리스트(입력) - parent
- 간접 부하의 수를 담은 리스트 - child_num
- 직접 부하의 인덱스를 담은 리스트 - child
- 도달 시간을 담은 리스트 - result

bfs로 위에서부터 진행
큐에서 x를 꺼내면, x의 직속 부하들의 도달 시간을 입력하고
해당 부하의 인덱스와 도달 시간을 tuple로 묶어 큐에 넣기
'''

from collections import deque

def count_child_num(child):
    child_num = [0] * n
    child_num[0] = n-1
    queue = deque()
    for i in range(1,n):
        queue.append(i)
        count = 0
        while queue:
            x = queue.popleft()
            for nx in child[x]:
                queue.append(nx)
                count += 1
        child_num[i] = count

    return child_num

def solution(parent):
    child = [[] for _ in range(n)]
    for i,par in enumerate(parent):
        if i==0:
            continue
        child[par].append(i)

    child_num = count_child_num(child)
    print(child)
    print(child_num)
    result = [0]*n

    queue = deque()
    queue.append(0)
    while queue:
        x = queue.popleft()
        temp = [(-child_num[i],i) for i in child[x]]
        temp.sort()
        for j,(_,i) in enumerate(temp):
            result[i] = result[x]+j+1
            queue.append((i))
    print(result)
    return max(result)

'''n = int(input())
parent = list(map(int,input().split()))'''
n = 15
parent = [-1,0,0,0,0,2,2,3,3,6,7,7,4,12,13]

print(solution(parent))