# 2579

'''
table[i][j] : i번째 계단을 j번째연속으로 밟았을 때 점수의 최댓값
table[i][0] = max(table[i-2][0],table[i-2][1]) + data[i]
table[i][1] = table[i-1][0] + data[i]
'''

def solution(data):
    table = [[0,0] for _ in range(n)]

    for i in range(n):
        if i==0:
            table[0][0] = data[0]
            table[0][1] = 0
        elif i==1:
            table[1][0] = data[1]
            table[1][1] = data[0] + data[1]
        else:
            table[i][0] = max(table[i-2][0],table[i-2][1]) + data[i]
            table[i][1] = table[i-1][0] + data[i]

    return max(table[-1])

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

print(solution(data))