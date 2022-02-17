# 과제 1
import numpy as np
import pandas as pd

arr = np.array([0, 30, 45, 60, 90])
print(np.sin(arr * np.pi / 180))

# 다음의 곡선 그래프를 그려보세요
import matplotlib.pyplot as plt
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)

# 다음의 x에 해당하는 값을 구해보세요
# np.sin(x) = 1
print(np.arcsin(1))

# 다음의 x에 해당하는 값을 구해보세요
# np.cos(x) = -1
print(np.arccos(-1))

# 다음의 x에 해당하는 값을 구해보세요
print(np.arctan(0))

# 180 degree 를 radian 으로 변환하면 어떤 값이 나오나요?
# NumPy 식을 사용하여 확인해보세요
print(np.deg2rad(180))

# 과제 2
# 다음의 배열에서, 양수이면 1, 0이면 0, 음수이면 -1을 리턴해보세요
c = np.array([-2, -1, 0, 1, 2])
print(np.sign(c))

# 다음의 배열에서, 정수와 소수점을 구분하는 2개의 배열을 반환해보세요
z = np.array([3.5, 7.8, -10.3])
split_z = np.modf(z)

print(split_z[0])
print(split_z[1])

# 다음의 배열에서 제곱값과 제곱근(Root) 값을 계산해보세요
y = np.array([1, 4, 100])
np.sqrt(y)   # 제곱근
np.square(y)  # 제곱

# 두가지 방법을 사용하여, 다음의 배열의 절대값을 계산해보세요
x = np.array([-100, 1, -4, 100])
print(np.abs(x))
print(np.fabs(x))

# 과제 3
# np.round, np.rint, np.fix, np.ceil, np.floor
a = np.array([0, 1, 2, np.nan, 4, np.inf, np.NINF, np.PINF])

# 배열에 NaN이 있으면 True 를 반환하는 결과를 도출해보세요
print(np.isnan(a))

# 배열에 유한수(finite) 포함 여부를 확인해보세요
print(np.isfinite(a))

# 배열에 무한수(infinite) 포함 여부를 확인해보세요
print(np.isinf(a))

# 배열에 음의 무한수 포함 여부를 확인해보세요
print(np.isneginf(a))

# 배열에 양의 무한수 포함 여부를 확인해보세요
print(np.isposinf(a))

# 다음의 데이터를 로드해보세요
all_TF = [[True, False], [True, True]]

# 배열의 모든 원소가 참이면 True, 아니면 False 를 반환해보세요
np.all(all_TF)

# 배열의 각 행의 원소가 모두 참이면, True, 아니면 False 를 반환해보세요
np.all(all_TF, axis=1)

# 배열의 각 열의 원소가 모두 참이면, True, 아니면 False 를 반환해보세요
np.all(all_TF, axis=0)

# - 다음의 데이터를 로드해보세요
any_TF = [[False, False], [True, True]]

# 배열의 1개 이상의 원소가 True 면 True, 아니면 False 를 반환해보세요
np.any(any_TF)

# 배열의 행 별로 1개 이상 원소가 True 면 True, 아니면 False 를 반환해보세요
np.any(any_TF, axis=1)

# 배열의 열 별로 1개 이상 원소가 True 면 True, 아니면 False 를 반환해보세요
np.any(any_TF, axis=0)

# 과제 4
# 평균이 0, 표준편차가 1인 정규분포로부터 난수 10000개를 생성해보세요
import pandas as pd
normal_value = np.random.normal(0, 1, 10000)
df = pd.DataFrame(normal_value, columns=['normal_value'])

# 해당 데이터의 기술 통계량을 알아보고, 히스토그램으로 분포를 살펴보세요
df.describe()
plt.hist(df)

# 해당 데이터 중 -3, 3 의 값을 벗어나는 데이터를 slicing 해보시고, 이의 개수를 출력해보세요
print(df[(np.abs(df) > 3).any(1)].count())

# np.sign() 함수를 사용해, +- sigma 를 벗어나는 관측치값을 모두 +- 3으로 대체해 보세요
df[(np.abs(df) > 3).any(1)] = np.sign(df[(np.abs(df) > 3).any(1)]) * 3

# 과제 5
# reshape 함수에서 -1 이 의미하는 바는 무엇인가요?
# 다른 차원의 값을 설정해두고, -1 로 설정해두면 가능한 나머지 차원 수에 대해서 자동으로 계산됨
arr = np.arange(20).reshape(4, 5)
print(arr)
print(arr.reshape(10, -1))


