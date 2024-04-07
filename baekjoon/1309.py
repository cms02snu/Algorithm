# 1309

'''
table[i][0] : i번째 행에 사자를 배치하지 않는 경우의 수
table[i][j] : i번째 행에 j열에 사자를 배치하는 경우의 수
table[i][0] = sum(table[i-1])
table[i][1] = table[i-1][0] + table[i-1][2]
table[i][2] = table[i-1][0] + table[i-1][1]
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n):
    table = [[0]*3 for _ in range(n)]
    
    for i in range(n):
        if i==0:
            table[0] = [1,1,1]
        else:
            table[i][0] = sum(table[i-1]) % 9901
            table[i][1] = (table[i-1][0] + table[i-1][2]) % 9901
            table[i][2] = (table[i-1][0] + table[i-1][1]) % 9901

    return sum(table[n-1]) % 9901

n = int(input())
print(solution(n))