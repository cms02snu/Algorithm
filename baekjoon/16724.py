# 16724

'''
순환의 개수를 카운트한다
특정칸에서 시작해서 다른 순환 안거치고 자가순환 완료하면 순환개수 +1
새로운 칸과 기존의 순환이 결합하면 새로운 칸들도 기존의 순환에 포함시킨다
기존의 순환과 현재의 경로를 구분해야 한다

data : n*m list / 순환 및 현재 경로관련 정보 저장
-1 : 아직 방문안함
음이아닌정수: i번째 순환으로 방문함(i!=result)

dfs : 자가 순환 완성시 True return
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

dir= {'D':(1,0),'L':(0,-1),'U':(-1,0),'R':(0,1)}

def dfs(start,data,graph,i):
    x,y = start
    while True:
        data[x][y] = i
        d = graph[x][y]
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if data[nx][ny]==-1:
            x,y = nx,ny
        elif data[nx][ny]==i:
            return True
        else:
            return False

def solution(graph):
    data = [[-1]*m for _ in range(n)]
    count = 0
    result = 0

    for i in range(n):
        for j in range(m):
            if data[i][j]==-1:
                cycle = dfs((i,j),data,graph,count)
                if cycle:
                    result += 1
                count += 1

    return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

print(solution(graph))