# 1339

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    score = {}
    for A in data:
        for i,a in enumerate(A):
            if a not in score:
                score[a] = 10**i
            else:
                score[a] += 10**i

    temp = [(a,b) for a,b in score.items()]
    temp.sort(key=lambda x:(-x[1]))

    db = {}
    for i,(a,_) in enumerate(temp):
        db[a] = 9-i

    result = 0
    for A in data:
        for i,a in enumerate(A):
            result += 10**i * db[a]

    return result    

n = int(input())
data = []
for _ in range(n):
    t = input()
    data.append(t[::-1])

print(solution(data))