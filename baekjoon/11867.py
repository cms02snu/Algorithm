# 11867

def solution(a,b):
    if a%2==1 and b%2==1:
        return 'B'
    else:
        return 'A'
    
a,b = map(int,input().split())
print(solution(a,b))