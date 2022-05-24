import pandas as pd
from pandas import DataFrame
import numpy as np

df = DataFrame(data=np.arange(20).reshape(4, 5),
               columns = ['c1', 'c2', 'c3', 'c4', 'c5'],
               index = ['r1', 'r2', 'r3', 'r4'])

groupby_dict = {"r1": "row_g1",
                "r2": "row_g1",
                "r3": "row_g2",
                "r4": "row_g2"}

df.groupby(groupby_dict).sum()

groupby_dict = {"c1": "col_g1",
                "c2": "col_g1",
                "c3": "col_g2",
                "c4": "col_g2",
                "c5": "col_g2"}

df.groupby(groupby_dict, axis=1).sum()

df = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b'],
                   'value_1': np.arange(6),
                   'value_2': np.random.randn(6)})
df

df.groupby("group").count()