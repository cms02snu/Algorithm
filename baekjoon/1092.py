# 1092

'''
크레인별로 들 수 있는 최대무게 박스 옮기기
큰 크레인부터 옮기기
가장 큰 크레인이 들수있는 박스 없을시 종료
'''

from bisect import bisect_left,bisect_right
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(crane,box):
    crane.sort(key=lambda x: -x)
    box.sort()

    if crane[0]<box[0]:
        return -1

    _time = 0

    while True:
        if not box:
            break
        if crane[0]<box[0]:
            return -1

        for a in crane:
            if not box:
                continue
            if a<box[0]:
                continue
            index = bisect_right(box,a)-1
            box.pop(index)

        _time += 1

    return _time

n = int(input())
crane = list(map(int,input().split()))
m = int(input())
box = list(map(int,input().split()))

print(solution(crane,box))