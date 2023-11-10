def findInsertIdx(ary,data): #삽입 정렬 구현
  findMinIdx = -1  # 초기값은 없는 위치로 
  for i in range(len(ary)):
    if (ary[i]>data): 
      findMinIdx = i
      break
  if findMinIdx== -1:  # 큰 값을 못 찾았을 때 == 제일 마지막 위치 (배열인덱스 + 1)
    return len(ary)
  else:
    return findMinIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []
print("정렬 전 -->", before)
for i in range(len(before)):
  data = before[i]
  insPos = findInsertIdx(after,data)
  after.insert(insPos,data)

print("정렬 후 -->", after)


def insertionSort(ary): #삽입정렬의 효율적인 구현(배열 하나일 때)
  n = len(ary)
  for end in range(1,n):
    for cur in range(end,0,-1):
      if(ary[cur-1]>ary[cur]):
        ary[cur-1],ary[cur] = ary[cur],ary[cur-1]
  return ary

before = [188, 162, 168, 120, 50, 150, 177, 105]

print("정렬 전 -->", before)
after = insertionSort(before)
print("정렬 후 -->", after)