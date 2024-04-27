# 11055

'''
table[i] : i번째 수를 포함한 증가하는 부분수열 중 합의 최댓값
table[i] = max(table[j]+data[i])
'''

def solution(n,data):
    table = [0] * n
    
    for i in range(n):
        if i==0:
            table[0] = data[0]
        else:
            _max = 0
            for j in range(i):
                if data[j]<data[i]:
                    _max = max(_max,table[j])
            table[i] = _max + data[i]
            
    return max(table)

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))
