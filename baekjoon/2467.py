# 2467

'''
a => -a의 위치 이진탐색 후 최솟값 갱신
'''

import sys
from bisect import bisect_left,bisect_right
input = lambda : sys.stdin.readline().rstrip()

def check(checklist):
    global _min,_minval

    for a,b in checklist:
        if a==b:
            continue
        if abs(a+b)<_min:
            _minval = (min(a,b),max(a,b))
            _min = abs(a+b)

def solution(data):
    global _min,_minval
    dataset = set(data)
    _min = 2*int(1e9)+1
    _minval = (-1,1)

    for i,a in enumerate(data):
        if a!=0 and -a in dataset:
            print(min(-a,a),max(-a,a))
            return
        
        index = bisect_left(data,-a)
        if index==0:
            check([(a,data[0])])
        elif index==n:
            check([(a,data[n-1])])
        else:
            check([(a,data[index-1]),(a,data[index])])

    print(_minval[0],_minval[1])
    
n = int(input())
data = list(map(int,input().split()))

solution(data)