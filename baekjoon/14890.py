# 14890

def road_check(road):
  checkpoints = []
  for i in range(n-1):
    if abs(road[i]-road[i+1])>1:
      return False
    elif road[i]<road[i+1]:
      checkpoints.append((i,-1))
    elif road[i]>road[i+1]:
      checkpoints.append((i+1,1))

  built = [False] * n

  for x,c in checkpoints:
    if c==-1:
      if x-l+1<0:
        return False
      if road[x-l+1:x+1]!=[road[x]]*l:
        return False
      if built[x-l+1:x+1]!=[False]*l:
        return False
      for i in range(x-l+1,x+1):
        built[i] = True
    else:
      if x+l>n:
        return False
      if road[x:x+l]!=[road[x]]*l:
        return False
      if built[x:x+l]!=[False]*l:
        return False
      for i in range(x,x+l):
        built[i] = True

  return True

def solution(n,l,graph):
  count = 0
  for i in range(n):
    temp = graph[i]
    if road_check(temp):
      count += 1

  for j in range(n):
    temp = [row[j] for row in graph]
    if road_check(temp):
      count += 1

  return count

n,l = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(n,l,graph))