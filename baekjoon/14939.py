# 14939

'''
greedy하게 완전탐색
첫째줄의 전구를 키고끄는 모든 경우의 수 1024개에 대하여
둘째줄 부터 다음의 알고리즘 반복
체크하는 칸 기준 윗칸이 켜져있으면 버튼 누른다
윗칸이 켜져있으면 밑에칸 버튼을 반드시 눌러야 모든 전구를 끌 수 있다.
'''

import copy,sys
input = lambda : sys.stdin.readline().rstrip()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def press(temp,x,y):
    temp[x][y] = (temp[x][y]+1)%2
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx>=0 and nx<10 and ny>=0 and ny<10:
            temp[nx][ny] = (temp[nx][ny]+1)%2

def solution(graph):
    result = [101] * (1<<10)

    for case in range(1<<10):
        temp = copy.deepcopy(graph)
        count = 0
        
        for j in range(10):
            if (1<<j) & case:
                press(temp,0,j)
                count += 1

        for i in range(1,10):
            for j in range(10):
                if temp[i-1][j]:
                    press(temp,i,j)
                    count += 1

        off = True
        for j in range(10):
            if temp[9][j]:
                off = False
                break

        if off:
            result[case] = count

    if min(result)==101:
        return -1
    else:
        return min(result)

data = []
for _ in range(10):
    data.append(list(input()))

graph = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if data[i][j]=='O':
            graph[i][j] = 1

print(solution(graph))