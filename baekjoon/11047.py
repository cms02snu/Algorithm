# 11047

def solution(n,target,money):
  count = 0
  while target>0:
    for a in money[::-1]:
      if a<=target:
        count += 1
        target -= a
        break

  return count

n,target = map(int,input().split())
money = []
for _ in range(n):
  money.append(int(input()))

print(solution(n,target,money))