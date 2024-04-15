# 17404

'''
table[i][a][b] : i번째칸을 a번째색으로, 0번째칸을 b번째 색으로 칠했을 때의 최소비용
if i<n-1: table[i][a][b] = table[i-1][a-1][b] + table[i-1][a+1][b]
if i==n-1,a!=b: table[n-1][a][b] = sum(table[n-2][x!=a][b])
'''

def solution(data):
    table = [[[int(1e9)]*3 for _ in range(3)] for _ in range(n)]

    for i in range(n):
        if i==0:
            for a in range(3):
                table[0][a][a] = data[0][a]
        elif i==n-1:
            for a in range(3):
                for b in range(3):
                    if a!=b:
                        table[n-1][a][b] = data[n-1][a] + min(table[n-2][(a+1)%3][b],table[n-2][(a-1)%3][b])
        else:
            for a in range(3):
                for b in range(3):
                    table[i][a][b] = data[i][a] + min(table[i-1][(a+1)%3][b],table[i-1][(a-1)%3][b])

    result = int(1e9)
    for a in range(3):
        for b in range(3):
            if table[n-1][a][b]>0:
                result = min(result,table[n-1][a][b])

    return result

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

print(solution(data))