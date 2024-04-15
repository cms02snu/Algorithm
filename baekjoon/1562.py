# 1562

'''
table[i][x][a][b] : i자리수,x로 끝나는,a~b로만 구성된 숫자 개수
if x==a:
table[i][x][a][b] = table[i-1][x-1][a][b] + table[i-1][x+1][a][b] + table[i-1][x+1][a+1][b]
if x==b:
table[i][x][a][b] = table[i-1][x-1][a][b] + table[i-1][x+1][a][b] + table[i-1][x-1][a][b-1]
else
table[i][x][a][b] = table[i-1][x-1][a][b] + table[i-1][x+1][a][b]
'''

def solution(n):
    table = [[[[0]*10 for _ in range(10)] for _ in range(10)] for _ in range(n)]

    for i in range(n):
        for x in range(10):
            for a in range(10):
                for b in range(10):
                    if i==0:
                        if x!=0 and x==a==b:
                            table[i][x][a][b] = 1
                    else:
                        if a>=b:
                            continue
                        if x==0:
                            if a==0:
                                table[i][0][0][b] = table[i-1][1][0][b] + table[i-1][1][1][b]
                        elif x==9:
                            if b==9:
                                table[i][9][a][9] = table[i-1][8][a][9] + table[i-1][8][a][8]
                        else:
                            if x==a:
                                table[i][x][x][b] = table[i-1][x+1][x][b] + table[i-1][x+1][x+1][b]
                            elif x==b:
                                table[i][x][a][x] = table[i-1][x-1][a][x] + table[i-1][x-1][a][x-1]
                            elif a<x<b:
                                table[i][x][a][b] = table[i-1][x-1][a][b] + table[i-1][x+1][a][b]

    result = 0
    for x in range(10):
        for a in range(10):
            for b in range(10):
                if a==0 and b==9:
                    result += table[n-1][x][0][9]

    return result % int(1e9)

n = int(input())

print(solution(n))