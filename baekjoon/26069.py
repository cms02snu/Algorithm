# 26069

def solution(n,data):
  dancing = set()
  dancing.add('ChongChong')
  for a,b in data:
    if a in dancing or b in dancing:
      dancing.add(a)
      dancing.add(b)

  return len(dancing)

n = int(input())
data = []
for _ in range(n):
  a,b = input().split()
  data.append((a,b))

print(solution(n,data))