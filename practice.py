import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler
import matplotlib.pyplot as plt
import pandas as pd

np.set_printoptions(precision=2)
np.random.seed(100)

mu, sigma = 10, 2
x = mu + sigma * np.random.randn(100)
plt.hist(x)

np.mean(x)
np.std(x)

x[98:100] = 100
np.mean(x)
np.std(x)
plt.hist(x, bins=np.arange(0, 102, 2))

# 이상치가 포함된 데이터의 표준정규분포로의 표준화
x = x.reshape(-1, 1)
x_StandardScaler = StandardScaler().fit_transform(x)
np.mean(x_StandardScaler)
np.std(x_StandardScaler)

x_StandardScaler_zoom_in = x_StandardScaler[x_StandardScaler < 5]

# (2) 이상치가 포함된 데이터의 중앙값과 IQR 를 이용한 표준화
np.median(x)
Q1 = np.percentile(x, 25, axis=0)
Q3 = np.percentile(x, 75, axis=0)
IQR = Q3 - Q1

x_RobustScaler = RobustScaler().fit_transform(x)

np.median(x_RobustScaler)
np.mean(x_RobustScaler)
np.std(x_RobustScaler)

plt.hist(x_RobustScaler)
x_RobustScaler_zoon_in = x_RobustScaler[x_RobustScaler < 5]
plt.hist(x_RobustScaler_zoon_in, bins=np.arange(-3, 3, 0.2))

