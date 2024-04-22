# 20115

n = int(input())
data = list(map(int,input().split()))
M = max(data)
result = (sum(data)-M)/2 + M

print(result)