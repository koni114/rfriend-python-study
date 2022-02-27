# day 13
# 과제 1
# 다음의 데이터 abalone.txt 를 로드해서 abalone 변수에 저장해주세요.
# 해당 데이터는 day13 directory 아래 존재합니다.

# abalone 데이터에서 length_cat 컬럼을 추가해주세요. 생성 조건은 다음과 같습니다
import pandas as pd
import os
os.getcwd()
abalone = pd.read_csv('./abalone.txt',
                      sep=',',
                      names=['sex', 'length', 'diameter', 'height',
                             'whole_weight', 'shucked_weight', 'viscera_weight',
                             'shell_weight', 'rings'],
                      header=None,
                      )

# abalone 데이터에서 length_cat 컬럼을 추가해주세요. 생성 조건은 다음과 같습니다.
# length 의 값이 중앙값 보다 크면 length_long, 작거나 같으면 length_short 로 편성해주세요.
import numpy as np
abalone['length_cat'] = np.where(abalone['whole_weight'] > np.median(abalone['whole_weight']),
                                 'length_long',
                                 'length_short')

# abalone 데이터셋을 성별(sex)로 GroupBy를 한 후에, for loop 를 돌려
#     그룹 이름(sex: 'F', 'I', 'M') 별로 출력해주세요
# 각 그룹별 데이터셋은 최대 5개까지 출력해주세요. 다음과 같은 결과값이 출력되어야 합니다.

for (sex, group_data) in abalone[['sex', 'length_cat', 'whole_weight', 'rings']].groupby('sex'):
    print(sex)
    print(group_data[:5])

# abalone 데이터셋을 두 개의 범주형 변수(sex, length_cat)를 사용하여
# for loop 반복문으로 그룹 이름(sex 와 length_cat 의 조합)과 각 그룹별 데이터셋을 출력해보세요
# 다음과 같은 결과값이 출력되어야 합니다.

for (sex, length_cat), group_data in abalone[['sex', 'length_cat', 'whole_weight', 'rings']].groupby(['sex', 'length_cat']):
    print(sex, length_cat)
    print(group_data[:5])

# abalone 데이터셋을 성별 그룹('F', 'I', 'M')을 key 로 하고, 데이터셋을 value 로 하는 dict 를 만들어보세요

abalone_dict = dict()
abalone_dict = dict(list(abalone.loc[:10, ['sex', 'length_cat', 'whole_weight', 'rings']].groupby('sex')))
print(abalone_dict)

# 과제 2
# 다음의 데이터를 로드해주세요

import pandas as pd
from pandas import DataFrame

df = DataFrame({'name': ['kim', 'KIM', 'Kim', 'lee', 'LEE', 'Lee', 'wang', 'hong'],
                'value': [1, 2, 3, 4, 5, 6, 7, 8],
                'value_2': [100, 300, 200, 100, 100, 300, 50, 80]
                })

name_2_dict = {'kim': 'kim',
               'KIM': 'kim',
               'Kim': 'kim',
               'lee': 'lee',
               'LEE': 'lee',
               'Lee': 'lee',
               'wang': 'others',
               'hong': 'others'}

func = lambda x: name_2_dict.get(x, x)

df['name_2'] = df['name'].apply(func)
print(df)

# 위의 도출된 데이터를 기반으로, name_2 컬럼별 합계(value_2) 을 도출해보세요
# 다음과 같은 결과값이 도출되어야 합니다.
df[['name_2', 'value', 'value_2']].groupby(['name_2']).sum()

# 과제 3
# 다음의 데이터를 로드해보세요
import pandas as pd
df = pd.DataFrame({'id': [1, 2, 10, 20, 100, 200],
                   'name': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']})

df['id_2'] = df['id'].apply(lambda x: "{:0>5d}".format(x))

# 새로 만든 id_2 변수와 name 변수를 각 원소별로 합쳐서 데이터프레임 안에 새로운 변수 id_name 만들어보세요
# 다음과 같은 결과값이 도출되어야 합니다.
df['id_name'] = df[['id_2', 'name']].apply(lambda x: '_'.join(x), axis=1)

# 과제 4
# 다음의 데이터를 로드해주세요
df = DataFrame(data=np.arange(20).reshape(4, 5),
               columns = ['c1', 'c2', 'c3', 'c4', 'c5'],
               index = ['r1', 'r2', 'r3', 'r4'])

# dict, Series, list 와 groupby 를 적절히 활용하여 다음의 결과를 도출해보세요
groupby_dict = {'r1': 'row_g1',
                'r2': 'row_g1',
                'r3': 'row_g2',
                'r4': 'row_g2'}

df.groupby(groupby_dict).sum()

# dict, Series, list 와 groupby 를 적절히 활용하여 다음의 결과를 도출해보세요
groupby_dict = {'c1': 'col_g1',
                'c2': 'col_g1',
                'c3': 'col_g2',
                'c4': 'col_g2',
                'c5': 'col_g2'}

df.groupby(groupby_dict, axis=1).sum()

# dataFrame 과 multiIndex 를 활용하여 다음의 hier_df dataFrame 을 만들어보세요
hier_columns = pd.MultiIndex.from_arrays([['col_g1', 'col_g1', 'col_g2', 'col_g2', 'col_g2'],
                                         ['c1', 'c2', 'c3', 'c4', 'c5']],
                                         names=['col_level_1', 'col_level_2'])

hier_df = pd.DataFrame(data=np.arange(20).reshape(4, 5),
                       columns=hier_columns,
                       index=['r1', 'r2', 'r3', 'r4'])

print(hier_df)

# 과제 5
# 다음의 데이터를 로드해주세요
df = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b'],
                   'value_1': np.arange(6),
                   'value_2': np.random.randn(6)})

# group 별 non-NA 개수를 도출해보세요
df.groupby('group').size()

# group 별 non-NA 합을 도출해보세요
df.groupby('group').sum()

# group 별 non-NA 최소값을 도출해보세요
df.groupby('group').max()

# group 별 non-NA 1분위수를 도출해보세요
df.groupby('group').quantile(0.25)
