# 2437

'''
data 오름차순 정렬
data[i]가 temp + data[i-1] + 1 이하이면 됨 
temp[i] : i번째 수까지로 나타낼 수 있는 수의 최댓값
temp[i] = temp[i-1] + data[i], temp[0] = data[0]
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    data.sort()
    temp = data[0]
    if temp!=1:
        return 1

    for i in range(1,n):
        if data[i]>temp+1:
            return temp+1
        
        temp += data[i]

    return temp+1

n = int(input())
data = list(map(int,input().split()))

print(solution(data))