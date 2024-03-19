# 14889

import itertools

def diff(data,team0,team1):
  sum_team0 = 0
  for a in team0:
    for b in [i for i in team0 if i!=a]:
      sum_team0 += data[a][b]

  sum_team1 = 0
  for a in team1:
    for b in [i for i in team1 if i!=a]:
      sum_team1 += data[a][b]

  return abs(sum_team0-sum_team1)


def solution(n,data):
  result = int(1e9)
  for team0 in itertools.combinations(list(range(n)),n//2):
    team1 = [i for i in range(n) if i not in team0]
    result = min(result,diff(data,team0,team1))

  return result


n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,data))