def solution(n,data):
    _sum = sum(data)
    return -_sum

n = int(input())
data = list(map(int,input().split()))

print(solution(n,data))
