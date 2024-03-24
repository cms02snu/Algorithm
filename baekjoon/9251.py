# 9251

def solution(str0,str1):
    n = len(str0)
    m = len(str1)

    table = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str0[i-1]==str1[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])

    return table[n][m]

str0 = input()
str1 = input()

print(solution(str0,str1))