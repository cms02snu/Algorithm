# 1439

def solution(string):
  count = [0,0]
  curr = -1
  for i in string:
    i = int(i)
    if i!=curr:
      count[i] += 1
      curr = i

  return min(count)

print(solution(input()))