# 11404

def solution(n,graph):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

  for row in graph:
    for i,a in enumerate(row):
      if i==n-1:
        if a==int(1e9):
          print(0)
        else:
          print(a)
      else:
        if a==int(1e9):
          print(0)
        else:
          print(a,end=' ')

n = int(input())
e = int(input())
graph = [[int(1e9)]*n for _ in range(n)]
for i in range(n):
  graph[i][i] = 0
for _ in range(e):
  a,b,c = map(int,input().split())
  graph[a-1][b-1] = min(c,graph[a-1][b-1])

solution(n,graph)