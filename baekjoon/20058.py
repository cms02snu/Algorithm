# 20058

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate(array):
    n = len(array)
    mir_array = [[0]*n for _ in range(n)]
    new_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mir_array[i][j] = array[j][i]
    for i in range(n):
        for j in range(n):
            new_array[i][j] = mir_array[i][n-1-j]

    return new_array

def merge_part(array):
    n = len(array)
    k = len(array[0][0])
    N = n*k
    result = [[0]*N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            for x in range(k):
                for y in range(k):
                    result[i*k+x][j*k+y] = array[i][j][x][y]

    return result

def part_rotate(ice,l):
    temp = [[0]*(2**(n-l)) for _ in range(2**(n-l))]
    for i in range(2**(n-l)):
        for j in range(2**(n-l)):
            temp[i][j] = [row[(2**l)*j:(2**l)*(j+1)] for row in ice[(2**l)*i:(2**l)*(i+1)]]
    
    for i in range(2**(n-l)):
        for j in range(2**(n-l)):
            temp[i][j] = rotate(temp[i][j])
    
    result = merge_part(temp)

    return result
    
def bigpart(ice):
    visited = [[False]*(2**n) for _ in range(2**n)]
    queue = deque()
    biggest = 0
    for i in range(2**n):
        for j in range(2**n):
            if visited[i][j] or ice[i][j]==0:
                continue
            count = 1
            visited[i][j] = True
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx>=0 and nx<2**n and ny>=0 and ny<2**n:
                        if ice[nx][ny]>0 and not visited[nx][ny]:
                            queue.append((nx,ny))
                            visited[nx][ny] = True
                            count += 1
            biggest = max(biggest,count)

    if biggest==1:
        return 0
    
    return biggest

def solution(n,ice,magic):
    temp = []
    for l in magic:
        ice = part_rotate(ice,l)
        for x in range(2**n):
            for y in range(2**n):
                if ice[x][y]==0:
                    continue
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx>=0 and nx<2**n and ny>=0 and ny<2**n:
                        if ice[nx][ny]>0:
                            count += 1
                if count<3:
                    temp.append((x,y))
        while temp:
            x,y = temp.pop(0)
            ice[x][y] -= 1

    _sum = 0
    for i in range(2**n):
        for j in range(2**n):
            _sum += ice[i][j]
    print(_sum)

    part = bigpart(ice)
    print(part)

n,q = map(int,input().split())
ice = []
for _ in range(2**n):
    ice.append(list(map(int,input().split())))
magic = list(map(int,input().split()))

solution(n,ice,magic)