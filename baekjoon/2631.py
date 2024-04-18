# 2641

from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    array = []
    array.append(data[0])
    count = 1

    for a in data[1:]:
        if a>array[-1]:
            array.append(a)
            count += 1
        else:
            index = bisect_left(array,a)
            array[index] = a

    return n - count

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

print(solution(data))