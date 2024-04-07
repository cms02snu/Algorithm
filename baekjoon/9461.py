# 9461

'''
table[i] = table[i-1] + table[i-5]
'''

def solution(n):
    table = [0] * n
    table[0] = 1
    table[1] = 1
    table[2] = 1
    table[3] = 2
    table[4] = 2

    for i in range(5,n):
        table[i] = table[i-1] + table[i-5]

    return table        

t = int(input())
table = solution(100)
for _ in range(t):
    print(table[int(input())-1])