# 과제 1
# 다음의 데이터를 로드해보세요
import numpy as np
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 1)
print(y + 1)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 2)
print(y - x)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 3)
print(y % 2)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 4)
print(y * 2)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 5)
print(x * y)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 6)
print(y / x)

# 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 7)
print(y ** x)

# 다음의 데이터를 로드해보세요
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])

# 배열간 비교 연산을 통해, =, !=, >, >=, <=, < 6가지 케이스를 비교해서 boolean 형태로 출력해보세요
# 다음과 같은 결과값이 도출되어야 합니다.
print(np.equal(x, y))
print(np.not_equal(x, y))
print(np.greater(x, y))
print(np.greater_equal(x, y))
print(np.less(x, y))
print(np.less_equal(x, y))

# 다음의 함수는 어떤 결과값이 도출되나요 ?
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])

z = y.copy()
np.array_equal(x, y) # -- (1) : False
np.array_equal(y, z) # -- (2) : True

# 다음의 x, y 데이터를 아래의 조건으로 비교한 결과를 도출해보세요
x4 = np.array([1, 1, 0, 0])
x5 = np.array([1, 0, 1, 0])

# - 두 배열의 원소가 모두 0이 아니면, True 반환
np.logical_and(x4, x5)

# - 두 배열의 원소 중 한개라도 0이 아니면 True 반환
np.logical_or(x4, x5)

# - 두 배열의 원소가 서로 같지 않으면 True 반환
np.logical_xor(x4, x5)

# 다음의 코드를 실행시키면, 어떤 결과가 도출되나요?
x4 = np.array([1, 1, 2, 2])
x5 = np.arange(5)
print(x4 + x5)

# value error 발생.
# broadcasting 이 적용되려면, axis 크기가 동일해야 함

# 과제 2
# 다음의 데이터를 로드해보세요
import pandas as pd
a_df = pd.DataFrame({'x1': [1, 2, 3, 4],
                     'x2': [5, 6, 7, 8]})

# 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
print(a_df + 1)

# 다음의 데이터를 로드해보세요
b = np.arange(12).reshape((4, 3))

# 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
a = np.array([0, 1, 2])
print(a + b)

# 배열의 차원 크기, 모양이 다르면 모두 Broadcasting 이 일어나나요?
# 그렇지 않다면, 어떤 경우에 Broadcasting 이 일어나나요?
# 간단한 코드 예시를 통해 설명해보세요

# 답
# 배열의 차원 크기, 모양이 다르면 모두 Broadcasting 이 일어나지는 않음
# 기준 축에 있는 원소의 크기가 서로 같아야 함
# shape 함수의 가장 마지막 축이 나머지가 0으로 떨어져야 함

a = np.array([1, 2, 3])
b = np.arange(12).reshape((4, 3))

# 아래 a, b array 는 마지막 축의 크기가 3으로 일치하므로,
# broadcasting 이 가능
print(a.shape)
print(b.shape)

# a, b array 의 마지막 축의 크기가 나머지로 떨어지지 않으면 error 발생
a = np.array([1, 2, 3, 4])
b = np.arange(14).reshape((2, 7))
try:
    print(a + b)
except ValueError:
    print("Value Error!")

# 다음의 데이터를 로드해보세요
# 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요

f = np.arange(24).reshape((2,4,3))
print(f + 1)

# 과제 3
# 다음의 코드를 완성시켜 보세요(-- 1)
a = np.array([1, 2, 3, 4])
a_4_1 = a[:, np.newaxis]
print(a_4_1)

# 다음의 코드를 완성시켜 보세요(-- 2)
b = np.arange(12).reshape(3, 4)
b_3_4_1 = b[:, :, np.newaxis]

# 다음의 코드를 완성시켜 보세요(-- 3)
A = np.array([0, 1, 2, 3])
A_2_8 = np.tile(A, (2, 2))
print(A_2_8)

# 다음의 코드를 완성시켜 보세요(-- 4)
B = np.arange(8).reshape(2, 4)
B_2_8 = np.tile(B, (2, 1))
print(B_2_8)

# 과제 4
# 3가지 방법을 사용하여 다음의 데이터의 전치 행렬을 구해보세요
a = np.arange(15).reshape(3, 5)
print(a.T)
print(np.transpose(a))
print(np.swapaxes(a, 0, 1))

# 다음 데이터의 shape 은 (2, 3, 4) 입니다.
# 이를 (2, 4, 3) 으로 변경한 결과를 최소 2가지 방법 이상으로 도출해보세요
b = np.arange(24).reshape(2, 3, 4)
print(np.swapaxes(b, 2, 1).shape)
print(np.transpose(b, (0, 2, 1)).shape)

# 과제 5
# 다음의 코드에서 -- 1 과 -- 2 는 같은 결과를 도출하나요?
# 아니면 다른 결과를 도출하나요? 그 이유는 무엇인가요 ?
d = np.arange(20).reshape(4, 5)
print(d[0:3, 1:3])  # -- 1
print(d[0:3][1:3])  # -- 2

# 결과가 다름.
# 첫 번째 결과는 index 와 column 을 slicing 함
# 두 번째 결과는 index 을 두번 slicing 함

