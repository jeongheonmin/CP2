import random

def qSort(arr,start,end): #퀵 정렬 
  if end<=start:
    return

  low = start
  high = end

  pivot = arr[(low+high)//2]
  while low<=high:
    while arr[low] < pivot:
      low += 1

    while arr[high] > pivot:
      high -= 1

    if low <= high:
      arr[low], arr[high] = arr[high], arr[low]
      low, high = low+1, high-1

  mid = low

  qSort(arr,start,mid-1)
  qSort(arr,mid,end)

def quickSort(ary):
  qSort(ary,0,len(ary)-1)

random_list = random.sample(range(1,100),20)
print("정렬 전 -->", random_list)
quickSort(random_list)
print("정렬 후 -->", random_list)


def binarySearch(arr,data):  #이진 검색
  start = 0
  end = len(random_list)-1
  while(start <= end):
    mid = (start+end)//2
    if data == arr[mid]:
      return mid
      break
    elif data>arr[mid]:
      start=mid+1
    else:
      end = mid-1
  return -1

findData = int(input())
position = binarySearch(random_list, findData)
if position==-1:
  print(findData, '(은)는 존재하지 않습니다.')
else:
  print(findData, '(은)는', position, "위치에 있습니다.")