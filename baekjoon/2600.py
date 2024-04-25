# 2600

'''
dp(k1,k2,db): k1,k2개 구슬이 있는 상황에서 선공이 이기면 0, 후공이 이기면 1 return
만약 다음 상황에서 한가지 경우라도 후공이 이기면 선공 승
만약 다음 상황에서 모든 경우가 선공이 이기면 후공 승
못가져가면 후공 승

0 x(<b1) : 후공 승 (1)
x(<b1) b1 : 선공 승 (0)
b1 b1 : 후공 승 (1)
'''

def dp(k1,k2):
    if (k1,k2) in db:
        return db[(k1,k2)]
    
    result = []

    if k1>=b1:
        result.append(dp(min(k1-b1,k2),max(k1-b1,k2)))
    if k1>=b2:
        result.append(dp(min(k1-b2,k2),max(k1-b2,k2)))
    if k1>=b3:
        result.append(dp(min(k1-b3,k2),max(k1-b3,k2)))
    if k2>=b1:
        result.append(dp(min(k1,k2-b1),max(k1,k2-b1)))
    if k2>=b2:
        result.append(dp(min(k1,k2-b2),max(k1,k2-b2)))
    if k2>=b3:
        result.append(dp(min(k1,k2-b3),max(k1,k2-b3)))

    if not result:
        db[(k1,k2)] = 1
        return 1
    
    if 1 in result:
        db[(k1,k2)] = 0
        return 0
    else:
        db[(k1,k2)] = 1
        return 1

def solution(k1,k2):
    a = min(k1,k2)
    b = max(k1,k2)
    if dp(a,b):
        return 'B'
    else:
        return 'A'

a,b,c = map(int,input().split())
b1,b2,b3 = sorted([a,b,c])
for _ in range(5):
    k1,k2 = map(int,input().split())
    db = {}
    print(solution(k1,k2))