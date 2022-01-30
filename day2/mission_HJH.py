# 과제 1
# 다음의 데이터를 로드하세요
import pandas as pd
import numpy as np
idx = ['r0', 'r1', 'r2', 'r3', 'r4']
df = pd.DataFrame({
    'c1': np.arange(5),
    'c2': np.random.randn(5)},
    index=idx)

# [r3, r4]를 빼고, [r5, r6]을 새로 추가해보세요. 이때 값들은 전부 0으로 채워주세요
# 아래와 비슷한 결괏값이 나와야 합니다.

idx = ['r0', 'r1', 'r2', 'r5', 'r6']
new_df = df.reindex(idx, fill_value=0)
print(new_df)

# 다음의 결괏값이 나오도록 dataFrame 을 만들어주세요
# 이 때, index 는 다음과 같은 시계열 데이터이여야 합니다.
date_list = pd.date_range('2022-01-25', periods=5, freq='D')
df_2 = pd.DataFrame({"c1": [10, 20, 30, 40, 50]}, index=date_list)
print(df_2)

# 위의 dataFrame 에서 2022-01-20 ~ 2022-01-24 날짜의 데이터를 추가하고
# 이 때 가장 최근(2022-01-25)의 데이터로 값을 채워주세요

date_idx_2 = pd.date_range("2022-01-20", periods=10, freq="D")
df_2.reindex(date_idx_2, method='bfill')

# 위의 dataFrame 에서 2022-01-30 ~ 2022-01-31 날짜의 데이터를 추가하고
# 이 때 가장 최근(2022-01-29)의 데이터로 값을 채워주세요

date_idx_3 = pd.date_range("2022-01-25", periods=7, freq="D")
df_2.reindex(date_idx_3, method='ffill')

# 과제 2
# 해당 데이터를 로드해 보세요
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

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
df_1_2 = pd.concat([df_1, df_2], axis=0)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
df_1_3 = pd.concat([df_1, df_3], axis=1)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
df_1_4 = pd.concat([df_1, df_4], axis=0)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
df_1_5 = pd.concat([df_1, df_4], axis=0, join='inner')

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 5)
df_1_6 = pd.concat([df_1, df_4], axis=1)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 6)
df_1_7 = pd.concat([df_1, df_4], axis=1, join='inner')

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 7)
df_1_8 = pd.concat([df_1, df_4], axis=1).reindex(df_1.index)

# 과제 3
# 해당 데이터를 로드해 보세요
# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'D': ['D0', 'D1', 'D2']},
                    index=[0, 1, 2])

S = pd.Series(['S1', 'S2', 'S3'], name='S')
df_1_s = pd.concat([df_1, S], axis=1)
print(df_1_s)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
S = pd.Series(['S1', 'S2', 'S3', 'S4'], index=['A', 'B', 'C', 'E'])
df_1.append(S, ignore_index=True)

# 과제 4
# 해당 데이터를 로드해 보세요
df_left = pd.DataFrame({'KEY': ['K0', 'K1', 'K2', 'K3'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})

df_right = pd.DataFrame({'KEY': ['K2', 'K3', 'K4', 'K5'],
                         'C': ['C2', 'C3', 'C4', 'C5'],
                         'D': ['D2', 'D3', 'D4', 'D5']})

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
df_1 = pd.merge(df_left, df_right, how='left', on='KEY')
print(df_1)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
df_2 = pd.merge(df_left, df_right, how='right', on='KEY')
print(df_2)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
df_3 = pd.merge(df_left, df_right, how='inner', on='KEY')
print(df_3)

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
df_4 = pd.merge(df_left, df_right, how='outer', on='KEY', indicator='indicator_info')
print(df_4)

# 과제 5
df_left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']},
                       index=['K0', 'K1', 'K2', 'K3'])

df_right = pd.DataFrame({'C': ['C2', 'C3', 'C4', 'C5'],
                         'D': ['D2', 'D3', 'D4', 'D5']},
                        index=['K2', 'K3', 'K4', 'K5'])

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 1)
df_5_1 = pd.merge(df_left, df_right,
                  left_index=True, right_index=True,
                  how='left')

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 2)
df_5_2 = pd.merge(df_left, df_right,
                  left_index=True, right_index=True,
                  how='right')

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 3)
df_5_3 = pd.merge(df_left, df_right,
                  left_index=True, right_index=True,
                  how='inner')

# 위의 데이터를 활용하여 아래처럼 만들어보세요(-- 4)
df_5_4 = pd.merge(df_left, df_right,
                  left_index=True, right_index=True,
                  how='outer')
