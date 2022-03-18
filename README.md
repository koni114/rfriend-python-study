# rfriend-python-study
- rfriend 블로그 내 python 내용을 기반으로 study 
- [rfriend 블로그](https://rfriend.tistory.com/250?category=675917) 

### 생각
- python pandas library 등, 데이터 전처리 및 python language 의 감을 놓치지 않도록 조금씩 매일 연습 및 정리할 예정
- 혼자 하는 것이 아니라 study 원을 구해서 함께 과제도 만들어보고, 과제를 풀어보는 형식으로!

### 방식
- 2일에 1번, 블로그 10개씩 진행(총 230개) 약 50일
- 데이터 전처리 -> 그래프_시각화 -> 통계분석 -> 기계학습 -> 프로그래밍 순으로 진행
- 블로그 10개 내용에 대한 과제 5문제를 만들고, 이에 대해서 study 원들이 과제에 대한 답 제출
- 답 제출은 2일 기준 자정까지 제출!  

### 폴더 구조
```
├── README.md
├── checklist.md : 과제에 대한 study 원들의 제출 내역을 정리
├── script : 기타 스크립트 파일. 과제를 풀어가면서 Tip 등을 개인적으로 업로드
    └── day1_tips_HJH.py     
└── day1 :  
    └── mission.md : day1에 대한 과제 내역
    └── mission_HJH.md : HJH이 제출한 과제 정답
```

### 날짜별 python Contents 정리
```
├──day1
    └── pd.read_csv, pd.DataFrame 생성, 행, 컬럼 선택 방법
├──day2
    └── df.reindex, pd.date_range, pd.concat
    └── pd.merge(특정 컬럼기반, index 기반)
├──day3
    └── df.isnull, df.sum, df.mean, df.std
    └── np.where, df.dropna, pd.Series.interporlate
├──day4
    └── pd.Series.replace, pd.duplicated, pd.drop_duplicates
    └── pd.Series.unique, pd.Series.value_counts
    └── scipy.stats, StandardScaler
    └── np.set_printoptions
    └── RobustScaler
├──day5
    └── MinMaxScaler, Binarizer, binarize
    └── OneHotEncoder, np.linspace, np.digitize
    └── pd.get_dummies vs OneHotEncoder
    └── PolynomialFeatures
├──day6
    └── pd.pivot_table, pd.stack, pd.unstack
    └── pd.melt, pd.crosstab
``` 