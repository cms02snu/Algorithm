# 11504

'''
table[i][0] : i번째 수가 증가하는 수일 때 최대길이
table[i][1] : i번째 수가 감소하는 수일 때 최대길이
table[i][0] = max(table[j][0]) + 1 (data[j]<data[i])
table[i][1] = max(table[j][0],table[j][1]) + 1 (data[j]>data[i])
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    table = [[0,0] for _ in range(n)]
    table[0] = [1,0]

    for i in range(1,n):
        inc_max = 0
        dec_max = -1
        for j in range(i):
            if data[j]<data[i]:
                inc_max = max(inc_max,table[j][0])
            elif data[j]>data[i]:
                dec_max = max(dec_max,table[j][0],table[j][1])
        table[i][0] = inc_max + 1
        table[i][1] = dec_max + 1

    return max([max(row) for row in table])

n = int(input())
data = list(map(int,input().split()))
print(solution(data))