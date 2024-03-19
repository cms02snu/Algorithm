# 15686

import itertools

def chicken_dist(house_loc,chicken_loc):
  result = 0
  for x,y in house_loc:
    house_chicken_dist = int(1e4)
    for nx,ny in chicken_loc:
      d = abs(nx-x) + abs(ny-y)
      house_chicken_dist = min(house_chicken_dist,d)
    result += house_chicken_dist

  return result

def solution(n,m,graph):
  chicken_loc = []
  house_loc = []
  for i in range(n):
    for j in range(n):
      if graph[i][j]==1:
        house_loc.append((i,j))
      elif graph[i][j]==2:
        chicken_loc.append((i,j))

  result = int(1e4)
  for temp in itertools.combinations(chicken_loc,m):
    result = min(result,chicken_dist(house_loc,temp))

  return result

n,m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int,input().split())))

print(solution(n,m,graph))