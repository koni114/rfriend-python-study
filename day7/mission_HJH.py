# 과제 1
# 다음의 데이터를 로드해 보세요
import pandas as pd
personnel_df = pd.DataFrame({'sequence': [1, 3, 2],
                             'name': ['park', 'lee', 'choi'],
                             'age': [30, 20, 40]})

# sequence 열을 기준을 오름차순 정렬을 해보세요
# 다음과 같은 결과값이 나와야 합니다.
# 이 때, 새로운 dataFrame 을 생성하지 말고, 기존 dataframe 을 정렬한 값을 도출해보세요

personnel_df.sort_values(['sequence'], inplace=True)
print(personnel_df)

# sequence 열을 기준을 내림차순 정렬을 해보세요
# 다음과 같은 결과값이 나와야 합니다.
personnel_df.sort_values(['sequence'], ascending=False, inplace=True)
print(personnel_df)

# 열 이름을 내림차순으로 정렬하여 다음과 같은 결과값을 도출해보세요
personnel_df.sort_index(1, ascending=False)

# 다음의 데이터를 로드해보세요
import numpy as np
personnel_df = pd.DataFrame({'sequence': [1, 3, np.nan],
                             'name': ['park', 'lee', 'choi'],
                             'age': [30, 20, 40]})


# 결측값을 처음에 나오도록 정렬해보세요
result_df = personnel_df.sort_values(['sequence'], na_position='first')
print(result_df.sort_index(1))

# 결측값을 제일 나중에 나오도록 정렬해보세요
result_df = personnel_df.sort_values(['sequence'], na_position='last')
print(result_df.sort_index(1))

# 다음의 데이터를 로드해보세요
personnel_tuple = [(1, 'park', 30),
                   (3, 'lee', 20),
                   (2, 'choi', 40)]

# 다음과 같은 결과값을 도출해보세요
print(sorted(personnel_tuple, key=lambda x: x[2]))

# 과제 2
## 과제 2-1
# 다음의 데이터를 로드해보세요
s = pd.Series([0, 1, 2, 3, 4])

# 다음과 같은 결과값을 도출해보세요(-- 1)
print(s[0])

# 다음과 같은 결과값을 도출해보세요(-- 2)
print(s[:3])

# 다음과 같은 결과값을 도출해보세요(-- 3)
print(s[s >= np.mean(s)])

# 다음과 같은 결과값을 도출해보세요(-- 4)
print(s[[4, 2, 0]])

## 과제 2-2
# 다음의 데이터를 로드해보세요
s = pd.Series([0, 1, 2, 3, 4], index=['a', 'b', 'c', 'd', 'e'])

# 다음과 같은 결과값을 도출해보세요(-- 1)
print(s[['a', 'b', 'e']])

# 다음과 같은 결과값을 도출해보세요(-- 2)
print(s.get(['a', 'b', 'e']))

# 과제 2-3
# 다음의 데이터를 로드해보세요
import pandas as pd
df = pd.DataFrame({'C1': [0, 1, 2, 3],
                   'C2': [4, 5, 6, 7],
                   'C3': [8, 9, 10, np.nan]},
                  index=['R1', 'R2', 'R3', 'R4'])

# 다음 데이터의 index 와 column 을 확인해보세요
print(df.index)
print(df.columns)

# 다음 데이터에서 index 가 R1, R3, column 은 C1, C3 인 dataFrame 을 만들어보세요
# 이 때, 최소 3가지 방법 이상으로 만들어보세요
print(pd.DataFrame(df, index=['R1', 'R3'], columns=['C1', 'C3']))
print(df.loc[['R1', 'R3'], ['C1', 'C3']])
print(df[['C1', 'C3']].loc[['R1', 'R3']])

# 다음 데이터에서 C1 컬럼과 C2 컬럼의 값을 더한 C4 컬럼을 만들어보세요
# 이 때 2가지 방법으로 만들어 보세요
df['C4'] = df['C1'] + df['C2']
df.assign(C4=df['C1'] + df['C2'])

# 다음 데이터에서 C4 컬럼을 삭제해 보세요
# 이 때 2가지 방법이 있는데, 2가지 방법 모두 기술해보시고, 어떤 차이가 있는지 설명해보세요
df.drop(columns='C4')
del df['C4']

# 다음 코드의 실행 결과는 어떻게 될까요?
# 결과를 설명해 보시고, 만약 문제가 있다면 어떻게 개선해야 하는지 설명해보세요

# error 발생
df.iloc[0]

# 과제 3
# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 1)
print(np.array([1, 2, 3, 4, 5]))

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 2)
print(np.arange(10).reshape(2, 5))

# np.array() 와 np.asarray() 는 어떤 차이가 있나요?
# 간단하게 설명해 보세요

arr = np.array([1, 2, 3, 4, 5])
np_arr = np.array(arr)
print(arr is np_arr)

arr = np.array([1, 2, 3, 4, 5])
np_arr = np.asarray(arr)
print(arr is np_arr)

# 다음의 코드를 실행시키면 어떤 결과가 나오나요?
# np.asarray_chkfinite 함수를 중심으로 설명해 보세요

e_2 = [11, 12, 13, np.nan, 15]
try:
    np.asarray_chkfinite(e_2, dtype=float)
except ValueError:
    print("ValueError")

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 5)
np.zeros(5)

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 6)
np.ones(10)

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 7)
np.zeros((2, 5))

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 8)
np.arange(10).reshape(2, 5)

# 다음의 결과를 NumPy 함수만을 사용해서 도출해보세요(-- 9)
# 2가지 방법이 있습니다. 2가지 모두 기술해 보세요
np.eye(5)
np.identity(5)

# 과제 4
# NumPy 를 활용해서 정규분포(Normal distribution)를 따르는 개수가 24개인 무작위 샘플을 만들어보세요
# 이 때, 무작위 샘플은 한 번 실행되면 바뀌지 않아야 합니다.
# matrix 구조는 (2, 3, 4) 3차원 구조이어야 합니다.
np.random.seed(100)
np.random.normal(size=(2, 3, 4))

# 앞(head) 또는 뒤(tail) 가 나올 확률이 50% 인 동전 던지기를 20번 해본 결과 샘플을 만들어보세요
np.random.binomial(n=1, p=0.5, size=20)

# good 이 5개, bad 가 20개인 모집단에서 5개의 샘플을 무작위로 비복원추출 하는 것을 100번
# 시뮬레이션 한 결과 샘플을 만들어보세요
np.random.hypergeometric(ngood=5, nbad=20, nsample=5, size=100)

# 자유도가 2인 카이제곱분포로부터 100개의 난수를 생성해보세요
# 이를 히스토그램을 그려서 분포를 확인해보세요
import matplotlib.pyplot as plt
chi_value = np.random.chisquare(2, 100)
plt.hist(chi_value)

# 과제 5
# 다음의 list 자료구조를 NumPy의 float64 로 변경해주세요
# 이 때, 3가지 방법으로 변경하여 x_float64 에 저장해주세요

arr = [1.4, 2.6, 3.0, 4.9, 5.32]
print(np.array(arr, dtype='float64').dtype)
print(np.array(arr, dtype=np.float64).dtype)
print(np.float64(arr))
x_float64 = np.float64(arr)

# 위의 저장된 x_float64 를 다시 NumPy의 int64로 변경해보세요
# 이 때, 2가지 방법으로 변경해주세요
np.array(x_float64, dtype='int64')
x_float64.astype('int64')

# x_float64 를 문자열(string) 으로 변경해주세요
x_float64.astype(np.string_)