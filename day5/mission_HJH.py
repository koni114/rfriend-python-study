# 과제 1
import numpy as np
train = np.array([[10., -10., 1.],
                  [5., 0., 2.],
                  [0., 10., 3.]])

test = np.array([[9., -10., 1.],
                 [5., -5., 3.],
                 [1., 0., 5.]])

# 다음의 train DataFrame data 를 0 ~ 1 범위로 변환하는 scaler 를 만들어보세요
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# 해당 scaler 로 train Data 를 변환한 결과를 출력해보세요
scaler.fit(train)
scaler.fit_transform(train)

# test DataFrame data 를 해당 scaler 로 변환해 보세요
print(scaler.transform(test))

# 과제 2
# 다음 X의 데이터를 이항변수화 변환을 수행해보세요
# 이 때, 기준값(threshold) 은 2.0 으로 설정하여 이항변수화를 변환해보세요
X = np.array([[10., -10., 1.],
              [5., 0., 2.],
              [0., 10., 3.]])

from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=2.0)
binarizer.fit_transform(X)

# binarize 함수를 사용하면, 복사를 하지 않고, 원본 데이터를 이항변수화 변환이 가능합니다.
# 다음의 binarize 함수를 사용해서 수행해보세요

from sklearn.preprocessing import binarize
binarize(X, threshold=2.0, copy=False)
print(X)

# 과제 3
# 다음의 train 데이터(범주형) 를 이항변수화(One-Hot encoding) 해보세요
data_train = np.array([[0, 0, 0],
                       [0, 1, 1],
                       [0, 2, 2],
                       [1, 0, 3],
                       [1, 1, 4]])

# 이 때, 다음의 제약조건을 충족하여야 합니다.
# - train data 에 포함되어있지 않은 category 가 발생할 경우, 무시

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown="ignore", sparse=False)
enc.fit_transform(data_train)

# 과제 4
import pandas as pd
np.random.seed(10)
df = pd.DataFrame({'C1': np.random.randn(20),
                   'C2': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                          'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']})

# 다음의 데이터를 활용하여 연속형 변수 C1 을 이산형화 시켜보세요
# - C1 컬럼의 데이터를 10개의 구간으로 나누고, 이를 (1 ~ 10) 까지로 만들어본 후, C1_bin 컬럼에 넣어 보세요.
np_lin = np.linspace(np.min(df['C1']), np.max(df['C1']), 10)
df['C1_bin'] = np.digitize(df['C1'], np_lin)

# - 만든 C1_bin 컬럼 값을 다시 one-hot encoding 을 수행해보세요. 이 때, 첫 번째 변수를 삭제해보세요
pd.get_dummies(df['C1_bin'], prefix='x', drop_first=True)

# 다음의 데이터를 활용하여 연속형 변수 C1을 이산형화 시켜보세요
np.random.seed(10)
df = pd.DataFrame({'C1': np.random.randn(20),
                   'C2': ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
                          'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']})

# - C1 컬럼의 데이터의 1분위수(Q1), 2분위수(Q2), 3분위수(Q3)를 계산해보세요
Q1 = np.quantile(df['C1'], 0.25)
Q2 = np.quantile(df['C1'], 0.5)
Q3 = np.quantile(df['C1'], 0.75)

# - 계산된 Q1, Q3 값을 토대로 4개의 구간을 해당 값 -->
# - (quarter01, quarter02, quarter03, quarter04) 으로 나누고 quarter 컬럼에 할당해보세요
df['quarter'] = np.where(df['C1'] < Q1,
                         'quarter01', np.where(df['C1'] < Q2,
                                               'quarter02',
                                               np.where(df['C1'] < Q3,
                                                        'quarter03',
                                                        'quarter04')))

print(df)

# 과제 5
# 다음의 데이터를 아래와 같이 변환해보세요
# x1, x2 컬럼 데이터를 가지고, 다항 2차수(1, x1, x2, x1^2, x1*x2, x2^2) 컬럼을 만들어보세요

from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
poly_f = PolynomialFeatures(degree=2)
print(poly_f.fit_transform(X))

# 다음의 데이터를 아래와 같이 변환해보세요
# x1, x2, x3 컬럼 데이터를 가지고, (1, x1, x2, x3, x1*x2, x1*x3, x2*x3, x1*x2*x3) 컬럼을 만들어보세요
X2 = np.arange(9).reshape(3, 3)
poly_f2 = PolynomialFeatures(degree=3, interaction_only=True)
print(poly_f2.fit_transform(X2))



