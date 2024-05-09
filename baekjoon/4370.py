# 4370

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n):
    i = 0
    a = 1
    next = [9,2]

    while True:
        a *= next[i]
        if n<=a:
            break
        else:
            i = (i+1)%2

    if i==0:
        print('Baekjoon wins.')
    else:
        print('Donghyuk wins.')

while True:
    k = input()
    if k:
        solution(int(k))
    else:
        break