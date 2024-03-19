# 12100

import itertools
import copy

def slide_line(array):
  new_array = []
  count = 0
  for a in array:
    if a==0:
      count += 1
    else:
      new_array.append(a)

  array = new_array + [0]*count

  merge = []
  next = 1
  for i in range(1,n):
    if i!=next:
      continue
    if array[i-1]==array[i] and array[i]!=0:
      merge.append((i-1,i))
      next = i+2
    else:
      next = i+1

  for i,j in merge:
    array[i] = array[i]*2
    array[j] = 0

  new_array = []
  count = 0
  for a in array:
    if a==0:
      count += 1
    else:
      new_array.append(a)

  new_array = new_array + [0]*count

  return new_array

def slide(data,d):
  new_data = []
  if d==0: # 좌로 밀기
    for row in data:
      new_data.append(slide_line(row))
    return new_data

  elif d==1: # 우로 밀기
    for row in data:
      new_data.append(slide_line(row[::-1])[::-1])
    return new_data

  elif d==2: # 위로 밀기
    newnew_data = [[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        newnew_data[i][j] = data[j][i]
    for row in newnew_data:
      new_data.append(slide_line(row))
    for i in range(n):
      for j in range(n):
        data[i][j] = new_data[j][i]
    return data

  elif d==3: # 아래로 밀기
    newnew_data = [[0]*n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        newnew_data[i][j] = data[j][i]
    for row in newnew_data:
      new_data.append(slide_line(row[::-1])[::-1])
    for i in range(n):
      for j in range(n):
        data[i][j] = new_data[j][i]
    return data

def solution(n,data):
  result = 0
  t = [0,1,2,3]

  for moves in itertools.product(t,repeat=5):
    temp = copy.deepcopy(data)
    for move in moves:
      temp = slide(temp,move)

    a = max([max(row) for row in temp])
    result = max(result,a)

  return result

n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))

print(solution(n,data))