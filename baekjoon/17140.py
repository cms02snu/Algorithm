# 17140

def sort_arr(row):
    db = {}
    for a in row:
        if a==0:
            continue
        if a in db:
            db[a] += 1
        else:
            db[a] = 1

    temp = [(a,b) for a,b in db.items()]
    temp.sort(key=lambda x:(x[1],x[0]))
    new_row = []
    for a,b in temp:
        new_row.append(a)
        new_row.append(b)

    return new_row

def do_r(array):
    max_len = 0
    for i,row in enumerate(array):
        array[i] = sort_arr(row)
        max_len = max(len(array[i]),max_len)
    
    for i,row in enumerate(array):
        n = len(row)
        if n<max_len:
            array[i] = row + [0] * (max_len-n)

    return array

def do_c(array):
    row = len(array)
    col = len(array[0])
    mir_array = [[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            mir_array[j][i] = array[i][j]

    mir_array = do_r(mir_array)
    row = len(mir_array)
    col = len(mir_array[0])
    new_array = [[0]*row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            new_array[j][i] = mir_array[i][j]

    return new_array

def solution(array,r,c,k):
    time = 0
    n,m = 3,3
    while time<=100:
        if r<n and c<m:
            if array[r][c]==k:
                return time

        if n>=m:
            array = do_r(array)
        else:
            array = do_c(array)

        n = len(array)
        m = len(array[0])
        if n>100:
            array = array[:100]
        if m>100:
            array = [row[:100] for row in array]

        time += 1

    return -1

r,c,k = map(int,input().split())
r -= 1
c -= 1
array = []
for _ in range(3):
    array.append(list(map(int,input().split())))

print(solution(array,r,c,k))