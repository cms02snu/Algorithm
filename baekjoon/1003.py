# 1003

'''
0 : 0 1번 1 0번
1 : 0 0번 1 1번
2 : 0 1번 1 1번
3 : 0 1번 1 2번
4 : 0 2번 1 3번
dp(i) = dp(i-1) + dp(i-2)
'''

def solution(n):
    table = [[-1,-1] for _ in range(n+1)]

    if n==0:
        print(1,end=' ')
        print(0)
        return
    if n==1:
        print(0,end=' ')
        print(1)
        return
    
    table[0] = [1,0]
    table[1] = [0,1]    

    for i in range(2,n+1):
        table[i][0] = table[i-1][0] + table[i-2][0]
        table[i][1] = table[i-1][1] + table[i-2][1] 

    print(table[n][0],end=' ')
    print(table[n][1])


for _ in range(int(input())):
    solution(int(input()))