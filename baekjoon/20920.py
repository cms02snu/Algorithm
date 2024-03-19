# 20920

def solution(n,m,data):
  mode = {}
  for word in data:
    if len(word) < m:
      pass
    else:
      if word not in mode.keys():
        mode[word] = 1
      else:
        mode[word] += 1

  temp = list(mode.keys())

  temp.sort(key=lambda x: (-mode[x],-len(x),x))

  for word in temp:
    print(word)

n,m = map(int,input().split())
data = []
for _ in range(n):
  data.append(input())

solution(n,m,data)