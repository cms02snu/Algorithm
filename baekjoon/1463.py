# 1463

from collections import deque

def solution(n):
  queue = deque()
  queue.append((0,n))

  while True:
    count,x = queue.popleft()
    if x==1:
      return count
    if x%3==0:
      queue.append((count+1,x//3))
    if x%2==0:
      queue.append((count+1,x//2))
    queue.append((count+1,x-1))

print(solution(int(input())))