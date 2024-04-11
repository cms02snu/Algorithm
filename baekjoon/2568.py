# 2568

'''
O(nlogn)으로 LIS 찾으면 됨
'''

from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

def lis(data):
    array = [data[0]]
    table = [[0,0] for _ in range(n)]
    table[0] = (0,data[0])
    len_array = 1

    for i,a in enumerate(data):
        if i==0:
            continue

        if a>array[-1]:
            array.append(a)
            table[i] = [len_array,a]
            len_array += 1
        else:
            index = bisect_left(array,a)
            array[index] = a
            table[i] = [index,a]

    k = len_array-1
    result = []
    for i in range(n-1,-1,-1):
        if table[i][0]==k:
            result.append(table[i][1])
            k -= 1

    return len_array,result[::-1]

def solution(data):
    data.sort(key=lambda x : x[1])
    data0 = [a for a,_ in data]

    l0,result0 = lis(data0)

    print(n-l0)
    temp = []
    s = set(result0)
    for a in data0:
        if a not in s:
            temp.append(a)
    temp.sort()
    for a in temp:
        print(a)

n = int(input())
data = []
for _ in range(n):
    a,b = map(int,input().split())
    data.append((a,b))

solution(data)