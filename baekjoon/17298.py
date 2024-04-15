# 17298

'''
stack 사용
새로 넣는 수가 stack 끝수보다 크면 stack 끝수의 오큰수는 새로 넣는 수가 된다
stack 비거나 stack 끝수가 더 커질때까지 반복
그 후 stack에 수의 index와 함께 삽입
반복문 종료 후 stack에 남아있는 수는 -1
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    stack = []
    result = [-1] * n

    for i,a in enumerate(data):
        if i==0:
            stack.append((a,0))
        else:
            while stack:
                if a>stack[-1][0]:
                    _,j = stack.pop()
                    result[j] = a
                else:
                    break
            stack.append((a,i))

    for a in result:
        print(a,end=' ')
            
n = int(input())
data = list(map(int,input().split()))

solution(data)