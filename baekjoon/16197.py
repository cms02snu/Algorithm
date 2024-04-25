# 16197

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(coin,count):
    global result

    for d in range(4):
        next_coin = [coin[0],coin[1]]
        fall = [False,False]
        for i,(x,y) in enumerate(coin):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                fall[i] = True
            else:
                if graph[nx][ny]=='.':
                    next_coin[i] = (nx,ny)
        
        if fall==[True,True]:
            continue
        if fall==[True,False] or fall==[False,True]:
            result = min(count+1,result)
            continue
        if count<9:
            dfs(next_coin,count+1)         

def solution(graph):
    global result
    result = int(1e9)

    coin = []

    for i in range(n):
        for j in range(m):
            if graph[i][j]=='o':
                coin.append((i,j))
                graph[i][j] = '.'

    dfs(coin,0)

    if result==int(1e9):
        return -1
    else:
        return result      

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

print(solution(graph))