'''
최소 개수의 "좋은 수열"로 나눠라

시작하는 수가 2**i * j로 표현가능하면 2**i 만큼 점프가능
무조건 2**i쪽으로 점프하는게 이득
그리디하게 크게크게 점프한다

a*2**b => c*2**d
3*2**5(96) => 5*2**6(320)
96 128 256 320
3*2^5(96) => 11*2^5(352)
96 128 256 320 352
113 => 253
113 114 116 120 128 192 224 240 248 252 253
'''

def maxpower(a):
    exponent = 0
    while a%2==0:
        a = a//2
        exponent += 1

    return exponent

def solution(l,r):
    result = []
    count = 0
    x = l

    while x<r:
        if x==0:
            k = 0
            while True:
                if x+2**k>r:
                    k -= 1
                    break
                else:
                    k += 1
        else:
            k = maxpower(x)
            while k>0:
                if x+2**k<=r:
                    break
                else:
                    k -= 1

        result.append((x,x+2**k))
        count += 1
        x += 2**k

    print(count)
    for a,b in result:
        print(a,b)

l,r = map(int,input().split())
solution(l,r)


