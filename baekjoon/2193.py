#  2193

'''
table[i][k] : i번째가 k인 경우의 수
table[i][0] = sum(table[i-1])
table[i][1] = table[i-1][0]
'''

def solution(n):
    table = [[0]*2 for _ in range(n)]
    
    for i in range(n):
        if i==0:
            table[0][0] = 0
            table[0][1] = 1
        else:
            table[i][0] = table[i-1][0] + table[i-1][1]
            table[i][1] = table[i-1][0]
            
    return table[n-1][0] + table[n-1][1]

print(solution(int(input())))
