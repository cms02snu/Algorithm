# 1931

'''
가장 빨리 끝나는걸 하나 잡아. 그 다음에 그 이후로 시작하는거
중에 가장 빨리 끝나는걸 잡아. 반복해.
'''

import sys

input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    count = 0
    curr_end = 0
    data.sort(key=lambda x:(x[1],x[0]))

    for start,end in data:
        if start>=curr_end:
            curr_end = end
            count += 1
    
    return count

n = int(input())
data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

print(solution(data))
