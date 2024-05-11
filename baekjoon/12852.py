# 12852

def dfs(n,result):
    result.append(str(n))
    if n>1:
        dfs(prev[n],result)

n = int(input())

table = [0] * (n+1)
prev = [0] * (n+1)

for i in range(2,n+1):
    p = -1
    _min = int(1e9)
    if i%3==0:
        if table[i//3]<_min:
            p = i//3
            _min = table[i//3]
    if i%2==0:
        if table[i//2]<_min:
            p = i//2
            _min = table[i//2]
    if table[i-1]<_min:
        p = i-1
        _min = table[i-1]

    prev[i] = p
    table[i] = _min+1

result = []
dfs(n,result)

print(table[n])
print(' '.join(result))