## day 1 mission 
### 과제 1
- 다음의 파일 3개를 로드하고(1), 각 파일의 행과 열의 개수를 출력(2)해보세요.  
  이 때, 파일의 구분자를 잘 확인하여 로드해보세요.
  - [test_csv_file.csv](https://github.com/koni114/rfriend-python-study/blob/main/day1/data/test_csv_file.csv)
  - [test_text_file.txt](https://github.com/koni114/rfriend-python-study/blob/main/day1/data/test_text_file.txt)
  - [text_without_column_name.txt](https://github.com/koni114/rfriend-python-study/blob/main/day1/data/text_without_column_name.txt)
- 다음의 파일을 로드하는데, 다음의 제약사항을 지켜 로드해보세요
  - [train.csv](https://github.com/koni114/rfriend-python-study/blob/main/day1/data/train.csv)
  - 첫번째 행은 빼고 상위 5개의 행(2, 3, 4, 5, 6)만 로드
  - PassengerId 컬럼을 Index column 으로 지정
  - 가장 상위 row 를 header 로 지정
  - `?`, `??`, `N/A`, `nan`, `NaN` 을 결측값으로 지정


### 과제 2
- 다음의 데이터를 DataFrame으로 생성 후 csv file로 만들어 보세요  
  이 때, 아래의 제약조건을 `to_csv` 함수 내에서 설정하여 만들어 보세요
  - 소수점은 둘째자리까지만 설정해주세요
  - X3 컬럼은 빼주세요
~~~python
data = {'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'X1': [1, 2, 3, 4, 5],
        'X2': [3.0132, 4.532, 3.2113, 4.023, 3.543],
        'X3': ['my', 'name', 'is', 'jaehun', 'heo']}
~~~
- 위의 DataFrame 의 다음의 attirbute를 조회해 보세요
  - transpose
  - 행과 열 이름
  - dataFrame의 데이터 형태
  - 행과 열의 개수를 튜플로 반환

### 과제 3
- 다음의 데이터를 로드해 보세요
~~~python
{'class_1': ['a', 'a', 'b', 'b', 'c'],
            'var_1': np.arange(5),
            'var_2': np.random.randn(5)}
~~~
- 'r0' ,'r1' ,'r2', 'r3', 'r4' 문자열을 index 로 지정하세요
- 'r0', 'r1' index 행만 선택하여 출력해보세요
- 'class_1', 'var_2' 컬럼만 선택하여 출력해보세요