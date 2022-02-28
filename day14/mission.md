## day 14
### 과제 1
- 다음의 데이터를 `abalone`변수에 로드해보세요. 데이터는 다음의 특징을 가지고 있습니다.  
  - url: `https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data`
  - Column name list: ['sex', 'length', 'diameter', 'height', 
                               'whole_weight', 'shucked_weight', 'viscera_weight', 
                               'shell_weight', 'rings']
  - header는 없음
- 다음의 조건을 만족하는 `length_cat` 이라는 범주형 변수를 추가하세요.  
  - `length` 값이 `length`의 중앙값보다 크거나 같으면, `length_long`, 중앙값보다 작으면 `length_short` 
- `sex` 와 `length_cat` 그룹별로 `whole_weight`의 크기(size), 평균(mean), 표준편차(std), 최소값(min), 최대값(max)을 구해보세요. 다음과 같은 결과값이 나와야 하며 리스트(List)를 사용해야 합니다. 
~~~
                   size	  mean	   std	        min    	max
sex	length_cat					
F	length_long	    889	 1.261330	0.329656	0.6405	2.6570
    length_short	418	 0.589702	0.202400	0.0800	1.3580
I	length_long	    188	 0.923215	0.218334	0.5585	2.0495
    length_short	1154 0.351234	0.204237	0.0020	1.0835
M	length_long	    966	 1.255182	0.354682	0.5990	2.8255
    length_short	562	 0.538157	0.246498	0.0155	1.2825
~~~
- `sex`, `length_cat` 그룹별로 `whole_weight`, `shell_weight`의 두 개의 칼럼에 대해서 크기(size), 평균(mean), 표준편차(std), 최소값(min), 최대값(max)을 구해보세요. 다음과 같은 결과값이 나와야합니다.  
해당 결과를 `groupby_result` 에 저장하세요
~~~
                    whole_weight	            shell_weight
                    size	mean	std      	size	mean	std
sex	length_cat						
F	length_long	    889	 1.261330	0.329656	889	 0.360013	0.104014
    length_short	418	 0.589702	0.202400	418	 0.178650	0.063085
I	length_long	    188	 0.923215	0.218334	188	 0.273247	0.064607
    length_short	1154 0.351234	0.204237	1154 0.104549	0.061003
M	length_long	    966	 1.255182	0.354682	966	 0.351683	0.102636
    length_short	562	 0.538157	0.246498	562	 0.162141	0.075629
~~~
- `groupby_result` 에서 성별이 `M`인 경우를 출력해보세요
- `groupby_result` 에서 성별이 `M`이고 `shell_weight` 인 경우를 출력해보세요
- `sex` 와 `length_cat` 그룹별로 `whole_weight` 컬럼은 크기(size), 평균(mean), 표준편차(std) 를, `shell_weight`는 최대 최소 범위(range)와 IQR(iqr) 을 구헤보세요. 이 때 range 컬럼명은 `Range`로, IQR 컬럼명은 `Inter-Quartile_Range` 이어야 합니다.

#### 과제 2
- 다음의 데이터프레임을 로드해주세요
~~~python
import numpy as np
import pandas as pd

df = pd.DataFrame({'grp_col_1' : ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'], 
                   'grp_col_2' : ['c', 'c', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'f'], 
                   'val_1' : np.arange(10),                   
                   'val_2' : np.random.randn(10)})
~~~
- `val_1` 칼럼에 대해서 평균(mean)과 표준편차(std)를 구하고, `val_2` 칼럼에 대해서는 최대값(max)과 최소값(min), 그리고 범위(range)를 구하는 사용자 정의 함수 `stat_func`를 정의해보세요. 이 때 중요한 것은 `apply` 함수에 사용할 수 있어야 합니다.
- 위의 `df`,`stat_func` 을 통해 아래의 결과를 도출해보세요
~~~
                          val_1_mean	val_1_std	val_2_max	val_2_min	val_2_range
grp_col_1	grp_col_2					
a	c	                    0.5	         0.707107	0.829698	-0.766809	1.596508
d	                        3.0	         1.000000	0.885744	-2.119938	3.005682
b	e	                    5.5	         0.707107	2.755351	0.126890	2.628461
f	                        8.0	         1.000000	0.441467	-1.166549	1.608016
~~~
- 위의 결과는 계층적 인덱스로 결과가 도출되는데, 이 인덱스를 컬럼으로 변환하여 출력해보세요  
  다음의 결과가 도출되어야 합니다.
~~~
    grp_col_1	grp_col_2	val_1_mean	val_1_std	val_2_max	val_2_min	val_2_range
0	a	c	0.5	0.707107	0.829698	-0.766809	1.596508
1	a	d	3.0	1.000000	0.885744	-2.119938	3.005682
2	b	e	5.5	0.707107	2.755351	0.126890	2.628461
3	b	f	8.0	1.000000	0.441467	-1.166549	1.608016
~~~

### 과제 3
- 다음의 데이터를 로드해주세요
~~~python
import pandas as pd
import numpy as np

df = pd.DataFrame({'grp_col' : ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'], 
                   'val' : np.arange(10)+1,                   
                   'weight' : [0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.4]})
~~~
- `grp_col` 을 기준으로 그룹별 객체를 만들어 `grouped ` 변수에 저장해보세요.
- `grouped` 변수를 가지고, `weight` 컬럼을 가중평균 계수로하는 `val` 값의 그룹별 가중평균을 구해보세요

### 과제 4
- 다음의 데이터를 로드해주세요
~~~python
import pandas as pd
import numpy as np

np.random.seed(123)

df = pd.DataFrame({'grp': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                   'col_1': np.random.randn(8),
                   'col_2': np.random.randn(8)})

df.loc[[1, 6], ['col_1', 'col_2']] = np.nan                   
~~~
- `Groupby` Operator, lambda 함수, `apply` 함수를 사용해서, `grp` 그룹별 평균값으로 결측치를 채워(imputation, = 보간)해보세요

### 과제 5
- 다음의 데이터를 로드해주세요
~~~python
 import numpy as np
 import pandas as pd
 from pandas import DataFrame

 df = DataFrame({'group_1': ['a', 'a', 'a', 'a', 'a',  
                             'b', 'b', 'b', 'b', 'b',], 
                 'group_2': ['c', 'c', 'c', 'd', 'd', 
                             'e', 'e', 'e', 'f', 'f'], 
                  'col': [1, 2, np.NaN, 4, np.NaN, 
                          6, 7, np.NaN, 9, 10]})
~~~
- `GroupBy()` 로 `group_1`과 `group_2` 칼럼을 모두 적용한 그룹을 만들어 보세요  
     [그룹 ('a', 'c'), 그룹 ('a', 'd'), 그룹 ('b'e, 'e'), 그룹 ('b', 'f')]
- 그룹별로 NaN이 아닌 원소의 '개수(count)', '합(sum)', '최대값(max)'을 계산하여 `df`의 새로울 컬럼으로 추가해보세요
  (hint: `transform`)

