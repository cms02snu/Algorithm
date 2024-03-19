# 18111

import sys
input = sys.stdin.readline

def flatten(h):
  blocks = b
  time = 0

  for i in range(n):
    for j in range(m):
      if data[i][j]>h:
        blocks += data[i][j]-h
        time += 2*(data[i][j]-h)
      else:
        blocks -= h-data[i][j]
        time += h-data[i][j]

  if blocks<0:
    return False,-1

  return True,time

def solution(n,m,b,data):
  low = min([min(row) for row in data])
  high = max([max(row) for row in data])

  min_time = int(1e9)
  max_height = 0

  for i in range(low,high+1):
    check,time = flatten(i)
    if check:
      if time<min_time:
        min_time = time
        max_height = i
      elif time==min_time:
        max_height = i
    else:
      break

  print(min_time,max_height)

n,m,b = map(int,input().split())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

solution(n,m,b,data)