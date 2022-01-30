# 과제 1
# 다음의 파일 3개를 로드하고(1), 각 파일의 행과 열의 개수를 출력(2)해보세요.
# 이 때, 파일의 구분자를 잘 확인하여 로드해보세요.
import pandas as pd
import os
os.chdir('./day1')

df_1 = pd.read_csv('./data/test_csv_file.csv')
print(df_1)

df_2 = pd.read_csv('./data/test_text_file.txt', sep='|')
print(df_2)

df_3 = pd.read_csv('./data/text_without_column_name.txt', sep='|')
print(df_3)

# 다음의 파일을 로드하는데, 다음의 제약사항을 지켜 로드해보세요
# 첫번째 행은 빼고 상위 5개의 행(2, 3, 4, 5, 6)만 로드
# PassengerId 컬럼을 Index column 으로 지정
# 가장 상위 row 를 header 로 지정
# ?, ??, N/A, nan, NaN 을 결측값으로 지정

df = pd.read_csv('./data/train.csv',
                 header=0,
                 skiprows=[1],
                 nrows=5,
                 index_col="PassengerId",
                 na_values=["?", "??", "N/A", "nan", "NaN"])
print(df)

# 과제 2
# 다음의 데이터를 DataFrame 으로 생성 후 csv file 로 만들어 보세요
# 이 때, 아래의 제약조건을 to_csv 함수 내에서 설정하여 만들어 보세요
# 소수점은 둘째자리까지만 설정해주세요
# X3 컬럼은 빼주세요

data = pd.DataFrame(data={'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
                          'X1': [1, 2, 3, 4, 5],
                          'X2': [3.0132, 4.532, 3.2113, 4.023, 3.543],
                          'X3': ['my', 'name', 'is', 'jaehun', 'heo']})


data.to_csv('./data/data_df_x2.csv',
            sep=',',
            na_rep='NaN',
            float_format="%0.2f",
            columns=['ID', 'X1', 'X2'],
            index=False)

# 과제 3
# 다음의 데이터를 로드해 보세요
import numpy as np
idx = ['r0', 'r1', 'r2', 'r3', 'r4']
df = pd.DataFrame({'class_1': ['a', 'a', 'b', 'b', 'c'],
                   'var_1': np.arange(5),
                   'var_2': np.random.randn(5)},
                  index=idx)

print(df.loc[['r0', 'r1']])
print(df.loc[:, ['class_1', 'var_1']])
