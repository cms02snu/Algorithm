# 1034

'''
열별 숫자 등장횟수 저장 후 큰 순으로 정렬
큰 것부터 가능, 불가능 판단
0 개수의 짝홀 여부, 0과 k 대소관계 고려
가능한 가장 큰 횟수 출력
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def possible(a,k):
    count = 0
    for i in a:
        if i=='0':
            count += 1

    if count<=k and count%2==k%2:
        return True
    else:
        return False

def solution(data):
    db = {}
    for a in data:
        if a in db:
            db[a] += 1
        else:
            db[a] = 1

    db = dict(sorted(db.items(),key=lambda x:-x[1]))

    for a in db:
        if possible(a,k):
            return db[a]
        
    return 0    

n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(input())
k = int(input())

print(solution(data))