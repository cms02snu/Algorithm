# 14864

'''
index_db = list(range(n))
index = [-1] * n
앞 학생부터 배치 
0번 학생보다 작은 학생 i명 있으면 index[0] = index_db.pop(i)
x번 학생보다 작은 학생 k명 있으면 index[x] = index_db.pop(k)

이렇게 모든 학생을 자리에 배치한 후 모든 순서쌍에 대해 올바른지 비교
EX) 
(3,5) 있으면 index[3]<index[5] 맞는지 확인
하나라도 아니면 -1 return
'''

from bisect import bisect_left
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(order,small):
    index_db = list(range(n))
    index = [-1] * n
    for i in range(n):
        index[i] = index_db.pop(small[i])

    for a,b in order:
        if index[a]<index[b]:
            print(-1)
            return
        
    for a in index:
        print(a+1,end=' ')    

n,m = map(int,input().split())
small = [0] * n
order = []
for _ in range(m):
    a,b = map(int,input().split())
    order.append((a-1,b-1))
    small[a-1] += 1

solution(order,small)