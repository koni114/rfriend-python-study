## day 12
### 과제 1
- 다음의 데이터를 `day12` 디렉토리 밑에 NumPy format의 `x_save.npy` 라는 바이너리 파일로 저장해주세요
~~~python
import numpy as np
import os
x = np.arange(5)
~~~
- 다음의 위에 저장한 `x_save.npy` 파일을 로드해 출력해보세요
- 다음의 데이터를 `xy_savez.npz` 포맷 파일로 저장해보세요
~~~python
import numpy as np
import os
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])
~~~
- 다음의 저장한 `xy_savez.npz` 포맷 파일을 로드해서 `x`, `y`를 출력해보세요
- 다음의 데이터를 아래 포멧의 text file을 `xy_save.txt`로 저장해 주세요
~~~python
import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 6, 7, 8, 9])
~~~
~~~t
# --xy save start--
0.00 1.00 2.00 3.00 4.00
5.00 6.00 7.00 8.00 9.00
# --xy save end--
~~~

### 과제 2
- 다음의 데이터를 로드해보시고, 아래와 같은 결과를 도출해보세요  
  2가지 이상의 방법을 통해서 도출해보세요
~~~python
import numpy as np
x = np.arange(18).reshape(3, 6)
~~~
~~~
Out[4]:
[array([[ 0, 1],
         [ 6, 7],
         [12, 13]]), 
 array([[ 2, 3],
         [ 8, 9],
         [14, 15]]), 
 array([[ 4, 5],
         [10, 11],
         [16, 17]])]
~~~
- 다음의 데이터를 로드해보시고, 아래와 같은 결과를 도출해보세요  
  2가지 이상의 방법을 통해서 도출해보세요
~~~python
x = np.arange(18).reshape(3, 6)
~~~
~~~
Out[14]:
[array([[0, 1, 2, 3, 4, 5]]),
 array([[ 6, 7, 8, 9, 10, 11]]),
 array([[12, 13, 14, 15, 16, 17]])]
~~~

### 과제 3
- 이번 과제는 선형 대수(Linear Algebra)입니다. 디음의 문제를 선형 대수 함수를 사용하여 풀어보세요
- 다음과 같은 단위행렬을 만들어보세요
~~~
[[1. 0. 0. 0.] 
 [0. 1. 0. 0.] 
 [0. 0. 1. 0.] 
 [0. 0. 0. 1.]]
~~~
- 다음의 데이터를 사용해서 다음과 같은 행렬을 만들어보세요  
  대각성분을 이용해야 합니다.
~~~python
x = np.arange(9).reshape(3, 3)
~~~
~~~
array([[0, 0, 0],
       [0, 4, 0],
       [0, 0, 8]])
~~~
- 다음의 데이터를 원소간 곱(element-wise product: a*b)과 내적(dot product) 통해 결과를 도출해보세요
~~~python
a = np.arange(4).reshape(2, 2)
~~~  
~~~
Out[8]:
array([[0, 1],
       [4, 9]])
~~~
~~~
Out[9]:
array([[ 2, 3],
       [ 6, 11]])
~~~
- 다음의 데이터의 대각합을 구하여 결과를 도출해보세요
~~~python
c = np.arange(27).reshape(3, 3, 3)
~~~
~~~
Out[17]: array([36, 39, 42])
~~~
- 다음 데이터의 행렬식(Determinant) 값을 구해보세요
~~~python
d = np.array([[1, 2], [3, 4]])
~~~
- 다음 데이터의 역행렬을 구해보세요
~~~python
a = np.array(range(4)).reshape(2, 2)
~~~
- 다음 데이터의 고유값(eigenvalue)과 고유벡터(eigenvector)를 구해보세요
~~~python
e = np.array([[4, 2],[3, 5]])
~~~
- 다음 데이터의 특이값 분해(svd)를 구해보세요
~~~python
A = np.array([[3,6], [2,3], [0,0], [0,0]])
~~~
- 다음의 연립방정식의 해를 구해보세요
~~~
4x0 + 3x1 = 23
3x0 + 2x1 = 16
~~~
~~~python
a = np.array([[4, 3], [3, 2]])
b = np.array([23, 16])
# x 변수에 두 연립방정식의 해를 구해보세요 
~~~
- 구한 두 연립방정식의 해가 맞는지 검증해보세요
- 다음의 데이터가 주어져있습니다. (x, y 좌표값)  
  해당 데이터를 최소자승법(LSM)을 사용하여 잔차 제곱합을 최소로 하는 회귀계수를 추정해보고,   
  해당 데이터와 회귀적합선을 PLOT으로 그려보세요
~~~python
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
~~~

### 과제 4
- 해당 범주형 데이터를 아래와 같이 One-Hot encoding 형태로 전처리해보세요
~~~python
music_df = pd.DataFrame({'music_id': [1, 2, 3, 4, 5],
                         'music_genre': ['rock',
                                         'disco',
                                         'pop',
                                         'rock',
                                         'pop']})
~~~
~~~python
# One-hot encoding 전처리 결과 
Out[7]:
   music_id  music_genre      genre_disco     genre_pop        genre_rock
0       1       rock                0               0                1
1       2       disco               1               0                0
2       3       pop                 0                1                0
3       4       rock                0                0                1
4       5       pop                 0                1                0
~~~
- 아래 주어진 데이터를 기반으로 One-Hot encoding 을 수행하는 예제입니다  
  다음의 지시를 잘 따라하여 도출해보세요
  - 수직바(`|`) 로 구분되어 있는 `music_genre` 컬럼에서 `|` 를 기준으로 잘라 음악 장르 범주 값들을 원소로 가지는 하나의 집합(set)을 만들어보세요  
  `music_genre_set` 변수에 저장해야 합니다.
  - `music_multi_df`의 행 개수만큼 행과 `music_genre_set`의 개수만큼의 열을 가지는 0으로 채워진 dataframe 을 만들어보세요  
  해당 dataframe을 `indicator_mat` 에 저장해주세요 
  - `indicator_mat` 데이터 프레임에 각 행별로 해당하는 음악 장르를 1로 채워 넣어 One-Hot encoding 을 완성하세요
  - 기존의 `music_multi_df` dataFrame 과 `indicator_mat` 를 합쳐서 완성해주세요

### 과제 5
- 다음의 바다 해산물 전복(abalone) 데이터를 입니다.  
  해당 데이터를 잘 조사하여, 다음과 같은 결과값을 도출해보세요
  - 다음은 전복의 성별과 전복의 길이를 범주형 데이터로 처리하여 추가한 컬럼 `length_cat` 을 이용하여 성별 별 length_cat 의 평균치를 구한 결과입니다.
  - `length_cat` 은 `abalone.length` 의 평균 값보다 크면 `length_long`, 작거나 같으면 `length_short` 로 구분해야 합니다.