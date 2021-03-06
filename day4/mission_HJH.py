# 과제 1
# 다음의 Series 데이터를 아래와 같이 변경해보세요
import pandas as pd
import numpy as np
ser = pd.Series([1, 2, 3, 4, np.nan])

# - 값이 2인 경우는 20, NaN(None) 은 5로 변경해보세요. 이 때 list를 사용해서 변경해보세요
ser.replace([2.0, np.nan], [20.0, 5])

# - 값이 3인 경우는 30, Nan(None) 은 10으로 변경해보세요. 이 때 dict 를 사용해서 변경해보세요
ser.replace({2.0: 20.0, np.nan: 5})

# 다음의 dataFrame 데이터를 아래와 같이 변경해보세요
df = pd.DataFrame({'C1': ['a_old', 'b', 'c', 'd', 'e'],
                   'C2': [1, 2, 3, 4, 5],
                   'C3': [6, 7, 8, 9, np.nan]})

# - C1 컬럼의 a_old 값은 a_new 의 값으로 변경해보세요
df.replace({'C1': "a_old"}, {'C1': 'a_new'})

# - C3 칼럼의 np.nan 값은 C3 컬럼의 10으로 변경해보세요
df.replace({'C3': np.nan}, {'C3': 'a_new'})

# 과제 2
# 다음의 데이터를 사용해서 아래와 같이 변경해보세요
data = {'key1': ['a', 'b', 'b', 'c', 'c'],
        'key2': ['v', 'w', 'w', 'x', 'y'],
        'col': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# - 'key1', 'key2' 중복 여부를 확인해보세요. 중복 데이터가 있을 때 첫 번째 값을 True 로 반환해보세요
df[['key1', 'key2']].duplicated(keep='last')

# - 'key1', 'key2'중복 여부를 확인해보세요. 중복 데이터가 있을 때 마지막 값을 True 로 반환해보세요
df[['key1', 'key2']].duplicated(keep='first')

# - 중복값 처리(unique 한 1개의 key 만 남기고 나머지 중복은 제거)를 해보세요.
# 이 때 중복값 중 첫 번째 값만 남기도록 해보세요
df[['key1', 'key2']].drop_duplicates(keep='first')

# - 중복값 처리(unique 한 1개의 key 만 남기고 나머지 중복은 제거)
# 이 때 중복값 중 마지막 값만 남기도록 해보세요
df[['key1', 'key2']].drop_duplicates(keep='last')

# 과제 3
# 다음의 데이터를 사용하여 아래와 같이 변경해보세요
df = pd.DataFrame({'A': ['A1', 'A1', 'A2', 'A2', 'A3', 'A3'],
                   'B': ['B1', 'B1', 'B1', 'B1', 'B2', np.nan],
                   'C': [1, 1, 3, 4, 4, 4]})


# - A, B, C 컬럼의 유일한 값을 반환해보세요(오름차순 예시)
df['A'].unique()
df['B'].unique()
df['C'].unique()

# - A, B, C 컬럼별 유일값에 대한 개수를 반환해보세요
# 이 때, 결측값도 포함하여 반환하여야 합니다.
df['A'].value_counts()
df['B'].value_counts()
df['C'].value_counts()

# - A, B, C 컬럼별 유일값에 대한 개수의 상대적 비율(A, B, C의 개수 / 전체 개수)을 반환해보세요
df['A'].value_counts(normalize=True)
df['B'].value_counts(normalize=True)
df['C'].value_counts(normalize=True)

# 과제 4
# - 다음의 데이터를 아래와 같은 제약조건으로 표준화를 진행해보세요
# - numpy 를 이용하여 표준화를 진행해보세요(z = (x - mean() / std())
import numpy as np
data = np.random.randint(30, size=(6, 5))
data_standardized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# - scipy.stats 를 이용하여 표준화를 진행해보세요
import scipy.stats as ss
ss.zscore(data, axis=0)

# - sklearn.preprocessing 을 이용하여 포준화를 진행해보세요
from sklearn.preprocessing import StandardScaler
std_scaler = StandardScaler()
std_scaler.fit_transform(data)

# 과제 5
# 다음의 데이터를 로드하는데, 다음의 조건을 충족시켜 주세요
# - numpy 내 숫자 소수점은 둘째자리까지 표현하도록 옵션을 수정하세요
np.set_printoptions(precision=2)

# - np.random. 함수 수행시, 고정되도록 옵션을 수정하세요
np.random.seed(100)

# - 다음의 데이터를 편성하고, 이 데이터를 표준정규분포 기반으로 표준화를 수행하세요
mu, sigma = 10, 2
x = mu + sigma * np.random.randn(100)
x[98:100] = 100

from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

x = x.reshape(-1, 1)
scaler = StandardScaler()
x_transformed = scaler.fit_transform(x)

# - 표준화된 데이터 중, 이상치를 제거하고 histogram 을 그려보세요
plt.hist(x_transformed[x_transformed < 5])

# - 위의 초기 df 데이터를 가지고 RobustScaler 를 사용하여 데이터를 histogram 으로 확인해보고,
# - 기존 표준화된 데이터와 비교해보세요

from sklearn.preprocessing import RobustScaler
robust_scaler = RobustScaler()
robust_x = robust_scaler.fit_transform(x)
plt.hist(robust_x[robust_x < 5])







