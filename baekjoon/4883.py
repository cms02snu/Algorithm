# 4883

'''
table[i][0,1,2] : (i,j)오는 최솟값
'''

def solution(n,data):
    table = [[0]*3 for _ in range(n)]
    
    for i in range(n):
        if i==0:
            table[0][0] = int(1e9)
            table[0][1] = data[0][1]
            table[0][2] = data[0][2] + data[0][1]
        else:
            table[i][0] = min(table[i-1][0],table[i-1][1]) + data[i][0]
            table[i][1] = min(table[i][0],min(table[i-1])) + data[i][1]
            table[i][2] = min(table[i][1],table[i-1][1],table[i-1][2]) + data[i][2]
            
    return table[n-1][1]
    
t = 0
while True:
    t += 1
    n = int(input())
    if n==0:
        break
    data = []
    for _ in range(n):
        data.append(list(map(int,input().split())))
    print(f'{t}. {solution(n,data)}')
