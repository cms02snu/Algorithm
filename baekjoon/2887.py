# 2887

def find_parent(parent,x):
  if x!=parent[x]:
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union(a,b):
  par_a = find_parent(parent,a)
  par_b = find_parent(parent,b)

  if par_a<par_b:
    parent[par_b] = par_a
  else:
    parent[par_a] = par_b

def distance(a,b):
  return min(abs(a[3]-b[3]),abs(a[1]-b[1]),abs(a[2]-b[2]))

def solution(n,data):
  global parent
  data_x = sorted(data,key=lambda x:x[1])
  data_y = sorted(data,key=lambda x:x[2])
  data_z = sorted(data,key=lambda x:x[3])

  temp = set()

  for i in range(n-1):
    temp.add(frozenset((data_x[i][0],data_x[i+1][0])))
    temp.add(frozenset((data_y[i][0],data_y[i+1][0])))
    temp.add(frozenset((data_z[i][0],data_z[i+1][0])))

  temp = list(temp)
  edges = []
  for a,b in temp:
    d = distance(data[a],data[b])
    edges.append((d,a,b))
  edges.sort()

  result = 0
  parent = list(range(n))
  count = 0
  for d,a,b in edges:
    if count==n-1:
      break
    if find_parent(parent,a)!=find_parent(parent,b):
      union(a,b)
      result += d
      count += 1

  return result

n = int(input())
data = []
for i in range(n):
  data.append([i] + list(map(int,input().split())))

print(solution(n,data))