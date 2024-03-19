# 14500

def tet0():
  global result
  for i in range(n):
    for j in range(m-3):
      temp = sum(graph[i][j:j+4])
      result = max(temp,result)

  for i in range(n-3):
    for j in range(m):
      temp = sum([row[j] for row in graph[i:i+4]])
      result = max(temp,result)

def tet1():
  global result
  for i in range(n-1):
    for j in range(m-1):
      temp = sum(graph[i][j:j+2]) + sum(graph[i+1][j:j+2])
      result = max(temp,result)

def tet2():
  global result
  # 수직, 좌
  for i in range(n-2):
    for j in range(1,m):
      temp = sum([row[j] for row in graph[i:i+3]])
      result = max(result,temp+graph[i][j-1],temp+graph[i+2][j-1])

  # 수직, 우
  for i in range(n-2):
    for j in range(m-1):
      temp = sum([row[j] for row in graph[i:i+3]])
      result = max(result,temp+graph[i][j+1],temp+graph[i+2][j+1])

  # 수평, 상
  for i in range(1,n):
    for j in range(m-2):
      temp = sum(graph[i][j:j+3])
      result = max(result,temp+graph[i-1][j],temp+graph[i-1][j+2])

  # 수평, 하
  for i in range(n-1):
    for j in range(m-2):
      temp = sum(graph[i][j:j+3])
      result = max(result,temp+graph[i+1][j],temp+graph[i+1][j+2])

def tet3():
  global result
  # 좌,수평,우
  for i in range(n-2):
    for j in range(m-1):
      temp = graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]
      result = max(result,temp)

  # 우,수평,좌
  for i in range(n-2):
    for j in range(1,m):
      temp = graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j-1]
      result = max(result,temp)

  # 상,수직,하
  for i in range(n-1):
    for j in range(m-2):
      temp = graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]
      result = max(result,temp)

  # 하,수직,상
  for i in range(1,n):
    for j in range(m-2):
      temp = graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i-1][j+2]
      result = max(result,temp)

def tet4():
  global result
  # 상
  for i in range(n-1):
    for j in range(1,m-1):
      temp = graph[i][j] + graph[i+1][j-1] + graph[i+1][j] + graph[i+1][j+1]
      result = max(temp,result)

  # 하
  for i in range(1,n):
    for j in range(1,m-1):
      temp = graph[i][j] + graph[i-1][j-1] + graph[i-1][j] + graph[i-1][j+1]
      result = max(temp,result)

  # 좌
  for i in range(1,n-1):
    for j in range(m-1):
      temp = graph[i][j] + graph[i-1][j+1] + graph[i][j+1] + graph[i+1][j+1]
      result = max(temp,result)

  # 우
  for i in range(1,n-1):
    for j in range(1,m):
      temp = graph[i][j] + graph[i-1][j-1] + graph[i][j-1] + graph[i+1][j-1]
      result = max(temp,result)

def solution(n,m,graph):
  global result
  result = 0
  tet0()
  tet1()
  tet2()
  tet3()
  tet4()

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(n,m,graph))