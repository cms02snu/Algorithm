# 1918

'''
계산 우선순위 : 괄호 - 곱셈/나눗셈 - 더하기/빼기
우선순위가 같을 경우 앞에거부터
안쪽 괄호부터 계산
문자열을 입력으로 받고 최우선순위 연산자의 index를 뱉는 함수 만들어야 함
괄호를 없애는 연산인지 아닌지 구분하는 bool 값도 return 해야됨
각 숫자 및 연산자를 값으로 갖는 리스트를 자료구조로 사용
'''

def priority(string,start,end):
  # 괄호가 있다면
  if '(' in string[start:end+1]:
    # 가장 앞에 있는 가장 안쪽의 괄호를 찾기
    br_0 = -1
    br_1 = -1
    for i in range(start,end+1):
      if string[i]=='(':
        br_0 = i
      elif string[i]==')':
        br_1 = i
        break
    if br_1-br_0==2:
      return -1,br_0+1
    if br_1-br_0==4:
      return True,br_0+2
    else:
      _,index = priority(string,br_0+1,br_1-1)
      return False,index

  # 괄호가 없다면
  else:
    # 가장 앞에 있는 곱셈이나 나눗셈 체크
    for i in range(start,end+1):
      if string[i]=='*' or string[i]=='/':
        return False,i
    # 곱셈이나 나눗셈 없다면 가장 앞에 있는 덧셈이나 뻴셈 체크
    for i in range(start,end+1):
      if string[i]=='+' or string[i]=='-':
        return False,i

def solution(s):
  if s=='()':
    return ''

  string = []
  for a in s:
    string.append(a)
  while len(string)>1:
    check,index = priority(string,0,len(string)-1)
    # 괄호를 없애는 연산
    if check==-1:
      string.pop(index-1)
      string.pop(index)
    elif check:
      temp = string[index-1]+string[index+1]+string[index]
      string[index-2] = temp
      string.pop(index-1)
      string.pop(index-1)
      string.pop(index-1)
      string.pop(index-1)

    # 괄호와 무관한 연산
    else:
      temp = string[index-1]+string[index+1]+string[index]
      string[index-1] = temp
      string.pop(index)
      string.pop(index)

  return string[0]

print(solution(input()))