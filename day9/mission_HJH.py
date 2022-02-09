# 과제 1
# 다음의 데이터를 로드해보세요
import numpy as np
arr = np.arange(20).reshape(5, 4)
axis_ABC = np.array(['A', 'A', 'B', 'C', 'C'])

# axis_ABC 를 활용하여, arr 2차원 배열에서 첫 번째와 두 번째 행을 선택해보세요
# 반드시 axis_ABC 를 활용해야 합니다.
print(arr[axis_ABC == 'A', ])

# `axis_ABC` 를 활용하여, `arr` 의 각각 첫 번째와 두 번쨰 행, 열을 선택해보세요
#  반드시 `axis_ABC` 를 활용해야 합니다.
print(arr[axis_ABC == 'A', :2])

# axis_ABC 를 활용하여, arr 의 3, 4, 5 행을 선택해보세요
# 반드시 axis_ABC 를 활용해야 합니다. (hint: ~)
print(arr[~(axis_ABC == 'A')])

# 다음 코드 실행 결과는 어떤 결과가 나올까요?
# 설명해 보세요

# error 발생!
# boolean 타입 slicing 시, and, or --> &, | 로 진행해야함
print(arr[(axis_ABC != 'A') & (axis_ABC != 'B')])

# 다음의 2차원 배열 (arr) 을 적절히 수정하여 다음과 같은 결과가 나올 수 있도록 해보세요
arr = np.arange(20).reshape(5, 4)

# 방법 1
arr[[0, 1], ] = 0
arr[[2, 3], ] = 10
print(arr)

# 방법 2
arr = np.arange(20).reshape(5, 4)
axis_ABC = np.array(['A', 'A', 'B', 'B', 'C'])
arr[axis_ABC == 'A'] = 0
arr[axis_ABC == 'B'] = 10
print(arr)

# 방법 3
arr = np.arange(20).reshape(5, 4)
arr[arr <= 7] = 0
arr[(arr > 7) & (arr <= 15)] = 10
print(arr)

# 과제 2
# Fancy Indexing 이란 무엇인가요?
# --> 배열로 특정 NumPy 배열을 slicing 하는 것.
# --> fancy indexing 을 수행하면, call by reference 가 일어나지 않음

arr = np.arange(20).reshape(4, 5)
arr_copy = arr[[0, 1, 2], 0:2]
arr_copy[0, 0] = 100
print(arr_copy)
print(arr)

# 다음의 데이터를 로드해보세요
a = np.arange(15).reshape(5, 3)

# Fancy Indexing 을 활용하여, 아래와 같은 결과가 나오도록 해보세요(-- 1)
# (여러 가지 방법이 있습니다. 최대한 생각해서 출력해보세요)

# 방법 1
print(a[[0, 2, 4]][:, [0, 2]])

# 방법 2
print(a[np.ix_([0, 2, 4], [0, 2])])

# 다음의 코드의 최종 a 의 결과는 어떻게 될까요?
# fancy indexing 이 아닌 단순 indexing & slicing 과 비교하여 설명해보세요
# --> 100 의 값이 할당되지 않음.
#     fancy indexing 은 주소값을 참조하여 View 만드는 개념이 아닌,
#     배열 자체를 copy 하는 개념이기 때문


# 과제 3
# 다음의 데이터를 로드해보시고, 아래 조건에 만족하는 결과를 도출해보세요

a = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])

# 0.5 를 기준으로 올림 또는 내림
np.round(a)

# 소수점 첫 번째 자리수까지 반올림
np.round(a, 1)

# 가장 가까운 정수로 올림 혹은 내림
np.rint(a)

# '0' 방향으로 가장 가까운 정수로 올림 혹은 내림
np.fix(a)

# 각 원소 값보다 크거나 같은 가장 작은 정수 값으로 올림
np.ceil(a)

# 각 원소 값보다 작거나 같은 가장 큰 정수 값 (바닥 값)으로 내림
np.floor(a)

# 각 원소의 소수점 부분은 잘라버리고 정수값만 남김
np.trunc(a)

# 과제 4
# 다음의 데이터를 로드해보세요
b = np.array([1, 2, 3, 4])
c = np.array([[1, 2], [3, 4]])

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 1)
np.prod(b)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 2)
np.prod(c, axis=0)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 3)
np.prod(c, axis=1)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 4)
np.sum(b)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 5)
np.sum(b, keepdims=True)

# 다음의 데이터를 로드해보세요
d = np.array([[1, 2], [3, np.nan]])

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 1)
np.nanprod(d, axis=0)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 2)
np.nanprod(d, axis=1)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 3)
np.nansum(d, axis=0)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 4)
np.nansum(d, axis=1)

# 다음의 데이터를 로드해보세요
e = np.array([1, 2, 3, 4])
f = np.array([[1, 2, 3], [4, 5, 6]])

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 1)
np.cumprod(e)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 2)
np.cumprod(f, axis=0)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 3)
np.cumprod(f, axis=1)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 4)

np.cumsum(f, axis=1)

# 다음의 데이터를 로드해보세요
g = np.array([1, 2, 4, 10, 13, 20])

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 1)
np.diff(g)

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 2)
np.diff(g, 2)

# 다음의 데이터를 로드해보세요
h = np.array([[1,  2,  4,  8],
              [10, 13, 20, 15]])

# 다음의 결과를 도출해보세요.
# 이 때 단 하나의 NumPy 함수만을 사용하여 결과를 도출해야 합니다.(-- 1)
np.ediff1d(h)

# 과제
# 다음의 데이터를 로드해보세요
x = np.array([0.00001, 1, 2, 4, 10, 100])

# e^x 값을 도출해보세요
np.exp(x)

# log(x), log_10^(x), log_2^(x), log(x+1) 을 도출해보세요
np.log(x)
np.log10(x)
np.log2(x)
np.log1p(x)



