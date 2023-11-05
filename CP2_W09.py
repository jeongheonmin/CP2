import numpy as np
import random

ary1_1 = np.random.randint(0,9,size=(1,10))
ary1_2 = np.random.randint(0,9,size=(1,10))
ary2_1 = np.random.randint(0,9,size=(3,3))
ary2_2 = np.random.randint(0,9,size=(3,3))

print("배열의 최소값 출력 :\n", np.argmin(ary1_1))
print("배열의 최소값 출력 :\n", np.argmin(ary2_1))

print("배열의 최대값 출력 :\n", np.argmax(ary1_1))
print("배열의 최대값 출력 :\n", np.argmax(ary2_1))

print("정렬된 배열의 원래 인덱스 출력 :\n", np.argsort(ary1_1))
print("정렬된 배열의 원래 인덱스 출력 :\n", np.argsort(ary2_1))

print("2차원 넘파이 배열 세로로 연결 :\n", np.concatenate((ary2_1, ary2_2),axis=0))
print("2차원 넘파이 배열 가로로 연결 :\n", np.concatenate((ary2_1, ary2_2),axis=1))


ary1_3 = ary1_1.reshape(2,5)
print("1차원 배열을 2차원 배열로 변환 :\n", ary1_3)
ary2_3 = ary2_1.reshape(9)
print("2차원 배열을 1차원 배열로 변환 :\n", ary2_3)

print("2차원 넘파이 배열의 축 전환 :\n", ary2_1.transpose(1,0))