# 1138

def solution(n,data):
    index = list(range(n))
    result = []

    for i in range(n):
        k = data[i]
        result.append(index[k])
        index.pop(k)

    lineup = [-1] * n

    for i in range(n):
        lineup[result[i]] = str(i+1)

    print(' '.join(lineup))

n = int(input())
data = list(map(int,input().split()))

solution(n,data)