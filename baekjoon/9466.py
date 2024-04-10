# 9466

'''
그냥 단순하게 앞에서부터 재귀함수 돌린다
이미 성공했거나 실패한 경우 result 리스트에 각각 1과 -1로 저장 후 후에 반복문에서 스킵
i의 성공 여부에 대해 판단할 때, 재귀함수에 들어가는 모든 j들을 저장해서
성공 및 실패 여부 갱신해야 한다
재귀함수 돌다가 실패하는 경우
- -1이나 1 만났을 때
- 나 빼고 순환할 때(나를 제외한 이미 만난애 또 만날 때)
- 자기자신 만났을 때 => 미리 제외 / -1,1 만난 경우에 포함
'''

import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e5)+1)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    cycleset.add(x)
    nx = data[x]

    if visited[nx]:
        if nx in cycleset:
            result += cycle[cycle.index(nx):]
    else:
        dfs(nx)

def solution(n,data):
    global visited,cycle,cycleset,result
    visited = [False] * n
    result = []

    for i in range(n):
        if not visited[i]:
            cycle = []
            cycleset = set()
            dfs(i)

    return n - len(result)

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    data = [a-1 for a in data]
    print(solution(n,data))