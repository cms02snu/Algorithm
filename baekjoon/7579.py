# 7579

def solution(data,m):
    table = {}
    temp = []

    for w,c in data:
        for cost,work in table.items():
            if c+cost not in table:
                temp.append((c+cost,w+work))
            else:
                temp.append((c+cost,max(w+work,table[c+cost])))
        if c not in table:
            temp.append((c,w))
        else:
            temp.append((c,max(table[c],w)))

        while temp:
            cost,work = temp.pop(0)
            if cost in table:
                table[cost] = max(work,table[cost])
            else:
                table[cost] = work

    min_cost = int(1e5)
    for cost,work in table.items():
        if work>=m:
            min_cost = min(min_cost,cost)

    return min_cost

n,m = map(int,input().split())
t1 = list(map(int,input().split()))
t2 = list(map(int,input().split()))
data = [(a,b) for a,b in zip(t1,t2)]

print(solution(data,m))