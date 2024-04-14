# 1493

'''
블로그 참고...
'''

def solution(l,w,h,cubes):
    cubes.reverse()

    result = 0
    curr = 0

    for i,num in cubes:
        curr *= 8
        x,y,z = l//(2**i),w//(2**i),h//(2**i)

        possible = min(x*y*z - curr,num)
        result += possible
        curr += possible

    if curr==l*w*h:
        return result
    else:
        return -1        

l,w,h = map(int,input().split())
n = int(input())
cubes = []
for _ in range(n):
    a,b = map(int,input().split())
    cubes.append((a,b))

print(solution(l,w,h,cubes))