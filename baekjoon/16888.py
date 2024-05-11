# 16888

'''
i가 선이면 pass
i가 선이 아니면 i는 후이므로 i+k^2 다 선set에 넣기 => 시간초과

a,a+2가 후이면 a+5,a+7 후
'''

def solution(n):
    firstwin = set()
    firstwin.add(1)

    for i in range(1,n+1):
        if i not in firstwin:
            k = 1
            while i+k*k<=n:
                firstwin.add(i+k*k)
                k += 1
        
    return firstwin

for _ in range(int(input())):
    n = int(input())
    if n%5 not in [0,2]:
        print('koosaga')
    else:
        print('cubelover')