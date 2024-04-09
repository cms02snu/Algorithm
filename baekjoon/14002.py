# 14002

'''
걍 table에 LIS 정보저장 하면되는거 아님?
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    if n==1:
        print(1)
        print(data[0])
        return

    table = [(0,0) for _ in range(n)]
    table[0] = (1,[data[0]])

    longestlength = 1
    longestlist = [data[0]]

    for i in range(1,n):
        _max = 0
        longest = []
        for j in range(i):
            if data[j]<data[i]:
                if table[j][0]>_max:
                    _max = table[j][0]
                    longest = table[j][1][:]
        longest.append(data[i])
        k = longest[:]
        table[i] = (_max+1,k)

        if table[i][0]>longestlength:
            longestlength = table[i][0]
            longestlist = table[i][1]

    print(longestlength)
    for i,a in enumerate(longestlist):
        if i==longestlength-1:
            print(a)
        else:
            print(a,end=' ')   

n = int(input())
data = list(map(int,input().split()))

solution(data)