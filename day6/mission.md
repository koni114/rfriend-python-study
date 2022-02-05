## day 6
### 과제 1
- 다음의 데이터를 로드해보세요
~~~python
df = pd.DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
                   'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
                   'grade': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                   'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})
~~~
- 아래와 같은 구조로 변경해보세요 (-- 1)
~~~python
# result_df
prod_cd  p1  p2  p3
cust_id           
c1       30  10   0
c2       40  15  30
c3        0   0  10
~~~
- 아래와 같은 구조로 변경해보세요 (-- 2)
~~~python
prod_cd        p1  p2  p3
cust_id grade           
c1      A      30  10   0
c2      A      40  15  30
c3      B       0   0  10
~~~
- 아래와 같은 구조로 변경해보세요 (-- 3)
~~~python
prod_cd    p1    p2    p3    All
grade                          
A        70.0  25.0  30.0  125.0
B         0.0   0.0  10.0   10.0
All      70.0  25.0  40.0  135.0
~~~

### 과제 2
- 다음의 데이터를 로드해보세요
~~~python
mul_index = pd.MultiIndex.from_tuples([('cust_1', '2015'), ('cust_1', '2016'),
                                       ('cust_2', '2015'), ('cust_2', '2016')])
data = pd.DataFrame(data=np.arange(16).reshape(4, 4),
                    index=mul_index,
                    columns=['prd_1', 'prd_2', 'prd_3', 'prd_4'],
                    dtype='int')
data.loc[['cust_2'], ['prd_4']] = np.nan
~~~
- 아래와 같은 구조로 변경해보세요 (-- 1). 이를 `result_df` 로 저장해보세요
~~~python
cust_1     2015   prd_1     0.0
                  prd_2     1.0
                  prd_3     2.0
                  prd_4     3.0
           2016   prd_1     4.0
                  prd_2     5.0
                  prd_3     6.0
                  prd_4     7.0
cust_2     2015   prd_1     8.0
                  prd_2     9.0
                  prd_3    10.0
                  prd_4     NaN
           2016   prd_1    12.0
                  prd_2    13.0
                  prd_3    14.0
                  prd_4     NaN
dtype: float64
~~~
- 저장한 `result_df`를 다음과 같이 변경해보세요 
~~~python
                  2015  2016
cust_1   prd_1     0     4
         prd_2     1     5
         prd_3     2     6
         prd_4     3     7
cust_2   prd_1     8    12
         prd_2     9    13
         prd_3    10    14
         prd_4    11    15
~~~

### 과제 3
- 다음의 데이터를 로드해주세요
~~~python
data = pd.DataFrame({'cust_ID': ['C_001', 'C_001', 'C_002', 'C_002'],
                     'prd_CD': ['P_001', 'P_002', 'P_001', 'P_002'],
                     'pch_cnt': [1, 2, 3, 4],
                     'pch_amt': [100, 200, 300, 400]})
~~~
- 아래와 같은 구조로 변경해주세요(-- 1)
~~~python
  cust_ID  prd_CD  pch_CD      pch_value
0   C_001  P_001   pch_amt        100
1   C_001  P_002   pch_amt        200
2   C_002  P_001   pch_amt        300
3   C_002  P_002   pch_amt        400
4   C_001  P_001   pch_cnt          1
5   C_001  P_002   pch_cnt          2
6   C_002  P_001   pch_cnt          3
7   C_002  P_002   pch_cnt          4
~~~

### 과제 4
- 다음의 데이터를 로드해주세요
~~~python
data_wide = pd.DataFrame({"C1prd1": {0: "a", 1: "b", 2: "c"},
                          "C1prd2": {0: "d", 1: "e", 2: "f"},
                          "C2prd1": {0: 2.5, 1: 1.2, 2: .7},
                          "C2prd2": {0: 3.2, 1: 1.3, 2: .1},
                          "value": dict(zip(range(3), np.random.randn(3)))})
~~~
- 아래와 같은 구조로 변경해주세요(-- 1)
~~~python
                value     C1    C2
seq_no prd                 
0        prd1  1.331587   a     2.5
1        prd1  0.715279   b     1.2
2        prd1 -1.545400   c     0.7
0        prd2  1.331587   d     3.2
1        prd2  0.715279   e     1.3
2        prd2 -1.545400   f     0.1
~~~

### 과제 5
- 다음의 데이터를 로드해주세요
~~~python
import pandas as pd
data = pd.DataFrame({'id': ['id1', 'id1', 'id1', 'id2', 'id2', 'id3'],
                     'fac_1': ['a', 'a', 'a', 'b', 'b', 'b'],
                     'fac_2': ['d', 'd', 'd', 'c', 'c', 'd']})
~~~
- 아래와 같은 구조로 변경해주세요(-- 1)
~~~python
fac_2  c  d
fac_1     
a      0  3
b      2  1
~~~
- 아래와 같은 구조로 변경해주세요(-- 2)
~~~python
fac_1  a  b  
fac_2  d  c  d
id           
id1    3  0  0
id2    0  2  0
id3    0  0  1
~~~
- 아래와 같은 구조로 변경해주세요(-- 3)
~~~python
fac_1  a  b    All
fac_2  d  c  d   
id               
id1    3  0  0   3
id2    0  2  0   2
id3    0  0  1   1
All    3  2  1   6
~~~