# 2629

'''
table[i][j] : i번째 추까지 사용해서 j 가능 불가능
'''

def solution(n,data):
    table = [[False]*40001 for _ in range(n)]

    for i in range(n):
        for j in range(40001):
            if i==0:
                if j==0:
                    table[0][0] = True
                elif j==data[0]:
                    table[0][j] = True

            else:
                if table[i-1][j]:
                    table[i][j] = True
                    if 0<abs(j-data[i])<40001:
                        table[i][abs(j-data[i])] = True
                    if 0<j+data[i]<40001:
                        table[i][j+data[i]] = True

    return table[n-1]

n = int(input())
data = list(map(int,input().split()))
t = int(input())
test = list(map(int,input().split()))
table = solution(n,data)
result = []
for a in test:
    result.append('Y' if table[a] else 'N')

print(' '.join(result))