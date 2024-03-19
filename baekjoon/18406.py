# 18406

def solution(string):
  n = len(string)
  a = string[:n//2]
  b = string[n//2:]
  result = 0
  for i,j in zip(a,b):
    i = int(i)
    j = int(j)
    result += i-j

  if result==0:
    print('LUCKY')
  else:
    print('READY')

solution(input())