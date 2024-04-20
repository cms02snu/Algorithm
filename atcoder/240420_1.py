n,q = map(int,input().split())

data = list(map(int,input().split()))
data = [a-1 for a in data]

teeth = [True] * n

for i in data:
    teeth[i] = not teeth[i]

print(sum(teeth))