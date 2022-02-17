## day 3
### 과제 1
- 다음의 데이터 `df_all` 를 활용해서 아래의 정보를 확인해보세요
  - dataFrame 내에 결측치 여부를 boolean 형태로 확인해보세요
  - row 행(0, 1), 열('A', 'B') 에 있는 값을 [['A1', 'A2'], [0.5, 2.2]] 로 대체해 보세요
  - 컬럼별 결측값 개수를 구해보세요
  - 행 단위로 결측값 개수를 구해보세요
~~~python
df_left = pd.DataFrame({'KEY': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': [0.5, 2.2, 3.6, 0.4]})

df_right = pd.DataFrame({'KEY': ['K2', 'K3', 'K4', 'K5'],
                         'C': ['C2', 'C3', 'C4', 'C5'],
                         'D': ['D2', 'D3', 'D4', 'D5']})

df_all = pd.merge(df_left, df_right,  how='outer', on='KEY')
~~~

### 과제 2
- 다음의 데이터 `df` 를 활용해서 아래의 정보를 확인해보세요
  - `C1`, `C2` 컬럼의 합을 계산해보세요
  - `C1`, `C2` 컬럼의 누적합을 계산해 보세요
  - `C1`, `C2` 컬럼의 평균값과 표준편차 값을 계산해 보세요
  - 
~~~python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(10).reshape(5, 2),
                  index=['a', 'b', 'c', 'd', 'e'],
                  columns=['C1', 'C2'])

df.loc[['b', 'e'], ['C1']] = None
df.loc[['b', 'c'], ['C2']] = None
~~~

### 과제 3
 - 다음의 데이터 `df`를 활용해서 아래 지시사항의 결과를 도출해 주세요
   - 결측값을 모두 0으로 대체해 주세요
   - 결측값을 앞 방향으로 채워 주세요  
     (ex) index 1번에 있는 값이 결측이라면, index 0번의 값으로 결측값 대체) 
   - 결측값을 뒷 방향으로 채워 주는데, 개수를 1개로 한정해서 채워 주세요.  
     (ex) index 0, 1번에 있는 값이 결측이라면, index 2번의 값으로 1번만 결측값 대체) 
   - 결측값을 컬럼(변수)별 평균으로 대체해 주세요  
   - `C2` 컬럼에서 결측값이 없으면 `C2` 컬럼을 그대로 사용하며, `C2` 컬럼에 결측값이 있으면 `C1` 컬럼으로 결측값 대체
~~~python
df = pd.DataFrame(np.random.randn(5, 3), columns=['C1', 'C2', 'C3'])
df.iloc[0, 0] = None
df.loc[1, ['C1', 'C3']] = np.nan
df.loc[2, 'C2'] = np.nan
df.loc[3, 'C2'] = np.nan
df.loc[4, 'C3'] = np.nan
~~~

### 과제 4
- 다음의 데이터 `df`를 활용해서 아래 지시사항의 결과를 도출해 주세요
  - 결측값이 들어있는 행 전체를 삭제한 데이터를 만들어주세요
  - 결측값이 들어있는 열 전체를 삭제한 데이터를 만들어주세요
  - `C1`, `C2`, `C3` 컬럼의 결측값이 들어있는 행 전체를 삭제한 데이터를 만들어주세요
~~~python
df = pd.DataFrame(np.random.randn(5, 4),
                  columns=['C1', 'C2', 'C3', 'C4'])

df.loc[[0, 1], 'C1'] = None
df.loc[2, 'C2'] = np.nan
~~~

### 과제 5
- 다음의 순서를 따라 결측치 보간(interpolate) 를 수행해 주세요
  - 아래와 같은 결과의 Series 을 만들어주세요 
~~~python
2021-01-03     1.0
2021-01-04     NaN
2021-01-07     NaN
2021-01-10    10.0
~~~
  - 선형으로 비례하는 결측 보간을 수행해 결측값을 채워주세요
  - 시계열 날짜 index를 기준으로 결측값을 보간해주세요
- 다음의 데이터를 dataFrame 값을 기준으로 선형으로 비례하는 방식으로 결측값을 보간해주세요
~~~python
df = pd.DataFrame({'C1': [1, 2, np.nan, np.nan, 5],
                   'C2': [6, 8, 10, np.nan, 20]})
~~~ 