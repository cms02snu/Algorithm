# 1253

'''
set에 서로 다른 두 수의 합 모두 저장 후 수 돌면서 set에 있는지 확인
만약 수 중 0이 있을 시 0을 제외한 두 수의 합만 set에 담고 같은 수가 두개 이상 있으면
그 수는 모두 좋은 수
0이 세개 이상 있으면 0도 좋은 수
'''

from bisect import bisect_left,bisect_right
import itertools,sys
input = lambda : sys.stdin.readline().rstrip()

def countf(data,x):
    a = bisect_left(data,x)
    b = bisect_right(data,x)
    return b-a

def solution(data):
    data.sort()
    db = set()
    nonzero = [a for a in data if a!=0]
    num_zero = countf(data,0)

    for a,b in itertools.combinations(nonzero,2):
        db.add(a+b)

    count = 0
    for x in nonzero:
        if num_zero==0:
            if x in db:
                count += 1
        else:
            if x in db or countf(data,x)>1:
                count += 1
    
    if num_zero>2:
        count += num_zero
    elif num_zero>0:
        if 0 in db:
            count += num_zero

    return count

n = int(input())
data = list(map(int,input().split()))

print(solution(data))