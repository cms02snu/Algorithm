# 2504

'''
- 올바른 괄호열 구분
왼쪽괄호 카운트+1 오른쪽괄호 카운트-1 카운트 마이너스 내려가면 틀린 괄호열
0 0 으로 문제없이 끝나면 올바른 괄호열

위 방식은 '[(])'을 잡아내지 못함 그래서 stack 자료구조 사용

- 올바른 괄호열 값 계산
dfs(괄호열)
괄호열이 두 괄호열의 결합으로 구성되어 있다면 두 괄호열 나눠서 dfs 진행
아니라면 2(3) * dfs(안쪽괄호열)
괄호열이 한쌍의 괄호로 구성되었다면 2나 3 return
'''

def r(s):
    if s==')':
        return '('
    if s==']':
        return '['

def correct(string):
    stack = []

    for s in string:
        if s=='(' or s=='[':
            stack.append(s)
        else:
            if not stack:
                return False
            if r(s)==stack[-1]:
                stack.pop()
            else:
                return False
            
    if not stack:
        return True
    else:
        return False
    
def dfs(string):
    if string=='()':
        return 2
    if string=='[]':
        return 3
    
    small = 0
    big = 0

    for i,s in enumerate(string):
        if s=='(':
            small += 1
        elif s==')':
            small -= 1
        elif s=='[':
            big += 1
        else:
            big -= 1

        if small==0 and big==0:
            if i==len(string)-1:
                if string[0]=='(':
                    return 2 * dfs(string[1:-1])
                else:
                    return 3 * dfs(string[1:-1])
            else:
                return dfs(string[:i+1]) + dfs(string[i+1:])
            
S = input()
if correct(S):
    print(dfs(S))
else:
    print(0)