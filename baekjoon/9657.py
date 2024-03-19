# 9657

'''
다음턴에 후 승을 만들 수 있으면 선 승
다음턴에 모두 선 승이 되게되면 후 승
1 - 선 승
2 - 후 승
3 - 선 승
4 - 선 승
5 - 선 승(2)
6 - 선 승(2)
7 - 후 승

n-1,n-3,n-4 중 후 승이 하나라도 있으면 선 승
세개 다 선 승이면 후 승

선승 - 0
후승 - 1
'''

def solution(n):
    table = [-1] * max((n+1),5)
    table[1] = 0
    table[2] = 1
    table[3] = 0
    table[4] = 0

    for i in range(5,n+1):
        if table[i-1]==0 and table[i-3]==0 and table[i-4]==0:
            table[i] = 1
        else:
            table[i] = 0

    if table[n]==0:
        return 'SK'
    else:
        return 'CY'

n = int(input())
print(solution(n))