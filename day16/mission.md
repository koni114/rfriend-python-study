## day 16 
### 과제 1
- 다음의 코드를 로드해주세요
~~~python
import numpy as np
a = np.arange(-5, 5)
~~~
- 위의 a 배열에서 <b>0보다 작은 수는 0으로 변환하고 나머지는 그대로 두는 코드를 작성해보세요</b>
  - (1) List Comprehension 을 활용하여 코드를 작성해보세요
  - (2) indexing 을 활용해서 코드를 작성해보세요(hint: a[a<0]) 
  - (3) np.where 을 활용해서 코드를 작성해보세요
  - (4) np.clip 을 활용해서 코드를 작성해보세요

### 과제 2
- 다음의 코드를 로드해주세요
~~~python
import numpy as np
a = np.arange(24).reshape(4, 3, 2)
~~~
- 배열(a) 에 차원을 추가해보세요
  - (1) `numpy.reshape()` 을 이용한 차원 추가
  - (2) `numpy.expand_dims()` 을 이용한 차원 추가
  - (3) `numpy.newaxis` 을 이용한 차원 추가 

### 과제 3
- 현재 경로를 확인하세요
- 현재 경로 안에 들어있는 파일 리스트를 확인해보세요
- 작업경로를 바꿔보세요
- 기존 경로에 `test` 라는 디렉토리 이름을 합쳐 하위 경로를 만들어보세요
- `test`라는 새로운 폴더를 만들어보세요
- `/Users/heojaehun/gitRepo/` 라는 경로가 있는지 확인해보세요
- `/Users/heojaehun/gitRepo/test` -> `/Users/heojaehun/gitRepo/test2` 로 변경해보세요
- `/Users/heojaehun/gitRepo/test` 에 `test1.txt`, `test2.txt`, `test3.txt` 를 만들고 이를 `/Users/heojaehun/gitRepo/test2` 에 복사해보세요
- `/Users/heojaehun/gitRepo/test2` 에 들어있는 파일들을 전부 삭제하고, 디렉토리도 삭제해보세요 

### 과제 4
- 다음의 데이터를 로드해보세요
~~~python
import pandas as pd
import numpy as np

df = pd.DataFrame({"id": ["A_001", "A_002", "A_003",
                          "B_001",  "C_001", "C_002"],
                   "val": np.arange(6)})
~~~
- 컬럼 `id`을 구분자(seperator) `_` 를 기준으로 `str.split('_')` 메소드를 사용하여 분할(split)한 후에, 앞부분([0])을 가져다가 `grp` 라는 칼럼을 추가하여 만들어보세요

### 과제 5
- 다음의 데이터를 로드해보세요
~~~python
df = pd.DataFrame({"grp": ['A', 'A' , 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
                   "val": [1, 2, np.nan, 4, np.nan, np.nan, 7, 8, 9]})

s = pd.Series([1, 2, np.nan, 4, np.nan, np.nan, 7, 8, 9])
~~~
- dataframe 과 series 를 비교해가면서 수행해보세요
  - (1) 행의 개수를 세어보세요 
  - (2) Series 에서 `count()` 와 `size()` 의 차이는 무엇인가요? 


