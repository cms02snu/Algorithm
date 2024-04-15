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

    for x in range(1,n):
        for y in range(m):
            for d in range(3):
                t = max(table[x-1][y])
                if t!=-int(1e9):
                    table[x][y][0] = t + data[x][y]

                if y==0:
                    t = max(table[x][y+1][2],table[x][y+1][0])
                    if t!=-int(1e9):
                        table[x][y][2] = t + data[x][y]
                elif y==m-1:
                    t = max(table[x][y-1][1],table[x][y-1][0])
                    if t!=-int(1e9):
                        table[x][y][1] = t + data[x][y]
                else:
                    t = max(table[x][y-1][1],table[x][y-1][0])
                    if t!=-int(1e9):
                        table[x][y][1] = t + data[x][y]

                    t = max(table[x][y+1][2],table[x][y+1][0])
                    if t!=-int(1e9):
                        table[x][y][2] = t + data[x][y]

    print(table)

    return max(table[n-1][m-1])                  

'''n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))'''

n,m = 5,5
data = [
    [10,25,7,8,13],
    [68,24,-78,63,32],
    [12,-69,100,-29,-25],
    [-16,-22,-57,-33,99],
    [7,-76,-11,77,15]
]

print(solution(data))