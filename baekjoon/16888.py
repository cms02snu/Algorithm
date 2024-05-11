# 16888

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(1e6)
first = [False] * (n+1)
for i in range(n+1):
    if not first[i]:
        k = 1
        while True:
            if i+k*k>n:
                break
            first[i+k*k] = True
            k += 1
    
for _ in range(int(input())):
    if first[int(input())]:
        print('koosaga')
    else:
        print('cubelover')