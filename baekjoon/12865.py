# 12865

def solution(data,k):
  data = [a for a in data if a[0]<=k]
  data.sort(key=lambda x:(-x[0],-x[1]))
  maxval_perweight = [-1] * (k+1)

  for i,(w,v) in enumerate(data):
    if i==0:
      maxval_perweight[w] = v
    else:
      for dw,dv in enumerate(maxval_perweight[:k-w+1]):
        if dv!=-1:
          maxval_perweight[w+dw] = max(v+dv,maxval_perweight[w+dw])
      maxval_perweight[w] = max(v,maxval_perweight[w])

  result = max(maxval_perweight)
  if result==-1:
    return 0

  return result

n,k = map(int,input().split())
data = []
for _ in range(n):
  data.append(tuple(map(int,input().split())))

print(solution(data,k))