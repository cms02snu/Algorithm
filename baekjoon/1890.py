# 1890

'''
table[i][j] : (i,j)에서 (n-1,n-1)까지 가는 방법의 수
table[x][y] = sum(table[nx][ny])

dp(x,y) : table[nx][ny]의 값들의 합으로 table[x][y] 값을 갱신
만약 table[nx][ny] 값이 갱신되지 않았다면 dp(nx,ny) 실행
'''

dx = [0,1]
dy = [1,0]

def dp(x,y):
    k = data[x][y]
    if k==0:
        table[x][y] = -1
        return

    for d in range(2):
        nx = x + k*dx[d]
        ny = y + k*dy[d]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if (nx,ny)==(n-1,n-1):
                table[x][y] += 1
                continue
            if table[nx][ny]==0:
                dp(nx,ny)
            if table[nx][ny]==-1:
                continue
            table[x][y] += table[nx][ny]

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
table = [[0]*n for _ in range(n)]

dp(0,0)

if table[0][0]==-1:
    print(0)
else:
    print(table[0][0])