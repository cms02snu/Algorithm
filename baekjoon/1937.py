# 1937

'''
table[i][j] : (i,j)에서 시작했을 때 이동하는 최대칸수
table[x][y] = max(table[nx][ny]) + 1
값이 큰 칸부터 갱신
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(data):
    temp = []
    for i in range(n):
        for j in range(n):
            temp.append((data[i][j],i,j))

    temp.sort(key=lambda x:-x[0])

    table = [[0] * n for _ in range(n)]

    for a,x,y in temp:
        _max = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]            
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if data[nx][ny]>a:
                    _max = max(_max,table[nx][ny])

        table[x][y] = _max + 1

    return max([max(row) for row in table])

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

print(solution(data))