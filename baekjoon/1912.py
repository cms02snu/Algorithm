# 1912

def solution(n,data):
    table = [0] * n
    
    for i in range(n):
        if i==0:
            table[0] = data[0]
        else:
            table[i] = max(table[i-1]+data[i],data[i])

    return max(table)

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))