## day 13
### 과제 1
- 다음의 데이터 `abalone.txt`를 로드해서 `abalone` 변수에 저장해주세요. 
  해당 데이터는 day13 directory 아래 존재합니다. 
- `abalone` 데이터에서 `length_cat` 컬럼을 추가해주세요. 생성 조건은 다음과 같습니다.  
  - `length` 의 값이 중앙값 보다 크면 `length_long`, 작거나 같으면 `length_short` 로 편성해주세요.
- `abalone` 데이터셋을 성별(sex)로 GroupBy를 한 후에, for loop를 돌려 그룹 이름(sex: 'F', 'I', 'M') 별로 출력해주세요  
  각 그룹별 데이터셋은 최대 5개까지 출력해주세요. 다음과 같은 결과값이 출력되어야 합니다.
~~~
F    sex    length_cat  whole_weight  rings
2    F  length_short        0.6770      9
6    F  length_short        0.7775     20
7    F  length_short        0.7680     16
9    F   length_long        0.8945     19
10   F  length_short        0.6065     14


I    sex    length_cat  whole_weight  rings
4    I  length_short        0.2050      7
5    I  length_short        0.3515      8
16   I  length_short        0.2905      7
21   I  length_short        0.2255     10
42   I  length_short        0.0700      5

M    sex    length_cat  whole_weight  rings
0    M  length_short        0.5140     15
1    M  length_short        0.2255      7
3    M  length_short        0.5160     10
8    M  length_short        0.5095      9
11   M  length_short        0.4060     10
~~~
- `abalone` 데이터셋을 두 개의 범주형 변수(sex, length_cat)를 사용하여 for loop 반복문으로 그룹 이름(sex와 length_cat의 조합)과 각 그룹별 데이터셋을 출력해보세요  
  다음과 같은 결과값이 출력되어야 합니다.
~~~
F length_long
   sex   length_cat  whole_weight  rings
9    F  length_long        0.8945     19
22   F  length_long        0.9395     12
23   F  length_long        0.7635      9
24   F  length_long        1.1615     10
25   F  length_long        0.9285     11
F length_short
   sex    length_cat  whole_weight  rings
2    F  length_short        0.6770      9
6    F  length_short        0.7775     20
7    F  length_short        0.7680     16
10   F  length_short        0.6065     14
13   F  length_short        0.6845     10
I length_long
    sex   length_cat  whole_weight  rings
509   I  length_long        0.8735     16
510   I  length_long        1.1095     10
549   I  length_long        0.8750     11
550   I  length_long        1.1625     17
551   I  length_long        0.9885     13
I length_short
   sex    length_cat  whole_weight  rings
4    I  length_short        0.2050      7
5    I  length_short        0.3515      8
16   I  length_short        0.2905      7
21   I  length_short        0.2255     10
42   I  length_short        0.0700      5
M length_long
   sex   length_cat  whole_weight  rings
27   M  length_long        0.9310     12
28   M  length_long        0.9365     15
29   M  length_long        0.8635     11
30   M  length_long        0.9975     10
32   M  length_long        1.3380     18
M length_short
   sex    length_cat  whole_weight  rings
0    M  length_short        0.5140     15
1    M  length_short        0.2255      7
3    M  length_short        0.5160     10
8    M  length_short        0.5095      9
11   M  length_short        0.4060     10
~~~
- `abalone` 데이터셋을 성별 그룹('F', 'I', 'M')을 key로 하고, 데이터셋을 value로 하는 dict를 만들어보세요
~~~
{'F':   sex    length_cat  whole_weight  rings
 2   F  length_short        0.6770      9
 6   F  length_short        0.7775     20
 7   F  length_short        0.7680     16
 9   F   length_long        0.8945     19,
 'I':   sex    length_cat  whole_weight  rings
 4   I  length_short        0.2050      7
 5   I  length_short        0.3515      8,
 'M':   sex    length_cat  whole_weight  rings
 0   M  length_short        0.5140     15
 1   M  length_short        0.2255      7
 3   M  length_short        0.5160     10
 8   M  length_short        0.5095      9}
~~~

### 과제 2
- 다음의 데이터를 로드해주세요
~~~python
import pandas as pd
from pandas import DataFrame

df = DataFrame({'name': ['kim', 'KIM', 'Kim', 'lee', 'LEE', 'Lee', 'wang', 'hong'], 
                'value': [1, 2, 3, 4, 5, 6, 7, 8], 
                'value_2': [100, 300, 200, 100, 100, 300, 50, 80]
               })
~~~
- df 라는 이름의 DataFrame에서, name 변수의 (kim, KIM, Kim) 를 (kim)으로, (lee, LEE, Lee)를 (lee)로,  
  그리고 (wang, hong)을 (others) 라는 항목으로 매핑하여 새로운 변수 name_2 를 만들어 보세요  
  다음과 같은 결과값이 도출되어야 합니다.
~~~
    name	value	value_2	name_2
0	kim	    1	    100	     kim
1	KIM	    2	    300	     kim
2	Kim	    3	    200	     kim
3	lee	    4	    100	     lee
4	LEE	    5	    100	     lee
5	Lee  	6	    300	     lee
6	wang	7	    50	    others
7	hong	8	    80	    others
~~~
- 위의 도출된 데이터를 기반으로, `name_2` 컬럼별 평균값(`value_2`) 을 도출해보세요  
  다음과 같은 결과값이 도출되어야 합니다.
~~~
      value	value_2
name_   2		
kim	    6	 600
lee	    15	 500
others	15	 130
~~~

### 과제 3
- 다음의 데이터를 로드해보세요
~~~python
import pandas as pd

df = pd.DataFrame({'id': [1, 2, 10, 20, 100, 200], 
                   'name': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']})
~~~
- `id` 변수가 전체 5개 자리가 되도록 왼쪽에 비어있는 부분에 '0'을 채워서 새로운 변수 `id_2` 를 만들어보세요  
  다음과 같은 결과를 도출해야합니다.
~~~
In [5]: df
Out[5]: 
    id   name     id_2
0   1    aaa      00001
1   2    bbb      00002
2   10   ccc      00010
3   20   ddd      00020
4  100   eee      00100
5  200   fff      00200
~~~
- 새로 만든 `id_2` 변수와 `name`변수를 각 원소별로 합쳐서 데이터프레임 안에 새로운 변수 `id_name` 만들어보세요  
  다음과 같은 결과값이 도출되어야 합니다.
~~~
In [7]: df
Out[7]: 
       id    name    id_2         id_name
0      1    aaa      00001       00001_aaa
1      2    bbb      00002       00002_bbb
2     10    ccc      00010       00010_ccc
3     20    ddd      00020       00020_ddd
4    100    eee      00100       00100_eee
5    200    fff      00200       00200_fff 
~~~

### 과제 4
- 다음의 데이터를 로드해주세요  
~~~python
df = DataFrame(data=np.arange(20).reshape(4, 5),
               columns = ['c1', 'c2', 'c3', 'c4', 'c5'], 
               index = ['r1', 'r2', 'r3', 'r4'])
df
~~~
- `dict`, `Series`, `list` 와 `groupby`를 적절히 활용하여 다음의 결과를 도출해보세요  
~~~python
       c1	c2	c3	c4	c5
row_g1	5	7	9	11	13
row_g2	25	27	29	31	33
~~~
-  `dict`, `Series`, `list` 와 `groupby`를 적절히 활용하여 다음의 결과를 도출해보세요  
~~~python
   col_g1 col_g2
r1	1	9
r2	11	24
r3	21	39
r4	31	54
~~~
- dataFrame 과 multiIndex를 활용하여 다음의 `hier_df` dataFrame을 만들어보세요  
~~~
print(hier_df)

col_level_1	col_g1	  col_g2
col_level_2	c1	c2	c3	c4	c5
r1	         0	1	2	3	4
r2	         5	6	7	8	9
r3	        10	11	12	13	14
r4	        15	16	17	18	19
 
hier_df.groupby(level = 'col_level_1', axis=1).mean()

col_level_1	col_g1	col_g2
r1	         0.5	3.0
r2	         5.5	8.0
r3	         10.5	13.0
r4	         15.5	18.0
~~~

### 과제 5
- 다음의 데이터를 로드해주세요
~~~python
df = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b'], 
                   'value_1': np.arange(6), 
                   'value_2': np.random.randn(6)})
df
~~~
- 다음의 결과를 도출해보세요
  - `group` 별 non-NA 개수를 도출해보세요  
  - `group` 내 non-NA 값 중 최소값 별 non-NA 합을 도출해보세요
  - `group` 내 non-NA 값 중 최소값을 도출해보세요
  - `group` 내 non-NA 값 중 분위수를 도출해보세요