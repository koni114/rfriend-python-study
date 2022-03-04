# 동일 길이로 나누어 범주 만들기.
# -> pd.cut()
# 동일 개수로 나누어서 범주 만들기
# -> pd.qcut()

import numpy as np
import pandas as pd

np.random.seed(123)
df = pd.DataFrame({'col_1': np.random.randint(20, size=20),
                   'col_2': np.random.randn(20)})

factor_col_1 = pd.cut(df.col_1, 4)



