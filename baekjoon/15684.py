# 15684

def check(vertical):
  for k in range(n):
    y = k
    for x in range(h):
      if (x,y) in vertical:
        y += 1
      elif (x,y-1) in vertical:
        y -= 1
    if k!=y:
      return False

  return True

def dfs(vertical,count,x,y):
  global result

  if check(vertical):
    result = min(result,count)
    return

  if count>=result:
    return

  if count<3:
    for i in range(x,h):
      start_y = y if i==x else 0
      for j in range(start_y,n-1):
        if (i,j) not in vertical and (i,j-1) not in vertical and (i,j+1) not in vertical:
          vertical.add((i,j))
          dfs(vertical,count+1,i,j)
          vertical.remove((i,j))

def solution(vertical):
  global result
  result = 4

  dfs(vertical,0,0,0)

  if result==4:
    return -1

  return result

n,m,h = map(int,input().split())
vertical = set()
for _ in range(m):
  a,b = map(int,input().split())
  vertical.add((a-1,b-1))

print(solution(vertical))