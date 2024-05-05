# 2885

'''
15 = 8 + 4 + 2 + 1
16 4
'''

def power2():
    result = [1]

    while True:
        if result[-1]<500000:
            result.append(result[-1]*2)
        else:
            break

    result = result[::-1]
    
    return result

def log2(x):
    if x==1:
        return 0
    
    count = 0
    while True:
        if x==1:
            return count
        x = x//2
        count += 1

def solution(k):
    power = power2()
    temp = []
    for i in power:
        if i<=k:
            k -= i
            temp.append(i)
            if k==0:
                break

    if len(temp)==1:
        print(temp[0],0)
        return
    
    a = temp[0] * 2
    b = log2(a//temp[-1])

    print(a,b)

solution(int(input()))