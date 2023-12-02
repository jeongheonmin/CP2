#stack을 이용한 괄호의 매칭 검사
str=input('괄호 입력 :')
s=[None for _ in range(len(str))]
top=-1

def isStackEmpty():
  global SIZE, stack, top
  if(top==-1):
    return True
  else:
    return False

def isStackFull():
  global SIZE, stack, top
  if(top>=len(s)-1):
    return True
  else:
    return False


def pop():
  global SIZE, s, top
  if(isStackEmpty()):
    print("스택이 비었습니다.")
    return None
  data=s[top]
  s[top]=None
  top-=1
  return data

def push(data):
  global SIZE,s,top
  if(isStackFull()):
    print('스택이 꽉 찼습니다.')
    return

  top+=1
  s[top]=data

def peek():
  global SIZE, s, top
  if(isStackEmpty()):
    print('스택이 비었습니다')
    return
  return s[top]

def parent(str):
  global SIZE, s, top
  for p in str:
    if p=='(' or p=='{' or p=='[':
      push(p)
    elif p==')':
      if s[top]=='(':
        pop()
      else:
        return False 

    elif p=='}':
      if s[top]=='{':
        pop()
      else:
        return False

    elif p==']':
      if s[top]=='[':
        pop()
      else:
        return False

  if s[top]==None:
    return True
  else:
    return False

print(parent(str))