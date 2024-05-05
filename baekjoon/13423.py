# 13423

import itertools,sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data,db):
    count = 0
    for a,b in itertools.combinations(data,2):
        if (a+b)/2 in db:
            count += 1

    return count

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    db = set(data)
    print(solution(data,db))