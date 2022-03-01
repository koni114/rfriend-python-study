# day 14
## 과제 1
import urllib
import ssl
import pandas as pd
import numpy as np
# 다음의 데이터를 abalone 변수에 로드해보세요. 데이터는 다음의 특징을 가지고 있습니다.
# - url: https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data
# - Column name list: ['sex', 'length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings']
# - header 는 없음

pd.set_option("display.max_columns", 100)
context = ssl._create_unverified_context()
downloaded_data = urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data",
                                        context=context)

abalone = pd.read_csv(downloaded_data,
                      names=['sex', 'length', 'diameter', 'height', 'whole_weight', 'shucked_weight', 'viscera_weight', 'shell_weight', 'rings'],
                      header=None)


# 다음의 조건을 만족하는 length_cat 이라는 범주형 변수를 추가하세요.
# length 값이 length 의 중앙값보다 크거나 같으면, length_long, 중앙값보다 작으면 length_short
abalone["length_cat"] = np.where(abalone["length"] >= np.median(abalone["length"]), "length_long", "length_short")

# sex 와 length_cat 그룹별로 whole_weight 의 크기(size), 평균(mean), 표준편차(std), 최소값(min), 최대값(max)을 구해보세요.
# 다음과 같은 결과값이 나와야 하며 리스트(List)를 사용해야 합니다.
stat_list = ["size", "mean", "std", "min", "max"]
abalone[["sex", "length_cat", "whole_weight"]].groupby(["sex", "length_cat"]).agg(stat_list)

# sex, length_cat 그룹별로 whole_weight, shell_weight의 두 개의 칼럼에 대해서 크기(size), 평균(mean), 표준편차(std), 최소값(min), 최대값(max)을 구해보세요.
# 다음과 같은 결과값이 나와야합니다.
# 해당 결과를 groupby_result 에 저장하세요
stat_dict ={"whole_weight": ["size", "mean", "std", "min", "max"],
            "shell_weight": ["size", "mean", "std", "min", "max"]}

groupby_result = abalone[["sex", "length_cat", "whole_weight", "shell_weight"]].groupby(["sex", "length_cat"]).agg(stat_list)

# groupby_result 에서 성별이 M인 경우를 출력해보세요
print(groupby_result.loc["M"])

# groupby_result 에서 성별이 M이고 shell_weight 인 경우를 출력해보세요
print(groupby_result.loc["M", "shell_weight"])

# sex 와 length_cat 그룹별로 whole_weight 컬럼은 크기(size), 평균(mean), 표준편차(std) 를,
# shell_weight 는 최대 최소 범위(range)와 IQR(iqr) 을 구헤보세요.
# 이 때 range 컬럼명은 Range 로, IQR 컬럼명은 Inter-Quartile_Range 이어야 합니다.


def range_val(x):
    x_min = np.min(x)
    x_max = np.max(x)
    x_range = x_max - x_min
    return x_range


def iqr_val(x):
    q1, q3 = np.quantile(x, (0.25, 0.75))
    return q3 - q1


stat_dict = {"whole_weight": ["size", "mean", "std"],
             "shell_weight": [("Range", range_val), ("Inter-Quartile_Range", iqr_val)]}


groupby_result = abalone[["sex", "length_cat", "whole_weight", "shell_weight"]].groupby(["sex", "length_cat"]).agg(stat_dict)
print(groupby_result)

# 과제 2
# 다음의 데이터프레임을 로드해주세요
import numpy as np
import pandas as pd

df = pd.DataFrame({'grp_col_1': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'],
                   'grp_col_2': ['c', 'c', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'f'],
                   'val_1': np.arange(10),
                   'val_2': np.random.randn(10)})


def stat_func(x):
    d = {}
    d["val_1_mean"] = np.mean(x['val_1'])
    d["val_1_std"] = np.std(x["val_1"])
    d["val_2_max"] = np.max(x["val_2"])
    d["val_2_min"] = np.min(x["val_2"])
    d["val_2_range"] = range_val(x["val_2"])
    return pd.Series(d, index=["val_1_mean", "val_1_std", "val_2_max", "val_2_min", "val_2_range"])


df.groupby(["grp_col_1", "grp_col_2"]).apply(stat_func)

# 위의 결과는 계층적 인덱스로 결과가 도출되는데, 이 인덱스를 컬럼으로 변환하여 출력해보세요
# 다음의 결과가 도출되어야 합니다.
df.groupby(["grp_col_1", "grp_col_2"]).apply(stat_func).reset_index()

# 과제 3
# 다음의 데이터를 로드해주세요

import pandas as pd
import numpy as np

df = pd.DataFrame({'grp_col': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'],
                   'val': np.arange(10)+1,
                   'weight': [0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.4]})

# grp_col 을 기준으로 그룹별 객체를 만들어 grouped 변수에 저장해보세요.
grouped = df.groupby("grp_col")

# grouped 변수를 가지고, weight 컬럼을 가중평균 계수로하는 val 값의 그룹별 가중평균을 구해보세요
weighted_avg_func = lambda g:np.average(g['val'], weights=g["weight"])
grouped.apply(weighted_avg_func)

# 과제 4
# 다음의 데이터를 로드해주세요
import pandas as pd
import numpy as np

np.random.seed(123)

df = pd.DataFrame({'grp': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                   'col_1': np.random.randn(8),
                   'col_2': np.random.randn(8)})

df.loc[[1, 6], ['col_1', 'col_2']] = np.nan

# Groupby Operator, lambda 함수, apply 함수를 사용해서,
# grp 그룹별 평균값으로 결측치를 채워(imputation, = 보간)해보세요
fill_mean_func = lambda g: g.fillna(g.mean())
df.groupby("grp").apply(fill_mean_func)

# 과제 5
# 다음의 데이터를 로드해주세요
import numpy as np
import pandas as pd
from pandas import DataFrame

df = DataFrame({'group_1': ['a', 'a', 'a', 'a', 'a',
                            'b', 'b', 'b', 'b', 'b',],
                'group_2': ['c', 'c', 'c', 'd', 'd',
                            'e', 'e', 'e', 'f', 'f'],
                'col': [1, 2, np.NaN, 4, np.NaN,
                        6, 7, np.NaN, 9, 10]})

# GroupBy() 로 group_1과 group_2 칼럼을 모두 적용한 그룹을 만들어 보세요
# [그룹 ('a', 'c'), 그룹 ('a', 'd'), 그룹 ('b'e, 'e'), 그룹 ('b', 'f')]
grouped = df.groupby(['group_1', 'group_2'])

df["count"] = grouped.col.transform("count")
df["sum"] = grouped.col.transform("sum")
df["max"] = grouped.col.transform("max")







