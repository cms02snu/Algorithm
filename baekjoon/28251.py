# 28251
import sys

input = lambda : sys.stdin.readline().rstrip()

def find_parent(parent,x):
    if x!=parent[x]:
        parent[x] = find_parent(parent,parent[x])
    
    return parent[x]

def union(a,b):
    par_a = find_parent(parent,a)
    par_b = find_parent(parent,b)

    if par_a<par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b

def solution(a,b):
    par_a = find_parent(parent,a)
    par_b = find_parent(parent,b)
    if par_a!=par_b:    
        union(a,b)
        temp = [size_data[par_a][0]+size_data[par_b][0],size_data[par_a][1]+size_data[par_b][1]]
        if par_a<par_b:
            size_data[par_a] = temp
            return (size_data[par_a][0]*size_data[par_a][0] - size_data[par_a][1]) // 2
        else:
            size_data[par_b] = temp
            return (size_data[par_b][0]*size_data[par_b][0] - size_data[par_b][1]) // 2
    else:
        return (size_data[par_a][0]*size_data[par_a][0] - size_data[par_a][1]) // 2

n,q = map(int,input().split())
size = list(map(int,input().split()))

parent = list(range(n))
size_data = [[k,k*k] for k in size]

for _ in range(q):
    a,b = map(int,input().split())
    print(solution(a-1,b-1))