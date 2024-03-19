# 4779

def dp(string,l):
  if l==1:
    return string

  a0 = string[:l//3]
  a1 = ' ' * (l//3)
  a2 = string[2*l//3:]

  return dp(a0,l//3) + a1 + dp(a2,l//3)

def solution(n):
  string = '-' * (3**n)
  return dp(string,3**n)

while True:
  try:
    n = int(input())
    print(solution(n))
  except:
    break