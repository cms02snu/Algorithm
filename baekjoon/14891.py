# 14891

def rotate_i(array,dir):
  if dir==1:
    new_array = array[-1:] + array[0:-1]
  else:
    new_array = array[1:] + array[0:1]

  return new_array

def solution(data,rotate):
  for i,dir in rotate:
    check = [False] * 3
    for j in range(3):
      if data[j][2]!=data[j+1][6]:
        check[j] = True
    if i==0:
      data[0] = rotate_i(data[0],dir)
      if check[0]:
        data[1] = rotate_i(data[1],-dir)
        if check[1]:
          data[2] = rotate_i(data[2],dir)
          if check[2]:
            data[3] = rotate_i(data[3],-dir)
    elif i==1:
      data[1] = rotate_i(data[1],dir)
      if check[0]:
        data[0] = rotate_i(data[0],-dir)
      if check[1]:
        data[2] = rotate_i(data[2],-dir)
        if check[2]:
          data[3] = rotate_i(data[3],dir)
    elif i==2:
      data[2] = rotate_i(data[2],dir)
      if check[1]:
        data[1] = rotate_i(data[1],-dir)
        if check[0]:
          data[0] = rotate_i(data[0],dir)
      if check[2]:
        data[3] = rotate_i(data[3],-dir)
    elif i==3:
      data[3] = rotate_i(data[3],dir)
      if check[2]:
        data[2] = rotate_i(data[2],-dir)
        if check[1]:
          data[1] = rotate_i(data[1],dir)
          if check[0]:
            data[0] = rotate_i(data[0],-dir)

  result = 0
  for i in range(4):
    if data[i][0]==1:
      result += 2**i

  return result

data = []
for _ in range(4):
  a = list(input())
  b = [int(i) for i in a]
  data.append(b)
k = int(input())
rotate = []
for _ in range(k):
  a,b = map(int,input().split())
  rotate.append((a-1,b))

print(solution(data,rotate))