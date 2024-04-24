# 10597

'''
len(S)로 자연수 몇 까지인지 파악

아이디어1)
뒤에서부터 세는데 두자리 묶어서 수 처리 가능하면 무조건 그렇게 한다
안되면 한자리로 처리한다
생각해봐야할 부분 : 두자리 처리 가능해도 한자리 처리하는게 유리한 경우 없나
반례) 2011110132

아이디어2)
dfs(S,used,remain)
'''

def dfs(S,used,remain):
    if len(S)==1:
        if S[0] in remain:
            return [S[0]]
        else:
            return []
    
    elif len(S)==2:
        if S[0]+S[1] in remain:
            return [S[0]+S[1]]
        else:
            if S[0] in remain:
                k = S[0]
                used.add(k)
                remain.remove(k)
                return [S[0]] + dfs(S[1:],used,remain)
            else:
                return []
        
    else:
        if S[0]+S[1] in remain:
            used.add(S[0]+S[1])
            remain.remove(S[0]+S[1])
            u,r = used.copy(),remain.copy()
            result = [S[0]+S[1]] + dfs(S[2:],u,r)
            if S==''.join(result):
                return result
            else:
                used.remove(S[0]+S[1])
                remain.add(S[0]+S[1])
            
        if S[0] in remain:
            used.add(S[0])
            remain.remove(S[0])
            result = [S[0]] + dfs(S[1:],used,remain)
            if S==''.join(result):
                return result
            else:
                return []
        else:
            return []

def solution(S):
    used = set()
    remain = set()
    k = len(S)
    if k<=9:
        for i in range(1,k+1):
            remain.add(str(i))
    else:
        k = (k-9)//2 + 9
        for i in range(1,k+1):
            remain.add(str(i))

    result = dfs(S,used,remain)
    
    print(' '.join(result))

S = input()
solution(S)