# 1541

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    result = 0
    minus = False
    for a in data:
        if a in ['-','+']:
            if not minus:
                if a=='-':
                    minus = True
        else:
            if minus:
                result -= int(a)
            else:
                result += int(a)

    return result
        
temp = input()
data = []
t = ''
for i,a in enumerate(temp):
    if i==len(temp)-1:
        t += a
        data.append(t)
    if a in ['-','+']:
        data.append(t)
        t = ''
        data.append(a)
    else:
        t += a

print(solution(data))


