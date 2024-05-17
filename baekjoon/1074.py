# 1074

dr = [0,0,1,1]
dc = [0,1,0,1]

def quadrant(i,r,c):
    s = power(2,i-1)

    if r<s and c<s:
        return 0
    if r<s and c>=s:
        return 1
    if r>=s and c<s:
        return 2
    if r>=s and c>=s:
        return 3

def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    k = power(a,b//2)
    if b%2==0:
        return k*k
    if b%2==1:
        return a*k*k

def dfs(i,r,c):
    division = quadrant(i,r,c)
    if i==1:
        return [division]
    
    i -= 1    
    r -= power(2,i) * dr[division]
    c -= power(2,i) * dc[division]

    return [division] + dfs(i,r,c)

n,r,c = map(int,input().split())
quad = dfs(n,r,c)

result = 0
for i in range(n):
    result += power(2,2*i) * quad[n-i-1]

print(result)