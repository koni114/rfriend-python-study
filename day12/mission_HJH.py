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

w, b = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, y, rcond=None)[0]

import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='Original data', markersize=8)
plt.plot(x, (w * x) + b, 'r', label='Fitted line')
plt.legend()

# 과제 4
# 해당 범주형 데이터를 아래와 같이 One-Hot encoding 형태로 전처리해보세요
import pandas as pd
music_df = pd.DataFrame({'music_id': [1, 2, 3, 4, 5],
                         'music_genre': ['rock',
                                         'disco',
                                         'pop',
                                         'rock',
                                         'pop']})
music_genre_oh_enc_df = pd.get_dummies(music_df['music_genre']).add_prefix('genre_')
pd.concat([music_df, music_genre_oh_enc_df], axis=1)

# 아래 주어진 데이터를 기반으로 One-Hot encoding 을 수행하는 예제입니다
music_multi_df = pd.DataFrame({'music_id': [1, 2, 3, 4, 5],
                               'music_genre': ['rock|punk rock|heavy metal',
                                               'hip hop|reggae',
                                               'pop|jazz|blues',
                                               'disco|techo',
                                               'rhythm and blues|blues|jazz']})

# 다음의 지시를 잘 따라하여 도출해보세요
# 수직바(|) 로 구분되어 있는 music_genre 컬럼에서 | 를 기준으로 잘라 음악 장르 범주 값들을 원소로 가지는
# 하나의 집합(set)을 만들어보세요

music_genre_iter = (set(x.split("|")) for x in music_multi_df.music_genre)
music_genre_set = sorted(set.union(*music_genre_iter))
print(music_genre_set)

# music_multi_df의 행 개수만큼 행과 music_genre_set 의 개수만큼의 열을 가지는
# 0으로 채워진 dataframe 을 만들어보세요

indicator_mat = pd.DataFrame(np.zeros((len(music_multi_df), len(music_genre_set))),
                             columns=music_genre_set)

# indicator_mat 데이터 프레임에 각 행별로 해당하는 음악 장르를 1로 채워 넣어 One-Hot encoding 을 완성하세요
# 기존의 music_multi_df dataFrame 과 indicator_mat 를 합쳐서 완성해주세요

for i, value in enumerate(music_multi_df.music_genre):
    indicator_mat.loc[i, value.split("|")] = 1

# 과제 5
# 다음의 바다 해산물 전복(abalone)를 로드해주세요. 해당 데이터를 잘 조사하여, 다음과 같은 결과값을 도출해보세요
import os
os.chdir('../day12')
abalone = pd.read_csv('./abalone.txt',
                      sep=',',
                      names=['sex', 'length', 'diameter', 'height',
                             'whole_weight', 'shucked_weight', 'viscera_weight',
                             'shell_weight', 'rings'],
                      header=None,
                      )

# abalone 데이터의 상위 5개의 데이터 샘플을 출력해보고 확인해보세요
abalone.head(5)

# abalone 데이터의 컬럼별 결측치 개수를 확인해보세요
abalone.isnull().sum()

# 전복 성별 그룹별로 전복의 전체 무게 평균, 크기(size)를 계산해보세요
abalone[['sex', 'whole_weight']].groupby('sex').mean()
abalone[['sex', 'whole_weight']].groupby('sex').size()

# 성별(sex)과 길이(length)를 가지고 범주형 변수를 하나 새로 만드세요
# 길이의(length) 중앙값보다 크면, length_long 으로, 중앙값보다 작으면
# length_short 의 이름으로하는 새로운 범주 length_cat 을 만들어주세요

abalone['length_cat'] = np.where(abalone['length'] > np.median(abalone['length']),
                                 'length_long',
                                 'length_short')

# 성별 그룹과 길이 범주(length_cat) 그룹별로 GroupBy를 사용하여 whole_weight'의 평균을 구해보세요
abalone[['sex', 'length_cat', 'whole_weight']].groupby(['sex', 'length_cat']).mean()

