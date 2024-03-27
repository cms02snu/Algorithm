# 2156

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    if n==1:
        return data[0]
    
    table = [[0]*2 for _ in range(n)]
    table[0][0] = data[0]
    table[0][1] = 0
    table[1][0] = data[1]
    table[1][1] = data[0] + data[1]

    for i in range(2,n):
        if i==2:
            table[2][0] = max(table[0]) + data[2]
            table[2][1] = table[1][0] + data[2]
        else:
            table[i][0] = max([max(row) for row in table[(i-3):(i-1)]]) + data[i]
            table[i][1] = table[i-1][0] + data[i]

    temp = [max(row) for row in table]

    return max(temp)        

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

print(solution(data))