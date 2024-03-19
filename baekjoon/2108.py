# 2108

def mode(n,data):
  dic = {}
  for i in data:
    if i not in dic.keys():
      dic[i] = 1
    else:
      dic[i] += 1

  result = 0
  values = []

  for i in dic.keys():
    if dic[i]>result:
      values = [i]
      result = dic[i]
    elif dic[i]==result:
      values.append(i)

  values.sort()
  if len(values)==1:
    return values[0]

  return values[1]

def solution(n,data):
  result = [0,0,0,0]
  data.sort()
  temp = sum(data)/n
  result[0] = int(round(temp,0))
  result[1] = data[n//2]
  result[2] = mode(n,data)
  result[3] = data[-1] - data[0]

  for i in result:
    print(i)

n = int(input())
data = []
for _ in range(n):
  data.append(int(input()))

solution(n,data)