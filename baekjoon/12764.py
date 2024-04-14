# 12764

'''
컴퓨터 대수는 1부터 시작
아직 배치안한 사람의 (시작시간,-1)과 배치한 사람의 (종료시간,인덱스)를 힙큐에 저장
빈 컴퓨터 인덱스 힙큐로 저장
컴퓨터 별 사용한 사람 수 리스트로 저장

힙큐 바닥날때까지(모두 사용끝날때까지) 힙큐에 있는 순서대로 반복문 실행
만약 시작 사람이면 
- 비는 컴퓨터 중 가장 앞에 배치(heappop 사용)
- 없으면 컴퓨터 개수 늘리고 거따가 배치
- 종료시간 힙큐에 삽입
만약 종료 사람이면
- 비는 컴퓨터에 사용한 컴퓨터 인덱스 추가
- 컴퓨터 사용횟수 추가
'''

import heapq,sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    num_com = 1
    h = []
    empty = []
    used = []
    heapq.heappush(empty,0)
    used.append(0)
    
    for a in data:
        heapq.heappush(h,(a,-1))

    while h:
        t,i = heapq.heappop(h)
        if i==-1:
            if empty:
                c = heapq.heappop(empty)
                heapq.heappush(h,(data[t],c))
            else:
                heapq.heappush(h,(data[t],num_com))
                num_com += 1
                used.append(0)
        else:
            heapq.heappush(empty,i)
            used[i] += 1

    print(num_com)
    for a in used:
        print(a,end=' ')

n = int(input())
data = {}
for _ in range(n):
    a,b = map(int,input().split())
    data[a] = b

solution(data)