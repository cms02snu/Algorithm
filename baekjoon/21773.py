# 21773

'''
매 초마다 힙큐에서 우선순위가 크고 id가 작은 프로세스 뽑는다
뽑은 프로세스 우선순위 1 증가시키고 시간도 1 감소시키고 힙에 넣는다
'''

import heapq

t,n = map(int,input().split())
h = []
for _ in range(n):
    a,b,c = map(int,input().split())
    heapq.heappush(h,(-c,a,b))

time = 0
while time<t and h:
    time += 1
    priority,_id,process = heapq.heappop(h)
    print(_id)
    if process>1:
        heapq.heappush(h,(priority+1,_id,process-1))
