# 11660

def solution(data,mission):
    table = [[0]*n for _ in range(n)]
    table[0][0] = data[0][0]
    for i in range(1,n):
        table[i][0] = table[i-1][0] + data[i][0]
    for j in range(1,n):
        table[0][j] = table[0][j-1] + data[0][j]
    
    for i in range(1,n):
        for j in range(1,n):
            table[i][j] = data[i][j] + table[i-1][j] + table[i][j-1] - table[i-1][j-1]

    for x0,y0,x1,y1 in mission:
        if x0>0 and y0>0:
            print(table[x1][y1]-table[x1][y0-1]-table[x0-1][y1]+table[x0-1][y0-1])
        elif x0==0 and y0>0:
            print(table[x1][y1]-table[x1][y0-1])
        elif x0>0 and y0==0:
            print(table[x1][y1]-table[x0-1][y1])
        else:
            print(table[x1][y1])


n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
mission = []
for _ in range(m):
    a,b,c,d = map(int,input().split())
    mission.append((a-1,b-1,c-1,d-1))

solution(data,mission)