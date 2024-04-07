# 2011

'''
table[i][0] : i번쨰 자리 단일해석,앞자리해석 경우의 수
table[i][1] : i번째 자리 뒷자리해석 경우의 수
table[i][0] = table[i-1][0] + table[i-1][1]
table[i][1] = (prev=1) table[i-1][0]
table[i][1] = (prev=2) table[i-1][0] or 0
table[i][1] = (else) 0
매번 i번째 숫자를 prev에 저장
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    prev = data[0]
    if prev==0:
        return 0
    
    n = len(data)
    table = [[0]*2 for _ in range(n)]

    for i in range(n):
        if prev not in [1,2] and data[i]==0:
            return 0
        if i==0:
            table[0] = [1,0]
        else:
            if data[i]==0:
                table[i][0] = 0
            else:
                table[i][0] = table[i-1][0] + table[i-1][1]
            if prev==1:
                table[i][1] = table[i-1][0]
            elif prev==2:
                if data[i]<=6:
                    table[i][1] = table[i-1][0]
                else:
                    table[i][1] = 0
            else:
                table[i][1] = 0

        prev = data[i]

    return sum(table[-1])%int(1e6)

data = list(input())
data = [int(a) for a in data]
print(solution(data))