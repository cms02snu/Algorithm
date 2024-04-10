# 14003

from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    array = [data[0]]
    table = [(0,0) for _ in range(n)]
    table[0] = (0,data[0])

    for i,a in enumerate(data):
        if i==0:
            continue

        if a>array[-1]:
            array.append(a)
            table[i] = (len(array)-1,a)
        else:
            idx = bisect_left(array,a)
            array[idx] = a
            table[i] = (idx,a)

    k = len(array)-1
    result = []

    for i in range(n-1,-1,-1):
        if table[i][0]==k:
            result.append(str(table[i][1]))
            k -= 1

    print(len(array))
    print(' '.join(result[::-1]))   

n = int(input())
data = list(map(int,input().split()))

solution(data)