# 20055

def rotate(array):
  return [array[-1]] + array[:-1]

def solution(durability,n,k):
  curr_state = list(range(2*n))
  robots = [False] * n

  stage = 0
  while True:
    stage += 1
    # step 1
    curr_state = rotate(curr_state)
    for i in range(n-2,-1,-1):
      if robots[i]:
        robots[i] = False
        robots[i+1] = True
        if i+1==n-1:
          robots[i+1] = False

    # step 2
    for i in range(n-2,-1,-1):
      if robots[i]:
        if not robots[i+1] and durability[curr_state[i+1]]>0:
          robots[i+1] = True
          robots[i] = False
          durability[curr_state[i+1]] -= 1
          if i+1==n-1:
            robots[i+1] = False

    # step 3
    if durability[curr_state[0]]>0:
      robots[0] = True
      durability[curr_state[0]] -= 1

    # step 4
    count = 0
    for i in durability:
      if i==0:
        count += 1
    if count>=k:
      return stage

n,k = map(int,input().split())
durability = list(map(int,input().split()))

print(solution(durability,n,k))