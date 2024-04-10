# 12015

from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    array = [data[0]]

    for a in data[1:]:
        if a>array[-1]:
            array.append(a)
        else:
            idx = bisect_left(array,a)
            array[idx] = a

    return len(array)

n = int(input())
data = list(map(int,input().split()))

print(solution(data))