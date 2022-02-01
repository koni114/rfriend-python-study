## day 4
### 과제 1
- 다음의 Series 데이터를 아래와 같이 변경해보세요
  - 값이 2인 경우는 20, NaN(None) 은 5로 변경해보세요. 이 때 list를 사용해서 변경해보세요
  - 값이 3인 경우는 30, Nan(None) 은 10으로 변경해보세요. 이 때 dict를 사용해서 변경해보세요
~~~python
import pandas as pd
import numpy as np
ser = pd.Series([1, 2, 3, 4, np.nan])
~~~
- 다음의 dataFrame 데이터를 아래와 같이 변경해보세요
  - `C1` 컬럼의 `a_old` 값은 `a_new`의 값으로 변경해보세요
  - `C3` 칼럼의 np.nan 값은 `C3` 컬럼의 10으로 변경해보세요
~~~python
df = pd.DataFrame({'C1': ['a_old', 'b', 'c', 'd', 'e'],
                   'C2': [1, 2, 3, 4, 5],
                   'C3': [6, 7, 8, 9, np.nan]})
~~~

### 과제 2
- 다음의 데이터를 사용하여 아래와 같이 변경해보세요
  - `key1`, `key2`의 중복 여부를 확인해보세요. 중복 데이터가 있을 때 첫 번째 값을 True로 반환해보세요
  - `key1`, `key2`의 중복 여부를 확인해보세요. 중복 데이터가 있을 때 마지막 값을 True로 반환해보세요  
  - 중복값 처리(unique한 1개의 key만 남기고 나머지 중복은 제거)를 해보세요  
    이 때 중복값 중 첫 번째 값만 남기도록 해보세요  
  - 중복값 처리(unique한 1개의 key만 남기고 나머지 중복은 제거)  
    이 때 중복값 중 마지막 값만 남기도록 해보세요  
~~~python
data = {'key1': ['a', 'b', 'b', 'c', 'c'],
        'key2': ['v', 'w', 'w', 'x', 'y'],
        'col': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
~~~

### 과제 3
- 다음의 데이터를 사용하여 아래와 같이 변경해보세요
  - `A`, `B`, `C` 컬럼의 유일한 값을 반환해보세요(오름차순 예시)
  - `A`, `B`, `C` 컬럼별 유일값에 대한 개수를 반환해보세요  
    이 때, 결측값도 포함하여 반환하여야 합니다.
  - `A`, `B`, `C` 컬럼별 유일값에 대한 개수의 상대적 비율(A, B, C의 개수 / 전체 개수)을 반환해보세요  
~~~python
df = pd.DataFrame({'A': ['A1', 'A1', 'A2', 'A2', 'A3', 'A3'],
                   'B': ['B1', 'B1', 'B1', 'B1', 'B2', np.nan],
                   'C': [1, 1, 3, 4, 4, 4]})
~~~


### 과제 4
- 다음의 데이터를 아래와 같은 제약조건으로 표준화를 진행해보세요
  - `numpy`를 이용하여 표준화를 진행해보세요(z = (x - mean() / std())
  - `scipy.stats` 를 이용하여 표준화를 진행해보세요
  - `sklearn.preprocessing`을 이용하여 포준화를 진행해보세요 
~~~python
import numpy as np
data = np.random.randint(30, size=(6, 5))
~~~

### 과제 5
- 다음의 데이터를 로드하는데, 다음의 조건을 충족시켜 주세요
  - `numpy` 내 숫자 소수점은 둘째자리까지 표현하도록 옵션을 수정하세요
  - `np.random.` 함수 수행시, 고정되도록 옵션을 수정하세요
~~~python
mu, sigma = 10, 2
x = mu + sigma * np.random.randn(100)
x[98:100] = 100
~~~
- 다음의 데이터를 편성하고, 이 데이터를 표준정규분포 기반으로 표준화를 수행하세요
- 표준화된 데이터 중, 이상치를 제거하고 histogram을 그려보세요
- 위의 초기 `df` 데이터를 가지고 `RobustScaler` 를 사용하여 데이터를 histogram 으로 확인해보고, 기존 표준화된 데이터와 비교해보세요
