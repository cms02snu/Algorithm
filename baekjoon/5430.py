# 5430

'''
우리가 다루는 데이터는 정수 리스트 형태
이걸로 바꾸고 이거에서 바꾸는 함수 필요
'''

def todata(s):
    if s=='[]':
        return []
    
    data = []
    t = ''

    for a in s:
        if a=='[':
            continue

        if a==',' or a==']':
            data.append(int(t))
            t = ''

        else:
            t += a

    return data

def fromdata(data):
    if data==-1:
        return 'error'
    
    s = '['
    for k,i in enumerate(data):
        if k>0:
            s += ','
        s += str(i)
    s += ']'

    return s

def func(f):
    nr = 0
    nd0 = 0
    nd1 = 0

    for g in f:
        if g=='R':
            nr += 1
        else:
            if nr%2==0:
                nd0 += 1
            else:
                nd1 += 1

    return nr,nd0,nd1

def solution(f,data):
    nr,nd0,nd1 = func(f)

    if nd0+nd1>n:
        return -1

    data = data[nd0:n-nd1]

    if nr%2==1:
        data = data[::-1]

    return data

for _ in range(int(input())):
    f = input()
    n = int(input())
    t = input()
    data = todata(t)
    result = solution(f,data)
    temp = fromdata(result)
    print(temp)