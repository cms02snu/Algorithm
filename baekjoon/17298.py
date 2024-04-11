# 17298

'''
큰수부터 반복문 진행
index 리스트에는 자기보다 큰 수들의 index가 들어있을텐데 이중 자기의 index의 위치를
이진탐색하여 오큰수의 index 찾음
자기보다 큰 수 중 자기의 index보다 큰 index가 없으면, 즉 이진탐색한 위치가
끝자리라면 -1 결과
그 후 자기의 index 이진탐색한 자리에 삽입
'''

from bisect import bisect_left,insort
import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(data):
    temp = [(a,i) for i,a in enumerate(data)]
    temp.sort(key=lambda x:-x[0])
    index = []
    result = [0] * n

    for l in range(n):
        i = temp[l][1]
        if not index:
            result[i] = '-1'
            index.append(i)
        else:
            idx = bisect_left(index,i)
            if idx==l:
                result[i] = '-1'
                index.append(i)
            else:
                result[i] = str(data[index[idx]])
                insort(index,i)

    print(' '.join(result))
            
n = int(input())
data = list(map(int,input().split()))

solution(data)