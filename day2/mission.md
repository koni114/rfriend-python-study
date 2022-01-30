## day 2 mission 
### 과제 1
- 다음의 데이터를 로드하세요
~~~python
idx = ['r0', 'r1', 'r2', 'r3', 'r4']
df = pd.DataFrame({
    'c1': np.arange(5),
    'c2': np.random.randn(5)},
    index=idx)
~~~
- `[r3, r4]`를 빼고, `[r5, r6]`을 새로 추가해보세요. 이때 값들은 전부 0으로 채워주세요  
  아래와 같은 결괏값이 나와야 합니다.
~~~python
c1        c2
r0   0  1.182716
r1   1  0.244398
r2   2 -1.494202
r5   0  0.000000
r6   0  0.000000
~~~
- 다음의 결괏값이 나오도록 dataframe을 만들어주세요  
  이 때, index 는 다음과 같은 시계열 데이터이여야 합니다. 
~~~python
           c1
2022-01-25 10
2022-01-26 20
2022-01-27 30
2022-01-28 40
2022-01-29 50
~~~
- 위의 dataFrame 에서 2022-01-20 ~ 2022-01-24 날짜의 데이터를 추가하고 이 때 가장 최근(2022-01-25)의 데이터로 값을 채워주세요
- 위의 dataFrame 에서 2022-01-30 ~ 2022-01-31 날짜의 데이터를 추가하고 이 때 가장 최근(2022-01-29)의 데이터로 값을 채워주세요

### 과제 2
- 해당 데이터를 로드해 보세요
~~~python
df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'D': ['D0', 'D1', 'D2']},
                    index=[0, 1, 2])

df_2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                     'B': ['B3', 'B4', 'B5'],
                     'C': ['C3', 'C4', 'C5'],
                     'D': ['D3', 'D4', 'D5']},
                     index=[3, 4, 5])

df_3 = pd.DataFrame({'E': ['A6', 'A7', 'A8'],
                     'F': ['B6', 'B7', 'B8'],
                     'G': ['C6', 'C7', 'C8'],
                     'H': ['D6', 'D7', 'D8']},
                     index=[0, 1, 2])                     

df_4 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'E': ['E0', 'E1', 'E2']},
                     index=[0, 1, 3])
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
~~~python
   A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
3  A3  B3  C3  D3
4  A4  B4  C4  D4
5  A5  B5  C5  D5
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
~~~python
   A   B   C   D    E   F   G   H
0  A0  B0  C0  D0  A6  B6  C6  D6
1  A1  B1  C1  D1  A7  B7  C7  D7
2  A2  B2  C2  D2  A8  B8  C8  D8
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
~~~python
    A   B   C    D    E
0  A0  B0  C0   D0  NaN
1  A1  B1  C1   D1  NaN
2  A2  B2  C2   D2  NaN
0  A0  B0  C0  NaN   E0
1  A1  B1  C1  NaN   E1
3  A2  B2  C2  NaN   E2
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
~~~python
   A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
0  A0  B0  C0
1  A1  B1  C1
3  A2  B2  C2
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 5)
~~~python
     A    B    C    D    A    B    C    E
 0   A0   B0   C0   D0   A0   B0   C0   E0
 1   A1   B1   C1   D1   A1   B1   C1   E1
 2   A2   B2   C2   D2  NaN  NaN  NaN  NaN
 3  NaN  NaN  NaN  NaN   A2   B2   C2   E2
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 6)
~~~python
    A   B   C   D   A   B   C   E
 0  A0  B0  C0  D0  A0  B0  C0  E0
 1  A1  B1  C1  D1  A1  B1  C1  E1
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 7)
~~~python
    A   B   C   D    A    B    C    E
 0  A0  B0  C0  D0   A0   B0   C0   E0
 1  A1  B1  C1  D1   A1   B1   C1   E1
 2  A2  B2  C2  D2  NaN  NaN  NaN  NaN
~~~ 

### 과제 3
- 해당 데이터를 로드해 보세요
~~~python
df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'D': ['D0', 'D1', 'D2']},
                     index=[0, 1, 2])
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
~~~python
   A    B  C   D   S
0  A0  B0  C0  D0  S1
1  A1  B1  C1  D1  S2
2  A2  B2  C2  D2  S3
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
~~~python
   A   B   C    D    E
0  A0  B0  C0   D0  NaN
1  A1  B1  C1   D1  NaN
2  A2  B2  C2   D2  NaN
3  S1  S2  S3  NaN   S4
~~~

### 과제 4
- 해당 데이터를 로드해 보세요
~~~python
df_left = pd.DataFrame({'KEY': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

df_right = pd.DataFrame({'KEY': ['K2', 'K3', 'K4', 'K5'],
                         'C': ['C2', 'C3', 'C4', 'C5'],
                         'D': ['D2', 'D3', 'D4', 'D5']})
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
~~~python
   A   B   KEY   C     D
0  A0  B0  K0  NaN  NaN
1  A1  B1  K1  NaN  NaN
2  A2  B2  K2   C2   D2
3  A3  B3  K3   C3   D3 
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
~~~python
    A    B  KEY   C   D
0   A2   B2  K2  C2  D2
1   A3   B3  K3  C3  D3
2  NaN  NaN  K4  C4  D4
3  NaN  NaN  K5  C5  D5
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
~~~python
   A   B KEY   C   D
0  A2  B2  K2  C2  D2
1  A3  B3  K3  C3  D3
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
~~~python
    A    B KEY    C    D indicator_info
0   A0   B0  K0  NaN  NaN      left_only
1   A1   B1  K1  NaN  NaN      left_only
2   A2   B2  K2   C2   D2           both
3   A3   B3  K3   C3   D3           both
4  NaN  NaN  K4   C4   D4     right_only
5  NaN  NaN  K5   C5   D5     right_only
~~~

### 과제 5
- 다음의 데이터를 로드하세요
~~~python
df_left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']},
                        index=['K0', 'K1', 'K2', 'K3'])

df_right = pd.DataFrame({'C': ['C2', 'C3', 'C4', 'C5'],
                         'D': ['D2', 'D3', 'D4', 'D5']},
                         index=['K2', 'K3', 'K4', 'K5'])
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
~~~python
    A   B    C    D
K0  A0  B0  NaN  NaN
K1  A1  B1  NaN  NaN
K2  A2  B2   C2   D2
K3  A3  B3   C3   D3
~~~
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
~~~python
     A    B   C   D
K2   A2   B2  C2  D2
K3   A3   B3  C3  D3
K4  NaN  NaN  C4  D4
K5  NaN  NaN  C5  D5
~~~ 
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
~~~python
    A   B   C   D
K2  A2  B2  C2  D2
K3  A3  B3  C3  D3
~~~ 
- 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
~~~python
     A    B    C    D
K0   A0   B0  NaN  NaN
K1   A1   B1  NaN  NaN
K2   A2   B2   C2   D2
K3   A3   B3   C3   D3
K4  NaN  NaN   C4   D4
K5  NaN  NaN   C5   D5
~~~