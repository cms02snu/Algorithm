def check(S,T):
    for a in S:
        if not T:
            break

        if a==T[0]:
            T = T[1:]

    if not T:
        return True
    else:
        return False

def solution(S,T):
    if check(S,T):
        return 'Yes'
    
    if check(S,T[:-1]) and T[-1]=='x':
        return 'Yes'
    
    return 'No'

S = input()
T = input()
T = T.lower()

print(solution(S,T))
