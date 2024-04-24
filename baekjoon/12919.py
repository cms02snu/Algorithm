# 12919

'''
A로 시작하고 B로 끝나는거는 만들 수 없다 EX)AABBB
A로 시작하는거는 쉽지 않다 EX)AABBBAA
B로 끝나는거는 쉽지 않다 EX)BAABB
'''

def dfs(T):
    global ans
    if len(T)==len(S):
        if T==S:
            ans = 1
        return
        
    s = T[0]
    e = T[-1]

    if s=='A' and e=='B':
        return
    elif s=='A' and e=='A':
        dfs(T[:-1])
    elif s=='B' and e=='A':
        dfs(T[:-1])
        dfs(T[1:][::-1])
    else:
        dfs(T[1:][::-1])

def solution(S,T):
    global ans
    ans = 0
    dfs(T)

    return ans    

S = input()
T = input()

print(solution(S,T))