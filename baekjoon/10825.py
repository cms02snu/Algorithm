# 10825

def solution(n,data):
  data.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

  for name,_,_,_ in data:
    print(name)

n = int(input())
data = []
for _ in range(n):
  a,b,c,d = input().split()
  data.append((a,int(b),int(c),int(d)))

solution(n,data)