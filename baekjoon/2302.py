# 2302

'''
n개의 자리 중 인접한 두자리씩 자리바꾸기 가능할 때 배치하는 총 경우의 수
1 - 1
2 - 2
3 - 3
4 - 5
table[i][0] : i번째 자리에 i가 오거나 i+1과 자리를 바꾸는 경우의 수
table[i][1] : i가 i-1이랑 자리를 바꾸는 경우의 수
table[i][0] = table[i-1][0] + table[i-1][1]
table[i][1] = table[i-1][0]
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(vip):
    table = [[0,0] for _ in range(40)]
    for i in range(40):
        if i==0:
            table[0] = [1,0]
        else:
            table[i][0] = table[i-1][0] + table[i-1][1]
            table[i][1] = table[i-1][0]

    result = 1
    count = 0
    for i in range(n):
        if i in vip:
            if count>0:
                result *= sum(table[count-1])
                count = 0
        else:
            count += 1
            if i==n-1:
                result *= sum(table[count-1])

    return result      

n = int(input())
m = int(input())
vip = []
for _ in range(m):
    vip.append(int(input())-1)

print(solution(vip))
