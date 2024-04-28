# 6603

import itertools

def solution(n,data):
    for temp in itertools.combinations(data,6):
        for i,a in enumerate(temp):
            if i==5:
                print(a)
            else:
                print(a,end=' ')

while True:
    data = list(map(int,input().split()))
    n = data.pop(0)
    if n==0:
        break
    solution(n,data)
    print('')