# 10211

'''
table[i] = table[i-1] + data[i] if table[i-1]>0
table[i] = data[i] else
'''

def solution(n,data):
    table = [-1] * n
    table[0] = data[0]

    for i in range(1,n):
        if table[i-1]>0:
            table[i] = table[i-1] + data[i]
        else:
            table[i] = data[i]

    return max(table)

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    print(solution(n,data))