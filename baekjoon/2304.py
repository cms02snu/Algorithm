# 2304

'''
증가하다가 감소하는거 밖에 없을 때 남은 것들 중 가장 큰걸로 내려가면 된다
내려갈 때는 항상 뒤에거 중 가장 큰거로 내려간다
올라갈 때는 큰것중 가장 앞에거로 올라간다

자기보다 큰 것중 가장 앞에거로 올라가다가 최고점 도달하면 뒤에거 중 가장 큰거로 내려간다
'''

def maxval(data,i):
    # 0index 값이 i보다 큰 것 중 가장 큰 h,index 값 return
    # 여러개라면 뒤에거 return
    index = 0
    _max = 0
    for k,h in data:
        if k>i:
            if h>_max:
                _max = h
                index = k
            elif h==_max:
                if k>index:
                    index = k

    if index==0:
        return -1,-1
    
    return index,_max

def solution(data):
    temp = sorted(data,key=lambda x: (-x[1],x[0]))
    M,_ = temp[0]
    data.sort()
    data = data[::-1]
    e = data[0][0]

    height = [0] * (e+1)

    up = True
    curr = 0

    for i in range(e+1):
        if not data:
            break
        if i!=data[-1][0]:
            height[i] = curr
        else:
            if up:
                if data[-1][0]==M:
                    curr = data[-1][1]
                    up = False
                    next,nh = maxval(data,M)
                    height[i] = curr
                    curr = nh
                else:
                    if data[-1][1]>curr:
                        curr = data[-1][1]
                        height[i] = curr
                    else:
                        height[i] = curr
            else:
                if i==next:
                    curr = data[-1][1]
                    next,nh = maxval(data,i)
                    height[i] = curr
                    curr = nh
                else:
                    height[i] = curr
                
            data.pop()

    return sum(height)

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int,input().split())))
    
print(solution(data))