def solution(S):
    temp = {}

    for s in S:
        if s not in temp:
            temp[s] = 1
        else:
            temp[s] += 1
    
    result = {}

    for s in temp:
        n = temp[s]
        if n not in result:
            result[n] = 1
        else:
            result[n] += 1

    for s in result:
        if result[s] not in [0,2]:
            return 'No'
        
    return 'Yes'

S = input()
print(solution(S))