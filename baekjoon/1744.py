# 1744

'''
양수 큰수부터 정렬 후 두개씩 묶어서
안 양수 절댓값 큰순으로 정렬후 두개씩 묶어서
'''

def solution(data):
    pos = [a for a in data if a>1]
    one = [a for a in data if a==1]
    neg = [a for a in data if a<=0]

    pos.sort(key=lambda x:-x)
    neg.sort()

    result = 0

    x,y = len(pos)//2,len(pos)%2
    for i in range(x):
        result += pos[2*i]*pos[2*i+1]
    if y==1:
        result += pos[-1]

    x,y = len(neg)//2,len(neg)%2
    for i in range(x):
        result += neg[2*i]*neg[2*i+1]
    if y==1:
        result += neg[-1]

    result += len(one)

    return result

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

print(solution(data))