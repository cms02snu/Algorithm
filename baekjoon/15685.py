# 15685

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def rotate(a,b):
  # a를 b를 기준으로 rotate
  x,y = a
  i,j = b

  x -= i
  y -= j
  x = -x
  x,y = y,x
  x += i
  y += j

  return x,y

def expand(curve):
  rotated_curve = []
  pin = curve[-1]
  for i in range(len(curve)-2,-1,-1):
    temp = rotate(curve[i],pin)
    rotated_curve.append(temp)

  return curve + rotated_curve

def dragon_curve(x,y,d,g):
  nx = x + dx[d]
  ny = y + dy[d]
  curve = [(x,y),(nx,ny)]

  for _ in range(g):
    curve = expand(curve)

  return curve

def solution(n,data):
  dragon_curves = []
  for x,y,d,g in data:
    dragon_curves.append(dragon_curve(x,y,d,g))

  in_curve = set()
  for curve in dragon_curves:
    for x,y in curve:
      in_curve.add((x,y))

  count = 0
  for i in range(100):
    for j in range(100):
      if (i,j) in in_curve and (i+1,j) in in_curve and (i,j+1) in in_curve and (i+1,j+1) in in_curve:
        count += 1

  return count

n = int(input())
data = []
for _ in range(n):
  a,b,c,d = map(int,input().split())
  data.append((b,a,c,d))

print(solution(n,data))