# 1344

prime = {2,3,5,7,11,13,17}
composite = {0,1,4,6,8,9,10,12,14,15,16,18}
prime_list = list(prime)

def combination(n,r):
    result = 1
    r = min(r,n-r)
    for i in range(n,n-r,-1):
        result = result * i
    for i in range(1,r+1):
        result = result//i

    return result

def goal(n,p):
    # 골 넣을 확률이 p일 때 18골 중 n골을 넣을 확률
    result = combination(18,n) * (p**n) * ((1-p)**(18-n))

    return result

def solution(p,q):
    p = p/100
    q = q/100
    prob0 = 0
    prob1 = 0
    for a in prime_list:
        prob0 += goal(a,p)
        prob1 += goal(a,q)

    return 1 - (1-prob0)*(1-prob1)

p = int(input())
q = int(input())

print(solution(p,q))