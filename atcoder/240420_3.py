'''
친구 그룹 별로 나눈다
친구 그룹 소속 인원 : n
실친 개수 : m
(n,2) - m 개 연산 가능
'''

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union(a,b):
    par_a = find_parent(parent,a)
    par_b = find_parent(parent,b)

    if par_a<par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b

def combination(a,b):
    b = min(b,a-b)
    result = 1
    for i in range(b):
        result  = result * (a-i)
    for i in range(1,b+1):
        result = result//i

    return result

n,m = map(int,input().split())
parent = list(range(n))
friendship = [0] * n
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    friendship[a] += 1
    friendship[b] += 1
    if find_parent(parent,a)!=find_parent(parent,b):
        union(a,b)

group = {}

for i in range(n):
    p = find_parent(parent,i)
    if p not in group:
        group[p] = [1,friendship[i]]
    else:
        group[p][0] += 1
        group[p][1] += friendship[i]

result = 0

for p in group:
    if group[p][0] in [1,2]:
        continue
    a = group[p][0]
    b = group[p][1]
    b = b//2
    result += combination(a,2) - b

print(result)