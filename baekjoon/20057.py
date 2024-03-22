# 20057

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def tornado(n):
    seq = []
    x,y = n//2,n//2
    d = 0
    seq.append((x,y))
    go = 1
    dir_count = 0
    go_count = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        seq.append((nx,ny))
        if (nx,ny)==(0,0):
            break
        go_count += 1
        if go_count==go:
            go_count = 0
            dir_count += 1
            d = (d+1)%4
            if dir_count==2:
                dir_count = 0
                go += 1
        x,y = nx,ny

    return seq

def scatter(sand,end,d):
    out = 0
    x,y = end
    moves = []
    # 0.01
    nx = x + dx[(d+2)%4] + dx[(d+1)%4]
    ny = y + dy[(d+2)%4] + dy[(d+1)%4]
    moves.append((nx,ny,0.01))
    nx = x + dx[(d+2)%4] + dx[(d-1)%4]
    ny = y + dy[(d+2)%4] + dy[(d-1)%4]
    moves.append((nx,ny,0.01))
    # 0.02
    nx = x + 2 * dx[(d+1)%4]
    ny = y + 2 * dy[(d+1)%4]
    moves.append((nx,ny,0.02))
    nx = x + 2 * dx[(d-1)%4]
    ny = y + 2 * dy[(d-1)%4]
    moves.append((nx,ny,0.02))
    # 0.05
    nx = x + 2 * dx[d]
    ny = y + 2 * dy[d]
    moves.append((nx,ny,0.05))
    # 0.07
    nx = x + dx[(d+1)%4]
    ny = y + dy[(d+1)%4]
    moves.append((nx,ny,0.07))
    nx = x + dx[(d-1)%4]
    ny = y + dy[(d-1)%4]
    moves.append((nx,ny,0.07))
    # 0.1
    nx = x + dx[d] + dx[(d+1)%4]
    ny = y + dy[d] + dy[(d+1)%4]
    moves.append((nx,ny,0.1))
    nx = x + dx[d] + dx[(d-1)%4]
    ny = y + dy[d] + dy[(d-1)%4]
    moves.append((nx,ny,0.1))

    count = 0
    for nx,ny,p in moves:
        if nx>=0 and nx<n and ny>=0 and ny<n:
            sand[nx][ny] += int(sand[x][y]*p)
        else:
            out += int(sand[x][y]*p)
        count += int(sand[x][y]*p)

    nx = x + dx[d]
    ny = y + dy[d]
    if nx>=0 and nx<n and ny>=0 and ny<n:
        sand[nx][ny] += int(sand[x][y]-count)
    else:
        out += int(sand[x][y]-count)
    sand[x][y] = 0

    return sand,out

def solution(n,sand):
    moves = tornado(n)
    count = 0
    dir = [(0,-1),(1,0),(0,1),(-1,0)]

    for i in range(len(moves)-1):
        x,y = moves[i]
        nx,ny = moves[i+1]
        d = dir.index((nx-x,ny-y))
        sand,out = scatter(sand,(nx,ny),d)
        count += out

    return count

n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int,input().split())))

print(solution(n,sand))