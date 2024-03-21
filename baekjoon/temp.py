def combination(n,r):
    result = 1
    r = min(r,n-r)
    for i in range(n,n-r,-1):
        result = result * i
    for i in range(1,r+1):
        result = result//i

    return result

print(combination(100,50))