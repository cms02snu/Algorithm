# 2110

'''
check(i) : i의 거리로 공유기 설치했을 때의 결과
1 : 목표 개수보다 더 많이 설치할 수 있다. => i 늘려야함, i+1~end =>> 잘못된 부분
0 : 목표 개수만큼 설치할 수 있다. => i 포함해서 늘려야 함, i~end
-1 : 목표 개수보다 적게 설치할 수 있다. => 줄여야 함, start~i-1
'''

def check(d):
  install = [False] * n
  install[0] = True
  last_install = data[0]
  for i,a in enumerate(data):
    if a>=last_install+d:
      last_install = a
      install[i] = True

  if sum(install)>=target:
    return True
  else:
    return False

def bs(start,end):
  if start==end:
    return start

  pivot = (start+end+1)//2

  if check(pivot):
    return bs(pivot,end)
  else:
    return bs(start,pivot-1)

def solution(n,target,data):
  m = data[0]
  M = data[-1]

  result = bs(1,M-m)

  return result

n,target = map(int,input().split())
data = []
for _ in range(n):
  data.append(int(input()))
data.sort()

print(solution(n,target,data))