# 15927

def same(S):
    n = len(S)
    if S==S[0]*n:
        return True
    else:
        return False

def palindrome(S):
    if S==S[::-1]:
        return True
    else:
        return False

def solution(S):
    n = len(S)

    if not palindrome(S):
        return n
    
    if not same(S):
        return n-1
    
    return -1

S = input()
print(solution(S))