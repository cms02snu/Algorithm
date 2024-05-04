# 3020

'''
table[h] : h구간(h-1~h)에서 피해야 하는 장애물 개수
table[h] = table[h-1] - 높이가h-1인석순개수 + 높이가h-1인종유석개수
'''

def solution(data):
    table = [0] * h

    for i in range(h):
        if i==0:
            table[i] = n//2 + data[0][1]
        else:
            table[i] = table[i-1] - data[i][0] + data[i][1]

    count = 0
    _min = n

    for i in range(h):
        if table[i]<_min:
            _min = table[i]
            count = 1
        elif table[i]==_min:
            count += 1
        
    print(_min,count)

n,h = map(int,input().split())
data = [[0]*2 for _ in range(h+1)]
for i in range(n):
    k = int(input())
    if i%2==1:
        data[k][0] += 1
    else:
        data[h-k][1] += 1

solution(data)