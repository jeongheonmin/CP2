#stack을 이용한 괄호의 매칭 검사
import sys
str=input('괄호 입력 :')
s=[None for _ in range(len(str))]
top=-1

def isStackEmpty():
  global SIZE, stack, top
  if(top==-1):
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


for p in str:
  if p=='(' or p=='{' or p=='[':
    push(p)
  elif p==')':
    if s[top]=='(':
      pop()
    else:
      print('괄호가 올바르지 않음')
      break
    
  elif p=='}':
    if s[top]=='{':
      pop()
    else:
      print('괄호가 올바르지 않음')
      break
    
  elif p==']':
    if s[top]=='[':
      pop()
    else:
      print('괄호가 올바르지 않음')
      break

if s[top]==None:
  print('True')
else:
  print('False')