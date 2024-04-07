# 11000

'''
끝나는 시간순으로 정렬
빨리 끝나는 것부터 강의실에 넣기
현재 있는 강의실에 넣을 수 없으면 새 강의실에 넣기
여러 강의실에 넣을 수 있는 경우 늦게 끝나는 강의실부터 넣기

시작하는 시간순으로 정렬
일찍 시작하는것부터 강의실에 넣기
가장 일찍 끝나는거에 넣고 못넣으면 새 강의실에 넣기
'''

import sys,heapq
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    data.sort()
    h = []

    for start,end in data:
        if not h:
            heapq.heappush(h,end)
        else:
            if h[0]<=start:
                heapq.heappop(h)
            heapq.heappush(h,end)

    return len(h)

n = int(input())
data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

print(solution(data))