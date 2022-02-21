import numpy as np
import os
x = np.arange(5)
os.chdir('/Users/heojaehun/gitRepo/rfriend-python-study/day12')

file_name = 'x_save.npy'
np.save(file_name, x)
result_arr = np.load(file_name)
print(result_arr)

import numpy as np
import os
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])
file_name = "xy_save.npz"
np.savez_compressed(file_name, x=x, y=y)

test = np.load(file_name)
x = test['x']
y = test['y']

import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])

file_name = "xy_save.txt"
np.savetxt(file_name,
           (x, y),
           header="--xy save start--",
           footer="--xy save end--",
           fmt="%1.2f")

import numpy as np
x = np.arange(18).reshape(3, 6)

np.hsplit(x, (2, 4))
np.split(x, 3, axis=1)

x = np.arange(18).reshape(3, 6)
np.split(x, 3, axis=0)
np.vsplit(x, (1, 2))

np.eye(4)
x = np.arange(9).reshape(3, 3)
np.diag(np.diag(x))

a = np.arange(4).reshape(2, 2)
a * a
np.dot(a, a)

c = np.arange(27).reshape(3, 3, 3)
np.trace(c)

d = np.array([[1, 2], [3, 4]])
np.linalg.det(d)

a = np.array(range(4)).reshape(2, 2)
np.linalg.inv(a)

e = np.array([[4, 2], [3, 5]])
w, v = np.linalg.eig(e)

A = np.array([[3,6], [2,3], [0,0], [0,0]])
u, s, vh = np.linalg.svd(A)

a = np.array([[4, 3], [3, 2]])
b = np.array([23, 16])
x = np.linalg.solve(a, b)

np.allclose(np.dot(a, x), b)

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np.c_[x, np.ones(len(x))]
m, c = np.linalg.lstsq(A, y, rcond=True)[0]


import matplotlib.pyplot as plt
plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, x * m + c, 'r', 'fitted line')
plt.legend()
plt.show()

# 과제 4
# 해당 범주형 데이터를 아래와 같이 One-Hot encoding 형태로 전처리해보세요
import pandas as pd
music_df = pd.DataFrame({'music_id': [1, 2, 3, 4, 5],
                         'music_genre': ['rock',
                                         'disco',
                                         'pop',
                                         'rock',
                                         'pop']})


oh_cat_df = pd.get_dummies(music_df['music_genre'], prefix='genre')
print(pd.concat([music_df, oh_cat_df], axis=1))

# 아래 주어진 데이터를 기반으로 One-Hot encoding 을 수행하는 예제입니다
# 다음의 지시를 잘 따라하여 도출해보세요

music_multi_df = pd.DataFrame({'music_id': [1, 2, 3, 4, 5],
                               'music_genre': ['rock|punk rock|heavy metal',
                                               'hip hop|reggae',
                                               'pop|jazz|blues',
                                               'disco|techo',
                                               'rhythm and blues|blues|jazz']})

# 수직바(|) 로 구분되어 있는 music_genre 컬럼에서 | 를 기준으로 잘라 음악 장르 범주 값들을
# 원소로 가지는 하나의 집합(set)을 만들어보세요
music_genre_iter = (set(x.split("|")) for x in music_multi_df.music_genre)
music_genre_set = sorted(set.union(*music_genre_iter))

# music_multi_df 의 행 개수만큼 행과 music_genre_set 의 개수만큼의 열을 가지는
# 0으로 채워진 dataframe 을 만들어보세요
indicator_mat = np.zeros((len(music_multi_df), len(music_genre_set)))
indicator_mat = pd.DataFrame(indicator_mat, columns=music_genre_set)

# indicator_mat 데이터 프레임에 각 행별로 해당하는 음악 장르를 1로 채워 넣어 One-Hot encoding 을 완성하세요
for i, genre in enumerate(music_multi_df.music_genre):
    indicator_mat.loc[i, genre.split("|")] = 1

music_multi_df = music_multi_df.join(indicator_mat.add_prefix('genre_'))

import pandas as pd
abalone = pd.read_csv('./abalone.txt',
                     sep=',',
                     names=['sex', 'length', 'diameter', 'height',
                            'whole_weight', 'shucked_weight', 'viscera_weight',
                            'shell_weight', 'rings'],
                     header=None,
                     )



