# 9252

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(a,b):
    n = len(a)
    m = len(b)

    table = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                continue
            if a[i-1]==b[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j],table[i][j-1])

    seq = ''
    i,j = n,m
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            seq += a[i-1]
            i -= 1
            j -= 1
        elif table[i-1][j]>table[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(table[-1][-1],seq[::-1],sep='\n')

a = input()
b = input()

solution(a,b)