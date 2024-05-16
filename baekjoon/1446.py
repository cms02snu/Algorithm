# 1446

import itertools

def dist(check,shortcut):
    curr_loc = 0
    curr_dist = 0
    for i in range(n):
        if check[i]:
            if curr_loc>shortcut[i][0]:
                return int(1e4)+1
            else:
                curr_dist += shortcut[i][2] + shortcut[i][0]-curr_loc
                curr_loc = shortcut[i][1]

    return curr_dist + d-curr_loc

def solution(n,d,shortcut):
    _min = int(1e4)+1
    for temp in itertools.product([True,False],repeat=n):
        _min = min(_min,dist(temp,shortcut))

    return _min    

n,d = map(int,input().split())
shortcut = []
for _ in range(n):
    a,b,c = map(int,input().split())
    if b-a>c and b<=d:
        shortcut.append((a,b,c))
n = len(shortcut)
shortcut.sort()

print(solution(n,d,shortcut))