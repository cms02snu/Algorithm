# 1629

'''
B를 32비트 2진수로 표현 => 길이 32의 리스트
A의 1,2,4,8,16...2**31 제곱의 값을 저장하는 길이 32의 리스트
'''

def solution(a,b,c):
  a = a%c
  if a==0:
    return 0

  binary = [0] * 32
  binary_power = [0] * 32

  temp = b
  for i in range(31,-1,-1):
    if temp>=2**i:
      temp -= 2**i
      binary[i] = 1

  binary_power[0] = a
  for i in range(31):
    binary_power[i+1] = ((binary_power[i])**2)%c

  result = 1
  for i in range(32):
    if binary[i]==1:
      result = (result * binary_power[i])%c

  return result

a,b,c = map(int,input().split())

print(solution(a,b,c))