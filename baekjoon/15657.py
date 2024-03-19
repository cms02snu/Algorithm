# 15657

def dfs(array,count):
  if count==m:
    for i,a in enumerate(array):
      if i==m-1:
        print(a)
      else:
        print(a,end=' ')

  elif count==0:
    for i in data:
      array.append(i)
      dfs(array,1)
      array.remove(i)

  else:
    for i in [a for a in data if a>=array[-1]]:
      array.append(i)
      dfs(array,count+1)
      array.remove(i)

n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

dfs([],0)