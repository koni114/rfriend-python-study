import pandas as pd
import numpy as np

# ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#  'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

df = pd.read_csv('/Users/heojaehun/gitRepo/rfriend-python-study/day1/data/train.csv',
                 header=0,
                na_values=['??', "NaN", ""])


df['Embarked'].value_counts()
df['Embarked'] = np.where(df['Embarked'].isnull(), 'S', df['Embarked'])


X_new = np.array([[9, -10, 1], [5, -5, 3], [1, 0, 5]])
(X_new - np.min(X_new, axis=0)) / (np.max(X_new, axis=0) - np.min(X_new, axis=0))

from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
min_max_scaler.fit_transform(X_new)

