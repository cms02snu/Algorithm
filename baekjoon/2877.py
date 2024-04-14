# 2877

'''
n자리수 개수 : 2^n
n자리수 중 k번째로 작은 수만 구할줄 알면 됨
4444 4447 4474 4477 4744 4747 4774 4777 7444 7447 7474 7477 7744 7747 7774 7777
n자리수 중 i+1부터 n자리까지 4인 경우의 수 : 2^i

n 이하 자리수 개수 : 2(2^n-1)

101 = 62 + 32 + 4 + 2 (+1)
6자리수 / 6자리수7 / 3자리수7 / 2자리수7
744774

digit : 6
temp : [5,2,1]
'''

def maxk(n):
    i = 0
    k = 0

    while True:
        if 2*(2**(i+1)-1)>n:
            return i,k
        else:
            i += 1
            k = 2*(2**i-1)

def max2(n):
    i = 0

    while True:
        if 2**(i+1)>n:
            return i,2**i
        else:
            i += 1

def solution(n):
    n -= 1
    i,k = maxk(n)
    n -= k
    digit = i+1

    temp = set()

    while n>0:
        i,a = max2(n)
        temp.add(i)
        n -= a

    result = ''
    for i in range(digit):
        if digit-i-1 in temp:
            result += '7'
        else:
            result += '4'

    return result

n = int(input())
print(solution(n))