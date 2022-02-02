# 최소 최대 '0 ~ 1' 범위 변환(scaling to 0 ~ 1 range)
# - 정규화 vs 표준화.
# 0 ~ 1 범위 변환에 사용.
# - sklearn.preprocessing.MinMaxScaler() method
# - sklearn.preprocessing.minmax_scale() 함수

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

train = np.array([[10., -10., 1.],
                  [5., 0., 2.],
                  [0., 10., 3.]])

test = np.array([[9., -10., 1.],
                 [5., -5., 3.],
                 [1., 0., 5.]])

# 이항변수화
# 연속형 변수를 특정 기준값 이하이면 '0', 특정 기준값 초과이면 '1'의 두 개의 값만 가지는 변수로 변환

import numpy as np
from sklearn.preprocessing import Binarizer

X = np.array([[10., -10., 1.],
              [5., 0., 2.],
              [0., 10., 3.]])

binarizer = Binarizer().fit(X)
binarizer.transform(X)

binarizer = Binarizer(threshold=2.0)
binarizer.transform(X)

# (2) sklearn.preprocessing.binarize() 함수를 사용한 이항변수화
from sklearn.preprocessing import binarize
binarize(X)
binarize(X, threshold=2.0)
binarize(X, threshold=2.0, copy=False)

X = np.array([[10., -10., 1.],
              [5., 0., 2.],
              [0., 10., 3.]])

# 범주형 변수의 이항변수화: sklearn.preprocessing.OneHotEncoder()

from sklearn.preprocessing import OneHotEncoder
import numpy as np
data_train = np.array([[0, 0, 0],
                       [0, 1, 1],
                       [0, 2, 2],
                       [1, 0, 3],
                       [1, 1, 4]])

print(data_train)

# OneHotEncoder() 로 범주형 변수의 이항변수화 적합시키기: enc.fit()
help(OneHotEncoder)

enc = OneHotEncoder(categories='auto',
                    drop=None,
                    sparse=True,
                    handle_unknown='ignore')
enc.fit(data_train)

enc.transform([["1", '0', '2']]).toarray()
enc.inverse_transform([[0., 1., 1., 0., 0., 0., 0., 1., 0., 0.]])
enc.get_feature_names()
enc.get_params()


