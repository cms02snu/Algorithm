# 14888

def do_calcul(data,calcul_used):
  result = data[0]
  for i in range(n-1):
    if calcul_used[i]==0:
      result = result + data[i+1]
    elif calcul_used[i]==1:
      result = result - data[i+1]
    elif calcul_used[i]==2:
      result = result * data[i+1]
    else:
      if result>=0:
        result = result//data[i+1]
      else:
        result = -(-result//data[i+1])

  return result

def dfs(data,calcul_used,calcul_remain):
  global max_val,min_val

  plus = calcul_remain[0]
  minus = calcul_remain[1]
  multiple = calcul_remain[2]
  divide = calcul_remain[3]

  if calcul_remain==[0,0,0,0]:
    result = do_calcul(data,calcul_used)
    max_val = max(result,max_val)
    min_val = min(result,min_val)

  else:
    if plus>0:
      dfs(data,calcul_used+[0],[plus-1,minus,multiple,divide])
    if minus>0:
      dfs(data,calcul_used+[1],[plus,minus-1,multiple,divide])
    if multiple>0:
      dfs(data,calcul_used+[2],[plus,minus,multiple-1,divide])
    if divide>0:
      dfs(data,calcul_used+[3],[plus,minus,multiple,divide-1])

def solution(n,data,num_calcul):
  global max_val,min_val
  max_val = -int(1e9)
  min_val = int(1e9)

  plus = num_calcul[0]
  minus = num_calcul[1]
  multiple = num_calcul[2]
  divide = num_calcul[3]

  dfs(data,[],[plus,minus,multiple,divide])

  print(max_val)
  print(min_val)

n = int(input())
data = list(map(int,input().split()))
num_calcul = list(map(int,input().split()))

solution(n,data,num_calcul)