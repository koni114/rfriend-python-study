# day 11
# 과제 1
# 다음의 데이터를 로드해보세요
import numpy as np
x = np.arange(12).reshape(3, 4)

# 다음 두 결과를 도출해보세요. 이 때 reshape 를 사용하지 말고 도출해보세요
np.ravel(x, order='C')
np.ravel(x, order='F')

# 다음의 데이터를 로드해보세요
y = np.arange(12).reshape(2, 3, 2)

# 다음의 결과를 도출해보세요. 이 때 reshape 를 사용하지 말고 도출해보세요
np.ravel(y, order='C')

# 과제 2
# 다음의 데이터를 로드해보세요
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 다음의 결과를 3가지 방법을 이용해서 도출해보세요
# array([1, 2, 3, 4, 5, 6])
np.hstack([a, b])
np.r_[a, b]
np.concatenate((a, b), axis=0)
np.ravel([a, b])

# 다음의 결과를 2가지 방법을 이용해 도출해보세요
# array([[1, 2, 3],
#        [4, 5, 6]])
np.vstack([a, b])
np.r_[[a], [b]]

# 다음의 결과를 2가지 방법을 이용해 도출해보세요
# Out[6]:
# array([[1, 4],
#        [2, 5],
#        [3, 6]])

np.c_[a, b]
np.column_stack([a, b])

# 다음의 데이터를 로드해보세요

import numpy as np
c = np.array([[0, 1, 2], [3, 4, 5]])
d = np.array([[6, 7, 8], [9, 10, 11]])
np.hstack([c.T, d.T])
np.concatenate((c.T, d.T), axis=1)

# 과제 3
# 다음의 데이터를 로드해보세요
import numpy as np
x = np.array([1, 2, 3, 4])
y = np.array([3, 4, 5, 6])

# 다음의 결과를 Numpy 함수를 사용해서 도출해보세요

# 두 개의 배열 x, y 의 교집합을 정렬하여 반환
np.intersect1d(x, y)

# 두 개의 배열 x, y의 합집합을 정렬하여 반환
np.union1d(x, y)

# 첫 번쨰 배열 x가 두 번째 배열 y의 원소를 포함하고 있는지 여부를 불리언 배열을 반환
np.in1d(x, y)

# 첫 번째 배열 x로 부터 두 번째 배열 y를 뺸 차집합을 반환
np.setdiff1d(x, y)

# 두 배열 x, y의 합집합에서 교집합을 뺀 대칭차집합을 반환
np.setxor1d(x, y)

# 과제 4
# 다음의 데이터를 로드해보세요
import numpy as np
x = np.array([5, 4, 3, 2, 1, 0])

# 위 데이터의 최대, 최소 값을 2가지 방법으로 도출해보세요
x.max()
np.max(x)

x.min()
np.min(x)

# 위 데이터의 최대, 최소 값의 index 값을 도출해보세요
x.argmin()
x.argmax()

# 위 데이터를 3보다 크거나 같으면 3으로 치환하고, 작으면 데이터 값 그대로 도출한 결과를 만들어보세요
np.where(x >= 3, 3, x)

# 과제 5
# 다음의 데이터를 로드해보세요

import numpy as np
x = np.array([4, 2, 6, 5, 1, 3, 0])

# 위의 데이터를 2가지 방법으로 오름차순 정렬을 해보세요
np.sort(x)
x[np.argsort(x)]

# 위의 데이터를 2가지 방법으로 내림차순 정렬을 해보세요
np.sort(x)[::-1]
x[np.argsort(-x)]

# 다음의 데이터를 로드해보세요
import numpy as np
x = np.array([4, 2, 6, 5, 1, 3, 0])

# 위의 데이터를 2가지 방법으로 오름차순 정렬을 해보세요
# 위의 데이터를 2가지 방법으로 내림차순 정렬을 해보세요
# 다음의 데이터를 로드해보세요

x2 = np.array([[2, 1, 6],
               [0, 7, 4],
               [5, 3, 2]])

np.sort(x2)