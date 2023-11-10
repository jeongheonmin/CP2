def selectionSort(ary):  #배열을 하나만 사용해서 선택정렬
  n=len(ary)
  for i in range(n-1):
    minIdx = i
    for j in range(i+1,n):  
      if(ary[minIdx]>ary[j]):
        minIdx = j
    tmp = ary[i]
    ary[i] = ary[minIdx]
    ary[minIdx] = tmp
  return ary

before = [188,162,168,120,50,150,177,105]
print("정렬 전 -->", before)
after = selectionSort(before)
print("정렬 후 -->", after)