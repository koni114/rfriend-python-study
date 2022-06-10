# 데이터 프레임에 그룹 단위 통계량 컬럼 추가하기.
import shutil

import numpy as np
import pandas as pd

df = pd.DataFrame({"group_1": ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b'],
                   "group_2": ['c', 'c', 'c', 'd', 'd', 'e', 'e', 'e', 'f', 'f'],
                   "col": [1, 2, np.NaN, 4, np.NaN, 6, 7, np.NaN, 9, 10]})

df["count_col"] = df.groupby(["group_1", "group_2"]).col.transform("count")
df["sum_col"] = df.groupby(["group_1", "group_2"]).col.transform("sum")

# 동일 길이를 나누어서 범주 만들기. pd.cut()
# 동일 개수로 나누어서 범주 만들기  pd.qcut()

np.random.seed(123)
df = pd.DataFrame({"col_1": np.random.randint(20, size=20),
                   "col_2": np.random.randn(20)})

# (1) pd.cut: 동일 길이로 나누어서 범주 만들기.
factor_col_1 = pd.cut(df.col_1, 4)
grouped_col_1 = df.col_1.groupby(factor_col_1)
grouped_col_1.agg(["count", "mean", "std", "min", "max"])


def summary_func(group):
    return {"count": group.count(),
            "mean": group.mean(),
            "std": group.std(),
            "min": group.min(),
            "max": group.max()}


grouped_col_1.apply(summary_func).unstack()

bucket_qcut_col_2 = pd.qcut(df.col_2, 4, labels=False)
labels = np.arange(4, 0, -1)
bucket_qcut_label_col_2 = pd.qcut(df.col_2, 4, labels=np.arange(4, 0, -1))
df.col_2.groupby(bucket_qcut_label_col_2).apply(summary_func).unstack()

## 그룹별 변수 간 상관관계 분석.
## Pearson correlation --> corr(), corrwith()
# --> groupby() 와 apply(lambda func) 를 함께 사용.

df = pd.DataFrame(np.random.randn(10, 4), columns=["a", "b", "c", "d"])
df["group"] = ["grp1", "grp1", "grp1", "grp1", "grp1",
               "grp2", "grp2", "grp2", "grp2", "grp2"]

df = df.set_index("group")

# corrwith --> 모든 변수 간 상관계수.
# corr     --> 두 변수 간 상관계수.

corr_with_d = lambda x: x.corrwith(x["d"])
grouped = df.groupby("group")
grouped.apply(corr_with_d)

corr_a_d = lambda g: g["a"].corr(g["d"])
grouped.apply(corr_a_d)

# 그룹 별 선형회귀모형 적합하기.
# (Group-wise Linear Regression)

from sklearn import datasets, linear_model
diabetes = datasets.load_diabetes()

diabetes_Y = pd.DataFrame(diabetes.target, columns=["target"])
diabetes_X = pd.DataFrame(diabetes.data[:, 0:3],
                          columns=["age", "sex", "bmi"])

diabetes_df = pd.concat([diabetes_Y, diabetes_X], axis=1)
diabetes_df["grp"] = np.where(diabetes_df.sex > 0, "M", "F")


def lin_regress(data, y_var, x_vars):
    """
    group_by 의 apply 에 사용할 선형회귀 모형 UDF
    """
    y = data[y_var]
    X = data[x_vars]

    linreg = linear_model.LinearRegression()

    model = linreg.fit(X, y)

    intercept = np.round(model.intercept_, 4)
    coef = np.round(model.coef_, 4)
    result = [intercept, coef]

    return result


grouped = diabetes_df.groupby("grp")
lin_reg_coef = grouped.apply(lin_regress, 'target', ["age", "bmi"])

lin_reg_coef["M"]
lin_reg_coef["F"]

# 그룹별 무작위 표본 추출.
np.random.permutation()
help(np.random.permutation)

np.random.seed(123)
df = pd.DataFrame({"grp": ["grp_1"] * 10 + ["grp_2"] * 10,
                   "col_1": np.random.randint(20, size=20),
                   "col_2": np.random.randint(20, size=20)})
print(df)


def sampling_func(data, sample_pct):
    np.random.seed(123)
    N = len(data)
    sample_n = int(len(data) * sample_pct)
    sample = data.take(np.random.permutation(N)[:sample_n])
    return sample


sample_set = df.groupby("grp", group_keys=False).apply(sampling_func, sample_pct=0.8)

print(sample_set.sort_index())
print(df.drop(df.index[sample_set.index]))

a = np.arange(-5, 5)
[0 if i < 0 else i for i in a]

a[a < 0] = 0
print(a)

np.where(a < 0, 0, a)

# np.clip(배열, 최소값 기준, 최대값 기준)
# 최소값과 최대값 조건으로 값을 기준으로 해서, 이 범위 기준을 벗어나는 값에 대해서는 일괄적으로 최소값, 최대값으로 대치해줌
a = np.arange(-5, 5)
np.clip(a, 0, 4, out=a)  # 반환되는 값을 a 에 저장

import numpy as np
a = np.arange(24).reshape(4, 3, 2)

np.reshape(a, (1, 4, 3, 2))
np.reshape(a, ((1, ) + a.shape))
a.reshape((1, ) + a.shape)

np.expand_dims(a, axis=0)
a[:, np.newaxis]

import os
os.getcwd()              # 현재 작업경로 확인하기
os.listdir(os.getcwd())  # 작업경로 안에 들어있는 파일 리스트 확인하기
os.chdir(os.getcwd())    # 작업 경로 바꾸기

# 기존 경로와 새로운 폴더 이름을 합쳐 하위 경로 만들기
base_dir = '/Users/heojaehun/gitRepo'
os.path.join(base_dir, "rfriend-python-study")

os.mkdir(os.getcwd())         # 새로운 폴더 만들기 : os.mkdir(path)
os.path.isdir(os.getcwd())    # 경로가 존재하는지 확인하기 : os.path.isdir(path)

# os.rename(src, dst) 파일이나 경로 이름 바꾸기
dst_path = os.path.join(base_dir, "os_renamed")
os.rename(os.getcwd(), dst_path)

# shutil 라이브러리를 이용한 파일 복사: shutil.copyfile(src, dst)
base_dir = '/Users/heojaehun/gitRepo'
src_dir = os.path.join(base_dir, "src_dir")
dst_dir = os.path.join(base_dir, "dst_dir")
shutil.copyfile(src_dir, dst_dir)

# 경로제거하기 --> os.rmdir(path)
# 경로 안에 파일이 있으면, OSError 발생.
# --> 디렉토리가 비어 있지 않습니다. 라고 나옴
os.rmdir(os.getcwd())

# 파일 삭제하기 : os.remove(path)
os.remove(os.path.join(os.getcwd(), "test.txt"))

# 경로와 파일을 한꺼번에 모두 삭제하기
# shutil.rmtree(os.getcwd())
