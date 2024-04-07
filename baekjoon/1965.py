# 1965

'''
LIS
table[i] : i번째 상자안에 넣을 수 있는 상자개수의 최댓값
table[i] = max(table[j] (data[j]<data[i],j<i) ) + 1
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    table = [0] * n

    for i in range(n):
        if i==0:
            table[0] = 1
        else:
            temp = []
            for j in range(i):
                if data[j]<data[i]:
                    temp.append(table[j])
            if not temp:
                table[i] = 1
            else:
                table[i] = max(temp) + 1

    return max(table)

n = int(input())
data = list(map(int,input().split()))

print(solution(data))