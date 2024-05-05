# 2607

'''
같은 구성인지 확인 후 비슷한 단어인지 확인
'''

def check(bag_target,word):
    for s in word:
        if s in bag_target:
            bag_target[s] -= 1
            if bag_target[s]==0:
                del bag_target[s]
        else:
            bag_target[s] = -1

    if not bag_target:
        return True,True
    
    if len(bag_target)==1:
        for s in bag_target:
            if abs(bag_target[s])==1:
                return False,True
            
    if len(bag_target)==2:
        if set(bag_target.values())=={-1,1}:
            return False,True
            
    return False,False   

def solution(bag_target,target,data):
    count = 0
    for word in data:
        temp = bag_target.copy()
        a,b = check(temp,word)
        if a or b:
            count += 1

    return count

n = int(input())
data = []
for i in range(n):
    if i==0:
        target = input()
    else:
        data.append(input())

bag_target = {}
for s in target:
    if s in bag_target:
        bag_target[s] += 1
    else:
        bag_target[s] = 1

print(solution(bag_target,target,data))