import os
os.chdir('/Users/heojaehun/gitRepo/rfriend-python-study/day12')

# 과제 1
# 다음의 데이터를 day12 디렉토리 밑에 NumPy format 의 x_save.npy 라는 바이너리 파일로 저장해주세요

import numpy as np
import os
x = np.arange(5)

file_name = 'x_save.npy'
np.save(file_name, x)

# 다음의 위에 저장한 x_save.npy 파일을 로드해 출력해보세요
x = np.load(file_name)
print(x)

# 다음의 데이터를 xy_savez.npz 포맷 파일로 저장해보세요
import numpy as np
import os
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])

file_name = "xy_savez.npz"
np.savez_compressed(file_name, x=x, y=y)

# 다음의 저장한 xy_savez.npz 포맷 파일을 로드해서 x, y를 출력해보세요
np_savez_load = np.load(file_name)
x = np_savez_load['x']
y = np_savez_load['y']
print(x, y)

# 다음의 데이터를 아래 포멧의 text file 을 xy_save.txt 로 저장해 주세요
import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])

file_name = 'savetxt.txt'
np.savetxt(file_name,
           (x, y),
           header='--xy save start--',
           footer='--xy save end--')

# 과제 2
# 다음의 데이터를 로드해보시고, 아래와 같은 결과를 도출해보세요
# 2가지 이상의 방법을 통해서 도출해보세요

import numpy as np
x = np.arange(18).reshape(3, 6)

split_x1 = np.hsplit(x, (2, 4))
split_x2 = np.split(x, 3, axis=1)

# 다음의 데이터를 로드해보시고, 아래와 같은 결과를 도출해보세요
# 2가지 이상의 방법을 통해서 도출해보세요

y = np.arange(18).reshape(3, 6)
split_y1 = np.vsplit(y, (1, 2))
split_y2 = np.split(y, 3, axis=0)
np.array_equal(split_y1, split_y2)

# 과제 3
# 이번 과제는 선형 대수(Linear Algebra)입니다. 디음의 문제를 선형 대수 함수를 사용하여 풀어보세요
# 다음과 같은 단위행렬을 만들어보세요
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
print(np.eye(4))

# 다음의 데이터를 사용해서 다음과 같은 행렬을 만들어보세요
# 대각성분을 이용해야 합니다.

x = np.arange(9).reshape(3, 3)
np.diag(np.diag(x))

# 다음의 데이터를 원소간 곱(element-wise product: a*b)과 내적(dot product) 통해 결과를 도출해보세요
a = np.arange(4).reshape(2, 2)

# 원소간 곱(element-wise)
print(a * a)

# 내적(dot product)
print(a.dot(a))
print(np.dot(a, a))

# 다음의 데이터의 대각합을 구하여 결과를 도출해보세요
# Out[17]: array([36, 39, 42])
c = np.arange(27).reshape(3, 3, 3)
np.trace(c)

# 다음 데이터의 행렬식(Determinant) 값을 구해보세요
d = np.array([[1, 2], [3, 4]])
np.linalg.det(d)

# 다음 데이터의 역행렬을 구해보세요
a = np.array(range(4)).reshape(2, 2)
np.linalg.inv(a)

# 다음 데이터의 고유값(eigenvalue)과 고유벡터(eigenvector)를 구해보세요
e = np.array([[4, 2],[3, 5]])
w, v = np.linalg.eig(e)

# 다음 데이터의 특이값 분해(svd)를 구해보세요
A = np.array([[3, 6], [2, 3], [0, 0], [0, 0]])
s, v, d = np.linalg.svd(A)

# 다음의 연립방정식의 해를 구해보세요
a = np.array([[4, 3], [3, 2]])
b = np.array([23, 16])

# 구한 두 연립방정식의 해가 맞는지 검증해보세요
x = np.linalg.solve(a, b)
np.allclose(a.dot(x), b)

# 다음의 데이터가 주어져있습니다. (x, y 좌표값)
# 해당 데이터를 최소자승법(LSM)을 사용하여 잔차 제곱합을 최소로 하는 회귀계수를 추정해보고,
# 해당 데이터와 회귀적합선을 PLOT 으로 그려보세요

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np
