# 25192

def solution(n,data):
  count = 0

  for s in data:
    if s=='ENTER':
      emo_user = set()
    else:
      if s not in emo_user:
        emo_user.add(s)
        count += 1

  return count

n = int(input())
data = []
for _ in range(n):
  data.append(input())

print(solution(n,data))