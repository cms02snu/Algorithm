# 2169

'''
0 상 1 좌 2 우
table[i][j][d] : (i,j)에 d방향에서 왔을 때 탐사지역 가치 최댓값
table[2][2][1] = max(table[1][2][:],table[2][1][0,1]) + data[2][2]
table[0][3][0] = -int(1e9)

갱신방법 생각해봐야돼
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    table = [[[-int(1e9)]*3 for _ in range(m)] for _ in range(n)]
    table[0][0] = [data[0][0]] * 3
    
    for j in range(1,m):
        table[0][j][1] = table[0][j-1][1] + data[0][j]

    for x in range(1,n-1):
        for y in range(m):
            # 0부터 갱신
            t = max(table[x-1][y])
            if t!=-int(1e9):
                table[x][y][0] = t + data[x][y]

        for y in range(m):                
            # 1 갱신
            if y>0:
                table[x][y][1] = max(table[x][y-1][0],table[x][y-1][1]) + data[x][y]

        for y in range(m-1,-1,-1):
            # 2 갱신
            if y<m-1:
                table[x][y][2] = max(table[x][y+1][0],table[x][y+1][2]) + data[x][y]

    if n>1:
        for j in range(m):
            table[n-1][j][0] = max(table[n-2][j]) + data[n-1][j]
        for j in range(1,m):
            table[n-1][j][1] = max(table[n-1][j-1][0],table[n-1][j-1][1]) + data[n-1][j]

    return max(table[n-1][m-1])                  

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

print(solution(data))