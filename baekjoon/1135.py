# 1135

'''
- 직접 상사의 인덱스를 담은 리스트(입력) : parent
- 간접 부하들에게 모두 전달하는데 걸린 시간을 담은 리스트
: table
- 직접 부하들의 인덱스를 담은 리스트 : child

table[i] = max(sorted(table[x_k]) + n~1)
탑다운 방식으로 구현
'''

def dp(i):
    if not child[i]:
        table[i] = 0
        return
    
    for c in child[i]:
        dp(c)

    temp0 = sorted([table[c] for c in child[i]],key=lambda x:-x)
    temp1 = [k+x for k,x in zip(range(1,len(temp0)+1),temp0)]
    table[i] = max(temp1)
    return

def solution(parent):
    global child,table
    child = [[] for _ in range(n)]
    for i,par in enumerate(parent):
        if i==0:
            continue
        child[par].append(i)

    table = [0] * n

    dp(0)

    return table[0]

n = int(input())
parent = list(map(int,input().split()))

print(solution(parent))