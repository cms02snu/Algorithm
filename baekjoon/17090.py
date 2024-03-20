# 17090

def move(x,y,d):
    if d=='U':
        return x-1,y
    if d=='R':
        return x,y+1
    if d=='D':
        return x+1,y
    if d=='L':
        return x,y-1

def solution(data):
    result = [[-1]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            x,y = i,j
            if result[x][y] in [0,1]:
                continue

            temp = {(x,y)}
            possible = False
            while True:
                nx,ny = move(x,y,data[x][y])
                if nx>=0 and nx<n and ny>=0 and ny<m:
                    if (nx,ny) in temp:
                        break
                    if result[nx][ny]==1:
                        possible = True
                        temp.add((nx,ny))
                        break
                    elif result[nx][ny]==0:
                        break
                    elif result[nx][ny]==-1:
                        temp.add((nx,ny))
                        x,y = nx,ny
                else:
                    possible = True
                    break
            
            temp = list(temp)
            if possible:
                for x,y in temp:
                    result[x][y] = 1
            else:
                for x,y in temp:
                    result[x][y] = 0      

    count = 0
    for i in range(n):
        for j in range(m):     
            if result[i][j]==1:
                count += 1

    return count           

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(input()))

print(solution(data))