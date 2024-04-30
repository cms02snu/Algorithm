# 2143

def sub(n,data):
    temp = [0] * n
    for i in range(n):
        if i==0:
            temp[0] = data[0]
        else:
            temp[i] = temp[i-1] + data[i]

    result = [[0]*n for _ in range(n)]

    for j in range(n):
        for i in range(j+1):
            if i==0:
                result[0][j] = temp[j]
            else:
                result[i][j] = temp[j] - temp[i-1]

    return result

def solution(target,A,B,n,m):
    _sumA = sub(n,A)
    _sumB = sub(m,B)

    dbA = {}
    dbB = {}

    for j in range(n):
        for i in range(j+1):
            k = _sumA[i][j]
            if k in dbA:
                dbA[k] += 1
            else:
                dbA[k] = 1

    for j in range(m):
        for i in range(j+1):
            k = _sumB[i][j]
            if k in dbB:
                dbB[k] += 1
            else:
                dbB[k] = 1

    count = 0

    for a in dbA:
        if target-a in dbB:
            count += dbA[a] * dbB[target-a]

    return count

target = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

print(solution(target,A,B,n,m))