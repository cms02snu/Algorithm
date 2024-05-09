# 9011

def solution(n,R):
    num = list(range(1,n+1))
    S = []
    for i in range(n-1,-1,-1):
        if R[i]>=len(num):
            return 'IMPOSSIBLE'
        else:
            S.append(str(num.pop(R[i])))

    S = S[::-1]
    return ' '.join(S)

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    print(solution(n,data))
