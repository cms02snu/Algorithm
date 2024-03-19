# 15652

def dfs(array,count):
  if count==m:
    for i,a in enumerate(array):
      if i==m-1:
        print(a)
      else:
        print(a,end=' ')

  elif count==0:
    for i in range(1,n+1):
      array.append(i)
      dfs(array,1)
      array.remove(i)

  else:
    for i in range(array[-1],n+1):
      array.append(i)
      dfs(array,count+1)
      array.remove(i)

n,m = map(int,input().split())

dfs([],0)