# 16956

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(data):
    meet = False
    for x in range(n):
        for y in range(m):
            if data[x][y]=='S':
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx>=0 and nx<n and ny>=0 and ny<m:
                        if data[nx][ny]=='W':
                            meet = True
    
    if meet:
        print(0)

    else:
        print(1)
        for i in range(n):
            for j in range(m):
                if data[i][j]=='.':
                    data[i][j] = 'D'
        for i in range(n):
            print(''.join(data[i]))
            
n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(input()))

solution(data)