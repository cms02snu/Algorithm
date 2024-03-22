# 1513

'''
dp(i,j,p,q) : (i,j)칸에 p개의 오락실을 거치고
q번째 오락실을 마지막으로 거쳐서 오는 경우의 수
if graph[i][j]==0:
    dp(i,j,a,b) = dp(i-1,j,a,b) + dp(i,j-1,a,b)
if graph[i][j]>0:
    a<v = graph[i][j]<b
    dp(i,j,0,v) = 0
    dp(i,j,p,v) = dp(i-1,j,p-1,0:v) + dp(i,j-1,p-1,0:v)
    dp(i,j,p,a) = 0
    dp(i,j,p,v) = 0
'''

def solution(game,c):
    graph = [[0]*m for _ in range(n)]
    for i,(x,y) in enumerate(game):
        graph[x][y] = i+1

    table = [[[[0]*(c+1) for _ in range(c+1)] for _ in range(m)] for _ in range(n)]
    if graph[0][0]==0:
        table[0][0][0][0] = 1
    else:
        table[0][0][1][graph[0][0]] = 1

    for i in range(1,n):
        for p in range(c+1):
            for q in range(c+1):
                if graph[i][0]==0:
                    table[i][0][p][q] = table[i-1][0][p][q]
                else:
                    if q==graph[i][0]:
                        temp = table[i-1][0][p-1][0:graph[i][0]]
                        table[i][0][p][q] = sum(temp)
                    else:
                        table[i][0][p][q] = 0

    for j in range(1,m):
        for p in range(c+1):
            for q in range(c+1):
                if graph[0][j]==0:
                    table[0][j][p][q] = table[0][j-1][p][q]
                else:
                    if q==graph[0][j]:
                        temp = table[0][j-1][p-1][0:graph[0][j]]
                        table[0][j][p][q] = sum(temp)
                    else:
                        table[0][j][p][q] = 0

    for i in range(1,n):
        for j in range(1,m):
            if graph[i][j]==0:
                for p in range(c+1):
                    for q in range(c+1):
                        table[i][j][p][q] = table[i][j-1][p][q] + table[i-1][j][p][q]
            else:
                for p in range(c+1):
                    for q in range(c+1):
                        if q==graph[i][j]:
                            temp0 = table[i][j-1][p-1][0:q]
                            temp1 = table[i-1][j][p-1][0:q]
                            table[i][j][p][q] = sum(temp0) + sum(temp1)
                        else:
                            table[i][j][p][q] = 0

    result =  [sum(row) for row in table[n-1][m-1]]
    for x in result:
        print(x%1000007,end=' ')

n,m,c = map(int,input().split())
game = []
for _ in range(c):
    a,b = map(int,input().split())
    game.append((a-1,b-1))

solution(game,c)