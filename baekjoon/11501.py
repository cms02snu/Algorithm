# 11501

'''
뒤에 높은게 있으면 사
높은게 없으면 있는거 다 팔거나 아무것도 사지마

큰것부터 정렬한 다음에 순서대로 앞에거 다사고 다판다 => 시간초과

뒤에서부터 반복문 진행
현재의 최댓값보다 큰게 나타나면 최댓값 갱신
현재의 최댓값보다 작은게 나타나면 최댓값과의 차이만큼 결과 갱신
'''

import sys
input = lambda : sys.stdin.readline().rstrip()

def solution(n,data):
    data.reverse()
    
    _max = 0
    result = 0
    for a in data:
        if a>_max:
            _max = a
        else:
            result += _max-a

    return result

for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    print(solution(n,data))
