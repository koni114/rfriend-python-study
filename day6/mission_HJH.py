# 과제 1
# 다음의 데이터를 로드해보세요
import pandas as pd
import numpy as np
df = pd.DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
                   'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
                   'grade': ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
                   'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})

# 아래와 같은 구조로 변경해보세요 (-- 1)
df_pivot_table = pd.pivot_table(data=df, index=['cust_id'], columns=['prod_cd'])
print(df_pivot_table)

# 아래와 같은 구조로 변경해보세요 (-- 2)
df_pivot_table = pd.pivot_table(data=df, index=['cust_id', 'grade'], columns=['prod_cd'])
print(df_pivot_table)

# 아래와 같은 구조로 변경해보세요 (-- 3)
df_pivot_table = pd.pivot_table(data=df, index=['grade'], columns=['prod_cd'], aggfunc=np.sum, margins=True)
print(df_pivot_table)

# 과제 2
# 다음의 데이터를 로드해보세요
mul_index = pd.MultiIndex.from_tuples([('cust_1', '2015'), ('cust_1', '2016'),
                                       ('cust_2', '2015'), ('cust_2', '2016')])

data = pd.DataFrame(data=np.arange(16).reshape(4, 4),
                    index=mul_index,
                    columns=['prd_1', 'prd_2', 'prd_3', 'prd_4'],
                    dtype='int')
data.loc[['cust_2'], ['prd_4']] = np.nan

# 아래와 같은 구조로 변경해보세요 (-- 1). 이를 result_df 로 저장해보세요
result_df = data.stack(dropna=False)
print(result_df)

# 저장한 result_df를 다음과 같이 변경해보세요
result_df_unstacked = result_df.unstack(level=1)

# 과제 3
# 다음의 데이터를 로드해주세요
data = pd.DataFrame({'cust_ID': ['C_001', 'C_001', 'C_002', 'C_002'],
                     'prd_CD': ['P_001', 'P_002', 'P_001', 'P_002'],
                     'pch_cnt': [1, 2, 3, 4],
                     'pch_amt': [100, 200, 300, 400]})

# 아래와 같은 구조로 변경해주세요(-- 1)
df_melt = pd.melt(data,
                  id_vars=['cust_ID', 'prd_CD'],
                  value_vars=['pch_cnt', 'pch_amt'],
                  value_name='pch_value',
                  var_name=['pch_CD'])

# 과제 4
# 다음의 데이터를 로드해주세요
data_wide = pd.DataFrame({"C1prd1": {0: "a", 1: "b", 2: "c"},
                          "C1prd2": {0: "d", 1: "e", 2: "f"},
                          "C2prd1": {0: 2.5, 1: 1.2, 2: .7},
                          "C2prd2": {0: 3.2, 1: 1.3, 2: .1},
                          "value": dict(zip(range(3), np.random.randn(3)))})

# 아래와 같은 구조로 변경해주세요(-- 1)
df_wide_to_long = pd.wide_to_long(data_wide,
                                  stubnames=['C1', 'C2'],
                                  i=['seq_no'],
                                  j='prd')

print(df_wide_to_long.index)
print(df_wide_to_long.columns)

# 과제 5
import pandas as pd
data = pd.DataFrame({'id': ['id1', 'id1', 'id1', 'id2', 'id2', 'id3'],
                     'fac_1': ['a', 'a', 'a', 'b', 'b', 'b'],
                     'fac_2': ['d', 'd', 'd', 'c', 'c', 'd']})

# 아래와 같은 구조로 변경해주세요(-- 1)
pd.crosstab(data.fac_1, data.fac_2)

# 아래와 같은 구조로 변경해주세요(-- 2)
pd.crosstab(data.id, [data.fac_1, data.fac_2])

# 아래와 같은 구조로 변경해주세요(-- 3)
pd.crosstab(data.id, [data.fac_1, data.fac_2], margins=True)