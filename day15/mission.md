## day 15 
### 과제 1
#### 과제 1-1 
- 다음의 데이터를 로드해보세요
~~~python
import numpy as np
import pandas as pd

np.random.seed(123)
df = pd.DataFrame({'col_1': np.random.randint(20, size=20), 
                   'col_2': np.random.randn(20)})
~~~
- `col_1` 컬럼에 대해서 4개의 동일한 길이의 범주를 만들고, 이를 `factor_col_1` 저장해 보세요  
  카테고리의 구간이 [(-0.019, 4.75] < (4.75, 9.5] < (9.5, 14.25] < (14.25, 19.0]] 처럼 4개의 각 구간의 길이가 동일해야 합니다.
- 위의 `factor_col_1` 그룹별로 위의 df 데이터의 `col_1` 의 개수, 평균, 표준편차, 최소값, 최대값을 계산해보세요.  
  다음의 결과값이 나와야 합니다.  
  해당 데이터는 `result_df1` 에 저장해 보세요
~~~
               count	mean	std	min	max
col_1					
(-0.019, 4.75]	8	    1.125	    1.457738	0	4
(4.75, 9.5]	    2	    7.500	    2.121320	6	9
(9.5, 14.25]	4	    12.750	    1.892969	10	14
(14.25, 19.0]	6	    17.000	    1.788854	15	19
~~~
- 위의 `factor_col_1` 그룹별로 위의 df 데이터의 `col_1` 의 개수, 평균, 표준편차, 최소값, 최대값을 계산해보세요.  
  다음의 결과값이 나와야 합니다.   
  단, `summary_func` 사용자 정의 함수를 만들어 `apply` 함수에 적용해서 도출해보세요  
  해당 데이터를 `result_df2` 에 저장해 주세요
~~~
(-0.019, 4.75]  count     8.000000
                max       4.000000
                mean      1.125000
                min       0.000000
                std       1.457738
(4.75, 9.5]     count     2.000000
                max       9.000000
                mean      7.500000
                min       6.000000
                std       2.121320
(9.5, 14.25]    count     4.000000
                max      14.000000
                mean     12.750000
                min      10.000000
                std       1.892969
(14.25, 19.0]   count     6.000000
                max      19.000000
                mean     17.000000
                min      15.000000
                std       1.788854
Name: col_1, dtype: float64
~~~
- `result_df2` 의 데이터를 다시 `result_df1` 처럼 변환해보세요

#### 과제 1-2
- 다음의 데이터를 로드해보세요
~~~python
import numpy as np
import pandas as pd

np.random.seed(123)
df = pd.DataFrame({'col_1': np.random.randint(20, size=20), 
                   'col_2': np.random.randn(20)})
~~~
- `col_2` 에 대해서 구간별 '동일한 개수'로 범주 바구니(bucket categorization)을 만들어보세요  
  이 때, label 을 4, 3, 2, 1로, 줄어드는 순서로 할당을 시켜보세요.  
  다음과 같은 결과값이 도출되어야 합니다.  
  이를 `bucket_qcut_label_col_2` 에 저장해보세요
~~~python
0     1
1     1
2     4
3     2
4     3
5     1
6     2
7     4
8     3
9     1
10    1
11    4
12    4
13    3
14    3
15    3
16    2
17    2
18    4
19    2
Name: col_2, dtype: category
Categories (4, int64): [4 < 3 < 2 < 1]
~~~
- [4 < 3 < 2 < 1] 순서로 동일 개수로 나눈 4개의 그룹별 통계량을 계산해보세요  
  다음의 결과값이 나와야합니다.
~~~
         count	  max	       mean     	min	     std
col_2					
4	     5.0	-0.823598	-1.612369	-3.055577	0.907474
3     	 5.0	-0.308209	-0.522940	-0.777655	0.201746
2	     5.0	1.070781	0.542247	-0.118201	0.589903
1	     5.0	1.804458	1.555265	1.232650	0.262163
~~~

### 과제 2
- 다음의 데이터를 로드해보세요
~~~python
import numpy as np
import pandas as pd
from pandas import DataFrame


# making DataFrame with 4 random variables
np.random.seed(123) # for reproducibility
df= DataFrame(np.random.randn(10, 4), 
                    columns=['a', 'b', 'c', 'd'])

# setting index with 2 group, 'grp1' and 'grp2'
df['group'] = ['grp1', 'grp1', 'grp1', 'grp1', 'grp1', 
               'grp2', 'grp2', 'grp2', 'grp2', 'grp2']

df = df.set_index('group')
~~~
- `d` 변수와 나머지 모든 변수 간 그룹 별 상관계수를 구해보세요  
  다음의 결과값이 나와야 합니다.  
~~~
        a	        b 	       c	      d 
group				
grp1	0.846822	0.099417	0.089205	1.0
grp2	0.307477	0.832473	-0.390469	1.0
~~~
- `a` 변수와 `d` 변수 간 그룹 별 상관계수를 구해보세요  
  다음의 결과값이 도출되어야 합니다.
~~~
         0
group	
grp1	0.846822
grp2	0.307477
~~~

### 과제 3
- 다음의 데이터를 로드해보세요  
  해당 데이터는 당뇨병 데이터입니다.
~~~python
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
~~~
- 위의 `diabetes` 데이터의 attribute 를 활용하여, 아래와 같은 `diabetes_df`를 만들어보세요 
  - `target` 컬럼은 종속변수, `age`, `sex`, `bmi` 는 독립변수에 해당합니다.
~~~python
print(diabetes_df[:5])

    target	age	       sex	       bmi
0	151.0	0.038076	0.050680	0.061696
1	75.0	-0.001882	-0.044642	-0.051474
2	141.0	0.085299	0.050680	0.044451
3	206.0	-0.089063	-0.044642	-0.011595
4	135.0	0.005383	-0.044642	-0.036385
~~~
- `sex` 변수를 가지고 `M`, `F` 를 class로 가지는 `grp`라는 범주형 변수를 만든 후, `sex` 변수는 삭제해주세요  
  `sex` 변수 값이 0보다 큰 경우 `M`, 작거나 같은 경우는 `F`
- 선형회귀모형의 사용자 정의 함수(UDF)를 정의해 주세요
  - 각 그룹별(`sex`) `age`와 `bmi` 변수의 회귀계수를 비교하기 위하여 사용자 정의 함수에서 그룹별 회귀모형의 회귀 계수와 절편을 결과로 반환 하도록 해주세요(종속 변수 --> `target`, 독립 변수 --> `age`, `bmi`)
  - 결과는 [절편, 회귀계수] 형태의 배열로 반환해야 합니다.
- 남성(M)과 여성(F) 그룹별 `절편`과 `age`, `bmi` 변수의 회귀계수 적합 결과를 조회해주세요  
  다음의 결과가 도출되어야 합니다.
~~~
lin_reg_coef['M']
[148.21507864445124, array([ 291.75632268, 1092.80118705])]

lin_reg_coef['F']
[152.40684676047456, array([ 23.19921015, 814.50932703])]
~~~

### 괴제 4
- 다음의 데이터를 로드해주세요
~~~python
import numpy as np
import pandas as pd

# setting seed number for reproducibility
np.random.seed(123)

# Make a DataFrame
df = pd.DataFrame({'grp': ['grp_1']*10 + ['grp_2']*10, 
                          'col_1': np.random.randint(20, size=20), 
                          'col_2': np.random.randint(20, size=20)})
~~~
- 사용자가 지정한 샘플링 비율(`sample_pct`) 만큼 무작위 표본 추출을 해주는 사용자 정의 함수를 정의해보세요  
  결과는 표본 추출 결과 데이터가 반환되어야 합니다.  
  함수명은 `sampling_func` 로 정의해 주세요
- 위의 `sampling_func` 를 활용해서 `grp` 별로 80% 만큼 무작위 표본 추출된 데이터를 도출해주세요

### 과제 5
- 먼저 아래의 값을 활용해서 3개의 그룹 변수, 4개의 연속형 변수를 가진 dataFrame 만들어주세요
~~~python
import numpy as np
import pandas as pd

group_1 = ['A', 'B'] * 20
group_2 = ['C', 'D', 'E', 'F'] * 10
group_3 = ['G', 'H', 'I', "J", 'K', 'L', 'M', 'N'] * 5

df = pd.DataFrame({'group_1': group_1,
                   'group_2': group_2,
                   'group_3': group_3,
                   'col_1': np.random.randn(40),
                   'col_2': np.random.randn(40),
                   'col_3': np.random.randn(40),
                   'col_4': np.random.randn(40)})

df.sort_values(by=['group_1', 'group_2', 'group_3'], axis=0)
~~~
- `group_1`, `group_2`, `group_3` 의 3개의 그룹 변수로 만들어진 모든 경우의 수의 그룹 조합에 대해서, `col_1`,  `col_2`, `col_3`, `col_4` 의 4개 연속형 변수로 2개씩 쌍(pair)을 이루어 만들어진 모든 경우의 수의 조합, 즉, ('col_1',  'col_2'), ('col_1', 'col_3'), ('col_1', 'col_4'), ('col_2', 'col_3'), ('col_2', 'col_4'), ('col_3',  'col_4') 의 4C2=6 개의 조합별 상관계수를 구해보세요.
  - `itertools` 패키지의 `combinations` 를 활용해보세요
  - 그룹별로 두 개의 변수 간 상관계수를 구하는 사용자 정의 함수를 정의해 활용해 for loop 를 통해 결과값을 append 하는 방법을 활용해보세요
