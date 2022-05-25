import pandas as pd
import numpy as np

personnel_df = pd.DataFrame({'sequence': [1, 3, 2],
                             'name': ['park', 'lee', 'choi'],
                             'age': [30, 20, 40]})

personnel_df.sort_values(["sequence"], inplace=True)
print(personnel_df[["age", "name", "sequence"]])


personnel_df.sort_values(["sequence"], ascending=False)

personnel_df = pd.DataFrame({'sequence': [1, 3, np.nan],
                             'name': ['park', 'lee', 'choi'],
                             'age': [30, 20, 40]})

personnel_df.sort_values(["sequence"], na_position="first")
personnel_df.sort_values(["sequence"], na_position="last")


personnel_tuple = [(1, 'park', 30),
                   (3, 'lee', 20),
                   (2, 'choi', 40)]

sorted(personnel_tuple, key=lambda x: -x[1])