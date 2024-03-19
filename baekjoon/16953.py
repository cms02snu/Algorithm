# 16953

'''
끝자리가 1이 아닌 홀수는 못만듦
짝수는 무조건 마지막에 2를 곱하는 연산을 통해 만들어야 함

b가 짝수면 2로 나눔
b가 끝자리가 1이면 끝자리 뺌
b가 끝자리가 1이 아닌 홀수면 안됨
'''

def dp(n,count):
  if n==a:
    print(count+1)
  else:
    if n%2==0:
      dp(n//2,count+1)
    elif n==1:
      print(-1)
    elif n%10==1:
      dp(int(str(n)[:-1]),count+1)
    else:
      print(-1)

a,b = map(int,input().split())
dp(b,0)