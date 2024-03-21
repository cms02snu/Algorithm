# 1229

def sixnumber(i):
    if i==0:
        return 1
    if i==1:
        return 6
    
    result = 1
    for k in range(1,i+1):
        result += 6*k

    result -= i
    for k in range(1,i):
        result -= 2*k

    return result    

def solution(n):
    six_list = []
    i = 0
    while True:
        temp = sixnumber(i)
        if temp>1000000:
            break
        six_list.append(temp)
        i += 1

    six_list = six_list[::-1]


    return 

'''n = int(input())'''
n = 999999
print(solution(n))